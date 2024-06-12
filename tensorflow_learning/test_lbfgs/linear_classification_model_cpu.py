import tensorflow as tf


class LinearClassificationModel(tf.keras.Model):
    def __init__(self, dim_feat=0):
        super(LinearClassificationModel, self).__init__()
        self.dim_feat = dim_feat
        self.denseout = tf.keras.layers.Dense(
            units=1, input_shape=(dim_feat, ), kernel_initializer='zeros',
            bias_initializer='zeros', activation=tf.keras.activations.sigmoid, dtype=tf.float64)

    @tf.function
    def make_sparse_tensor(self, indices, values):
        # bool : n_batch x size_max_array
        b_exist = tf.math.logical_or(tf.math.not_equal(indices, 0), tf.math.not_equal(values, 0))
        # int : N_nonzeros x 2(ith-batch, jth-index of array)
        idx2d_exist = tf.where(b_exist)
        # int : N_nonzeros x 1(ith-batch)
        #nth_batch = tf.slice(idx2d_exist, [0,0], [idx2d_exist.shape[0], 1])
        nth_batch = tf.slice(idx2d_exist, [0,0], [tf.shape(idx2d_exist)[0], 1])
        # int : N_nonzeros x 1(idx of sparse vector)
        #idx_sparse = tf.expand_dims(tf.cast(tf.ragged.boolean_mask(indices, b_exist), tf.int64), axis=1)
        idx_sparse = tf.expand_dims(tf.cast(tf.ragged.boolean_mask(indices, b_exist), tf.int64).values, axis=1)

        # int : N_nonzeros x 2(ith-batch, idx of sparse vector)
        idx_bnfi = tf.concat([nth_batch, idx_sparse], axis=1)
        # floatX : N_nonzeros x 1(value at (nth-batch, idx of sparse vector))
        val_bnfi = tf.ragged.boolean_mask(values, b_exist).values

        tf_sparse = tf.sparse.SparseTensor(
            indices=idx_bnfi,
            values=val_bnfi,
            dense_shape=[tf.shape(indices)[0], self.dim_feat])
        tf_sparse = tf.sparse.reorder(tf_sparse) # if debug , turn off it
        return tf_sparse

    @tf.function
    def reduce_sparse_tensor(self, tensor3d):
        # int : size(number of indices in one batch) x 3
        idx_3d = tensor3d.indices
        # int : size(number of indices in one batch) x 2
        idx_2d = tf.gather(idx_3d, [0, 2], axis=1)
        # floatX : values x 1
        val_feat = tensor3d.values
        tf_sparse = tf.sparse.SparseTensor(
            indices=idx_2d,
            values=val_feat,
            dense_shape=[tf.shape(tensor3d)[0], self.dim_feat]
        )
        tf_sparse = tf.sparse.reorder(tf_sparse) # if debug , turn off it
        return tf_sparse

    def call(self, input):
        rawfeat = input['sparse_feat']
        feat = self.reduce_sparse_tensor(rawfeat)
        result = self.denseout(feat)
        result = tf.clip_by_value(result, 1.0e-16, 1.-1.0e-16)
        return result
