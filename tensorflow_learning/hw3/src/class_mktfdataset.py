import tensorflow as tf

class MkTFDataset(object):
    def __init__(self):
        self.size_fulltraindata = None
        self.train_dataset = None
        self.valid_dataset = None

    def init_fulltraindata(self, arr_x, arr_y, batch_size=128, ratio=0.8):
        self.batch_size = batch_size
        self.size_fulltraindata = len(arr_x)
        self.fulltrain_dataset = tf.data.Dataset.from_tensor_slices((arr_x, arr_y))
        self.train_dataset = None
        self.valid_dataset = None
        self.fulltrain_dataset_prime = None
        self.Split(batch_size, ratio)

    def Split(self, batch_size=128, ratio=0.8):
        train_size = int(ratio * self.size_fulltraindata)
        self.train_dataset = self.fulltrain_dataset.take(train_size)
        self.train_dataset = self.train_dataset.shuffle(train_size, seed=14522).batch(batch_size)
        self.valid_dataset = self.fulltrain_dataset.skip(train_size).batch(1)
        self.fulltrain_dataset_prime = self.fulltrain_dataset.batch(1)

    def set_validation_dataset(self, arr_x, arr_y):
        self.valid_dataset = None
        self.valid_dataset = tf.data.Dataset.from_tensor_slices((arr_x, arr_y)).batch(1)

    def set_training_dataset(self, arr_x, arr_y, batch_size=128):
        train_size = len(arr_x)
        self.batch_size = batch_size
        self.train_dataset = None
        self.train_dataset = tf.data.Dataset.from_tensor_slices((arr_x, arr_y))
        self.train_dataset = self.train_dataset.take(train_size)
        self.train_dataset = self.train_dataset.shuffle(train_size, seed=834121).batch(batch_size)
