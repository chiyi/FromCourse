import tensorflow as tf

class Learner(object): 
    def __init__(self, n_classes, train_dataset_unbatch=None, train_dataset=None, valid_dataset=None, train_batch_size=128):
        self.n_classes = n_classes
        self.train_batch_size = train_batch_size
        self.num_epochs = 100
        self.num_epochs_validation = 10
        self.model = None #CNNModel(pic_height=128, pic_width=128, n_classes=n_classes)
        self.__init_train_dataset__(train_dataset, train_dataset_unbatch, train_batch_size)
        self.valid_dataset = valid_dataset
        self.optimizer = tf.keras.optimizers.Adam(learning_rate=0.001, beta_1=0.8, beta_2=0.99, epsilon=1e-07)
        self.train_loss = tf.keras.metrics.Mean(name='train_loss')
        self.valid_loss = tf.keras.metrics.Mean(name='valid_loss')
        self.train_acc = tf.keras.metrics.Mean(name='train_acc')
        self.valid_acc = tf.keras.metrics.Mean(name='valid_acc')

    def __init_train_dataset__(self, train_dataset, train_dataset_unbatch, train_batch_size):
        if train_dataset is not None:
            self.train_dataset = train_dataset
        else:
            self.train_dataset = train_dataset_unbatch.batch(train_batch_size)  

    @tf.function
    def train_step(self, features, labels):  
        with tf.GradientTape() as tape:
            #predictions = self.model(features)
            predictions = self.model(features, training=True)
            loss = tf.keras.losses.sparse_categorical_crossentropy(y_true=labels, y_pred=predictions, from_logits=True)
        gradients = tape.gradient(loss, self.model.trainable_variables)        
        self.optimizer.apply_gradients(zip(gradients, self.model.trainable_variables))
        self.train_loss(loss)
        self.train_acc(tf.keras.metrics.sparse_categorical_accuracy(y_true=labels, y_pred=predictions))

    @tf.function
    def valid_step(self, features, labels):        
        with tf.GradientTape() as tape:          
            predictions = self.model(features)          
            loss = tf.keras.losses.sparse_categorical_crossentropy(y_true=labels, y_pred=predictions, from_logits=True)
        self.valid_loss(loss)
        self.valid_acc(tf.keras.metrics.sparse_categorical_accuracy(y_true=labels, y_pred=predictions))

    def train(self):
        for epoch in range(self.num_epochs):
            epoch_start_time = time.time()
            self.train_loss.reset_states()
            self.valid_loss.reset_states()
            self.train_acc.reset_states()
            self.valid_acc.reset_states()
            
            for features, labels in self.train_dataset:
                self.train_step(features, labels)

            if epoch % self.num_epochs_validation == self.num_epochs_validation - 1:
                for features, labels in self.valid_dataset:
                    self.valid_step(features, labels)
                template = 'Epoch {} {} sec(s) , Loss: {}, CategoricalAccurancy:{}, Valid Loss: {}, Valid CategoricalAccurancy:{}'
                print(template.format(epoch + 1,
                                      ("%2.2f" % (time.time()-epoch_start_time)),
                                      ("%3.6f" % self.train_loss.result()),
                                      ("%3.6f" % self.train_acc.result()),
                                      ("%3.6f" % self.valid_loss.result()),
                                      ("%3.6f" % self.valid_acc.result())))
