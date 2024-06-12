from src.myenv import tf, np


def load_train_img_dataset():
    #train_img_dataset 
    res = tf.keras.preprocessing.image_dataset_from_directory(
        directory="data/food-11_fortf/training", labels='inferred', label_mode='int', class_names=["0", "1", "2" ,"3", "4", "5", "6", "7", "8", "9", "10"],
        color_mode='rgb', batch_size=1, image_size=(128, 128), shuffle=False, seed=12345,
        validation_split=None, subset=None, interpolation='nearest', follow_links=False
    )
    return res

preprocessing_data_augmentation = tf.keras.Sequential(
    [
     tf.keras.layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical"),
     tf.keras.layers.experimental.preprocessing.RandomRotation(0.041667, interpolation="nearest") #15/360 * 2pi
    ]
)
#train_img_dataset_2 = train_img_dataset.map(lambda x,y: (preprocessing_data_augmentation(x), y))

def load_valid_img_dataset():
    #valid_img_dataset 
    res = tf.keras.preprocessing.image_dataset_from_directory(
        directory="data/food-11_fortf/validation", labels='inferred', label_mode='int', class_names=["0", "1", "2" ,"3", "4", "5", "6", "7", "8", "9", "10"],
        color_mode='rgb', batch_size=1, image_size=(128, 128), shuffle=False, seed=12345,
        validation_split=None, subset=None, interpolation='nearest', follow_links=False
    )
    return res

def read_tfdataset(dataset, b_withlabel=True):
    len_dataset = dataset.cardinality().numpy()
    x = np.zeros((len_dataset, 128, 128, 3), dtype=np.uint8)
    y = np.zeros(len_dataset, dtype=np.uint8)
    for idx, data_i in enumerate(dataset):
        if b_withlabel:
            data_i_x, data_i_y = data_i
            y[idx] = data_i_y
        else:
            data_i_x = data_i
        x[idx, :, :] = data_i_x
        
    if b_withlabel:
        return x, y
    else:
        return x
