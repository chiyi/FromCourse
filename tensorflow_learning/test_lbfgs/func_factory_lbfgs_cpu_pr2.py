import numpy
import random
import tensorflow as tf
import tensorflow_probability as tfp

#tf.executing_eagerly()

class FunctionFactory(object):
    def __init__(self, model, ds_train, dim_feat, regularization=50, val_dtype=tf.float64):
        self.model = model
        assert dim_feat == self.model.dim_feat
        self.dim_model = dim_feat + 1
        self.ds_train = ds_train
        # obtain the shapes of all trainable parameters in the model
        self.shapes = tf.shape_n(model.trainable_variables)
        self.n_tensors = len(self.shapes)
        self.regularization = regularization
        self.iter = 0
        self.val_dtype=val_dtype
        self.__init_shape__()

    def __init_shape__(self):
        # we'll use tf.dynamic_stitch and tf.dynamic_partition later, so we need to
        # prepare required information first
        self.count = 0
        self.idx = [] # stitch indices
        self.part = [] # partition indices
         
        for i, shape in enumerate(self.shapes):
            n = numpy.product(shape)
            self.idx.append(tf.reshape(tf.range(self.count, self.count+n, dtype=tf.int32), shape))
            self.part.extend([i]*n)
            self.count += n
         
        self.part = tf.constant(self.part)

    def gen_function(self):

        @tf.function
        def assign_model_weights(model_weights_1d):
            weights = tf.dynamic_partition(model_weights_1d, self.part, self.n_tensors)
            for i, (shape, param) in enumerate(zip(self.shapes, weights)):
                self.model.trainable_variables[i].assign(tf.reshape(param, shape))
         
        # now create a function that will be returned by this factory
        @tf.function
        def f(x):
            print('x=', x)
            # update the parameters in the model
            assign_model_weights(x)

            with tf.GradientTape() as tape:
                x2 = tf.reduce_sum(tf.math.square(tf.dynamic_stitch(self.idx, self.model.trainable_variables)))
                l2_penalty = 0.5 * self.regularization * x2
            tmp_grads = tape.gradient(l2_penalty, self.model.trainable_variables)
            grads = tf.dynamic_stitch(self.idx, tmp_grads)
            # for debug during initialization
            print('grads=',grads)
            print(grads.shape) 
            total_loss = l2_penalty

            sumlogloss = tf.constant(0., self.val_dtype)
            for ith_batch, ds_i in enumerate(self.ds_train):
                with tf.GradientTape() as tape:
                    # calculate the loss
                    predictions = self.model(ds_i)
                    labels = ds_i['label']
                    #if random.random()<1.0e-5:
                    #    tf.print('(p,y)', predictions[0], labels[0])
                    logloss = tf.keras.losses.binary_crossentropy(y_true=tf.expand_dims(labels, axis=1), y_pred=predictions)
                    sumlogloss_i = tf.reduce_sum(logloss)
                    sumlogloss += sumlogloss_i
                    total_loss += sumlogloss_i
                tmp_grads = tape.gradient(sumlogloss, self.model.trainable_variables)
                grads += tf.dynamic_stitch(self.idx, tmp_grads)
            print('grads=', grads)

            # print out iteration & loss
            f.iter.assign_add(1)
            tf.print(
                'Iter:', f.iter,
                ', loss:', total_loss,
                ', sumlogloss:', sumlogloss,
                ', x2:', x2,
                ', bias=', self.model.trainable_variables[1])
            print('total_loss=', total_loss, 'grads=', grads) # for debug during initialization
         
            return total_loss, grads
         
        # store these information as members so we can use them outside the scope
        f.iter = tf.Variable(0)
        f.idx = self.idx
        f.part = self.part
        f.shapes = self.shapes
        f.assign_model_weights = assign_model_weights
        f.history = []
        return f

