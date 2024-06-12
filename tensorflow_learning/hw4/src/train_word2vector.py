import tensorflow as tf
tf.executing_eagerly() #check
tf.debugging.set_log_device_placement(True)

import os
import numpy as np
import pandas as pd
import time


class Word2Vec(tf.keras.Model):
  def __init__(self, vocab_size, embedding_dim, num_ns):
    super(Word2Vec, self).__init__()
    self.target_embedding = tf.keras.layers.Embedding(vocab_size, 
                                      embedding_dim,
                                      input_length=1,
                                      name="w2v_embedding", )
    self.context_embedding = tf.keras.layers.Embedding(vocab_size, 
                                       embedding_dim, 
                                       input_length=num_ns+1)
    self.dots = tf.keras.layers.Dot(axes=(3,2))
    self.flatten = tf.keras.layers.Flatten()

  def call(self, pair):
    target, context = pair
    we = self.target_embedding(target)
    ce = self.context_embedding(context)
    dots = self.dots([ce, we])
    return self.flatten(dots)


targets = []
with open("train_word2vec/word2vec_targets_sen20.txt", mode='r') as fr:
  lines = fr.readlines()
  for linei in lines:
    targets.append(int(linei))


contexts = []
with open("train_word2vec/word2vec_contexts_sen20.txt", mode='r') as fr:
  lines = fr.readlines()
  for linei in lines:
    str_shape, str_bytes = linei.split('\t')
    tmp_deserialized_data = np.frombuffer(eval(str_bytes), dtype='int64').reshape(eval(str_shape))
    contexts.append(tmp_deserialized_data)


labels = []
with open("train_word2vec/word2vec_labels_sen20.txt", mode='r') as fr:
  lines = fr.readlines()
  for linei in lines:
    str_shape, str_bytes = linei.split('\t')
    tmp_deserialized_data = np.frombuffer(eval(str_bytes), dtype='int64').reshape(eval(str_shape))
    labels.append(tmp_deserialized_data)


def train_word2vector():
    BATCH_SIZE = 256 #1024
    BUFFER_SIZE = len(targets)
    ds_word2vec = tf.data.Dataset.from_tensor_slices(((targets, contexts), labels))
    ds_word2vec = ds_word2vec.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)
    
    vocab_size = 8192
    embedding_dim = 512 #128
    
    model_word2vec = Word2Vec(vocab_size, embedding_dim, num_ns=4)
    model_word2vec.compile(
        optimizer='adam',
        loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
        metrics=['accuracy'])
    
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="logs")
    
    model_word2vec.fit(ds_word2vec, epochs=20, callbacks=[tensorboard_callback])
    
    model_word2vec.save("models/word2vec_sen20.tf", save_format='tf')


train_word2vector()
