from subprocess import check_output
import tensorflow as tf


class MkTFDataset(object):
    def __init__(self, list_files_train, list_files_test=None, dim_feat=10246007):
        self.dim_feat = dim_feat #for sparse vector features
        self.size_alltraindata = None
        self.size_train = 0
        self.size_valid = 0
        self.maxrows_mem_shuffle = 500000
        self.list_files_train = list_files_train
        self.list_files_test = list_files_test
        self.dataset_train = None
        self.dataset_valid = None
        self.dataset_test = None
        self.csv_cols = ['Label', 'Features']
        self.csv_types = [
            #tf.float32,          # label
            tf.float64,          # label
            tf.string,           
        ]

    #@tf.function
    #def convert_to_tfarr(self, tf_inpstr, dtype=tf.int32):
    #    tf_tmpstr = tf.strings.regex_replace(tf_inpstr, '[\[\]]', '')
    #    res = tf.strings.to_number(tf.strings.split(tf_tmpstr, ','), dtype)
    #    return res

    @tf.function
    def extract_to_tfarr(self, tf_inpstr, ith=0, sep=':', dtype=tf.int32):
        tf_tmparr = tf.strings.split(tf.strings.strip(tf_inpstr), sep=' ')
        tmpstr = tf.map_fn(fn=lambda x: tf.strings.split(x, sep=sep)[ith], elems=tf_tmparr)
        res = tf.map_fn(fn=lambda x: tf.strings.to_number(x, dtype), elems=tmpstr, dtype=dtype)
        return res

    #@tf.function
    #def package_data(self, row):
    #    out_indices_feat = self.convert_to_tfarr(row[2], tf.int32)
    #    out_values_feat = self.convert_to_tfarr(row[3], tf.float32)
    #
    #    res = {
    #        'label': row[0],
    #        'Id': row[1],
    #        'indices_feat': out_indices_feat,
    #        'values_feat': out_values_feat,
    #        'AdGroupId': row[4],
    #    }
    #    return res

    @tf.function
    def package_data(self, row):
        indices_feat = self.extract_to_tfarr(row[1], 0, dtype=tf.int64)
        values_feat = self.extract_to_tfarr(row[1], 1, sep=':', dtype=tf.float64)
        tmp_0 = tf.zeros_like(indices_feat, dtype=tf.int64)
        tmp_indices_tensor = tf.stack([tmp_0, indices_feat], axis=1)

        out_feat = tf.sparse.SparseTensor(tmp_indices_tensor, values_feat, [1, self.dim_feat])

        res = {
            'label': row[0],
            'sparse_feat': out_feat,
            #'features': row[1],
            #'indices_feat': indices_feat,
            #'values_feat': values_feat,
        }
        return res

    def read_csv(self, list_files):
        list_colnames = self.csv_cols
        dataset = tf.data.experimental.CsvDataset(
         list_files, self.csv_types,
         header = False,
         field_delim = '\t',
        )
        dataset = dataset.map(lambda *cols: self.package_data(cols))
        for idx, irow in enumerate(dataset):
            print(irow)
            break
        return dataset

    def get_datasize(self, list_files):
        lines = map(lambda x: int(check_output(['wc', '-l', x]).split()[0]), list_files)
        lines = filter(lambda x: x>0, lines)
        size_data = sum(map(lambda x: x-1, lines))
        return size_data

    def init_traindata(self, batch_size=4, ratio=0.8):
        self.alltraindata = self.read_csv(self.list_files_train)
        self.size_alltraindata = self.get_datasize(self.list_files_train)
        self.Split(batch_size, ratio)

    def init_testdata(self, batch_size=4):
        self.dataset_test = self.read_csv(self.list_files_test).batch(batch_size)
        self.size_test = self.get_datasize(self.list_files_test)

    def init_smaller_traindata(self, batch_size=4, ratio=0.8):
        """init_smaller_traindata(batch_size=4, ratio=0.8)"""
        self.alltraindata = self.read_csv(self.list_files_train)
        self.size_alltraindata = int(0.1 * self.get_datasize(self.list_files_train))
        self.Split(batch_size, ratio)

    def init_testio_traindata(self, batch_size=4, ratio=0.8):
        """init_testio_traindata(batch_size=4, ratio=0.8)"""
        self.alltraindata = self.read_csv(self.list_files_train)
        self.size_alltraindata = int(0.0001 * self.get_datasize(self.list_files_train))
        self.Split(batch_size, ratio)
        self.dataset_prime_alltrain = self.alltraindata.take(self.size_alltraindata).batch(1)

    def Split(self, batch_size=4, ratio=0.8):
        """Split(batch_size=4, ratio=0.8)"""
        self.size_train = int(ratio * self.size_alltraindata)
        self.size_valid = self.size_alltraindata - self.size_train
        self.dataset_train = self.alltraindata.take(self.size_train)
        size_shuffle = min(self.maxrows_mem_shuffle, self.size_train)
        #self.dataset_train = self.dataset_train.shuffle(size_shuffle, seed=14522).batch(batch_size)
        self.dataset_train = self.dataset_train.batch(batch_size)
        self.dataset_valid = self.alltraindata.skip(self.size_train).take(self.size_valid).batch(1)
        self.dataset_prime_alltrain = self.alltraindata.batch(1)
