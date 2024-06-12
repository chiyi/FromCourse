import math
import tensorflow as tf

class VGG16_CNNModel(tf.keras.Model):
    def __init__(self, pic_height=128, pic_width=128, n_classes=11):
        super(VGG16_CNNModel, self).__init__()
        self.pic_width = pic_width
        self.pic_height = pic_height        
        self.n_classes = n_classes
        self.const_halfpi = math.pi/2
 
        self.data_augmentation = tf.keras.Sequential(
            [
             tf.keras.layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical"),
             tf.keras.layers.experimental.preprocessing.RandomTranslation(height_factor=0.1, width_factor=0.1, interpolation='nearest'),
             tf.keras.layers.experimental.preprocessing.RandomRotation(0.0625, interpolation="nearest") #, #1/16 * 2pi
            ]
        )

        self.image2dlayers_R1 = tf.keras.Sequential(
            [
             #tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), padding='same', input_shape=(pic_height, pic_width, 3), activation=tf.keras.activations.relu), #failed when local ipynb
             tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), padding='same', input_shape=(128, 128, 3), activation=tf.keras.activations.relu),
             tf.keras.layers.Conv2D(filters=64, kernel_size=(3, 3), padding='same', activation=tf.keras.activations.relu),
             tf.keras.layers.MaxPooling2D(2, strides=(2,2), padding='same')
            ]
        )
        self.image2dlayers_R2 = tf.keras.Sequential(
            [
             tf.keras.layers.Conv2D(filters=128, kernel_size=(3, 3), padding='same', activation=tf.keras.activations.relu),
             tf.keras.layers.Conv2D(filters=128, kernel_size=(3, 3), padding='same', activation=tf.keras.activations.relu),
             tf.keras.layers.MaxPooling2D(2, strides=(2,2), padding='same')
            ]
        )        
        self.image2dlayers_R3 = tf.keras.Sequential(
            [
             tf.keras.layers.Conv2D(filters=256, kernel_size=(3, 3), padding='same', activation=tf.keras.activations.relu),
             tf.keras.layers.Conv2D(filters=256, kernel_size=(3, 3), padding='same', activation=tf.keras.activations.relu),
             tf.keras.layers.Conv2D(filters=256, kernel_size=(3, 3), padding='same', activation=tf.keras.activations.relu),
             tf.keras.layers.MaxPooling2D(2, strides=(2,2), padding='same')
            ]
        )
        self.image2dlayers_R4 = tf.keras.Sequential(
            [
             tf.keras.layers.Conv2D(filters=512, kernel_size=(3, 3), padding='same', activation=tf.keras.activations.relu),
             tf.keras.layers.Conv2D(filters=512, kernel_size=(3, 3), padding='same', activation=tf.keras.activations.relu),
             tf.keras.layers.Conv2D(filters=512, kernel_size=(3, 3), padding='same', activation=tf.keras.activations.relu),
             tf.keras.layers.MaxPooling2D(2, strides=(2,2), padding='same')
            ]
        )
        self.image2dlayers_R5 = tf.keras.Sequential(
            [
             tf.keras.layers.Conv2D(filters=512, kernel_size=(3, 3), padding='same', activation=tf.keras.activations.relu),
             tf.keras.layers.Conv2D(filters=512, kernel_size=(3, 3), padding='same', activation=tf.keras.activations.relu),
             tf.keras.layers.Conv2D(filters=512, kernel_size=(3, 3), padding='same', activation=tf.keras.activations.relu),
             tf.keras.layers.MaxPooling2D(2, strides=(2,2), padding='same')
            ]
        )                

        #self.flat = tf.keras.layers.Flatten()
        #self.dropout1 = tf.keras.layers.Dropout(0.2)
        #self.flatten1dlayersR = tf.keras.Sequential(
        #    [
        #     #tf.keras.layers.Dense(units=4096, activation=tf.keras.activations.relu)
          
        #     tf.keras.layers.Dense(units=4096, activation=tf.keras.activations.relu),
        #     tf.keras.layers.Dense(units=1024, activation=tf.keras.activations.relu),
        #     tf.keras.layers.Dense(units=256, activation=tf.keras.activations.relu),
        #     #tf.keras.layers.Dense(units=128, activation=tf.keras.activations.relu)
        #    ]
        #)
        #self.dropout2 = tf.keras.layers.Dropout(0.2)
        ##self.outputlayer = tf.keras.layers.Dense(units=n_classes, activation=tf.keras.activations.relu)
        self.outputlayer = tf.keras.layers.Dense(units=n_classes, activation=tf.keras.activations.linear)
        ##self.outputlayer = tf.keras.layers.Dense(units=n_classes, activation=tf.keras.activations.sigmoid)

 
    def call(self, input, training=False):
        local_input = input
        if training:
            local_input = self.data_augmentation(local_input)

        resultR = self.image2dlayers_R1(local_input)
        resultR = self.image2dlayers_R2(resultR)
        resultR = self.image2dlayers_R3(resultR)
        resultR = self.image2dlayers_R4(resultR)
        resultR = self.image2dlayers_R5(resultR)
        #resultR = self.flat(resultR)
        #resultR = self.dropout1(resultR, training=training)
        #resultR = self.flatten1dlayersR(resultR)
        #resultR = self.dropout2(resultR, training=training)
          
        #result = tf.concat([resultR], 1)
        result = self.outputlayer(resultR)
 
        return result
