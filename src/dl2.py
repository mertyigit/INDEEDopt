import tensorflow as tf

# This part can be uncommented if GPU is available in computer system.

#tf.test.is_gpu_available

#from tensorflow.python.client import device_lib
#print(device_lib.list_local_devices())


### Modified on Feb 10 2021 due to tensorflow update
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.metrics import r2_score
from sklearn import preprocessing
from tqdm import tqdm
from sklearn.preprocessing import StandardScaler
import math
from sklearn.preprocessing import MinMaxScaler
from time import time
np.set_printoptions(suppress=True)    

def dl2(param_size, num_prop, file_name):
    
    df_gold = pd.read_csv("dl-gold.csv")
    df_gold = df_gold.iloc[:, 0:num_prop]
    
    df_weight = pd.read_csv("dl-weight.csv")
    df_weight = df_weight.iloc[:, 0:num_prop]
    
    data = pd.read_csv(file_name)
    
    data_size = data.shape[0]
    properties = np.arange(0, num_prop)
    
    x = data.loc[:,data.columns[range(param_size)]]
    y = data.loc[:,data.columns[range(param_size, num_prop+param_size)]]
    x = np.asarray(x).astype(np.float32)
    y = np.asarray(y).astype(np.float32)
    x_train_ns, x_test_ns, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    y_train_ns = y_train
   #y_train_ns = y_train.astype("float32")
    y_test_ns = y_test
   #y_test_ns =  y_test.astype("float32")
    
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train_ns)
    x_test = scaler.transform(x_test_ns)
    
    y_train = scaler.fit_transform(y_train_ns)
    y_test = scaler.transform(y_test_ns)
    y_train= y_train_ns
    y_test = y_test_ns
    
    tf.keras.backend.clear_session()
    
    # MODEL FOR REGRESSION PART
    def build_model():
        model = tf.keras.Sequential([
            layers.Dense(num_prop,activation=tf.nn.relu, input_shape=[param_size]),
            layers.Dense(num_prop, activation=tf.nn.relu),
            layers.Dense(num_prop, activation='linear')
        ])
        opt = tf.keras.optimizers.Adam(lr=0.001)
        model.compile(loss='mean_absolute_error', optimizer=opt, metrics=['mean_absolute_error', 'mean_squared_error'])
    
        return model
    model = build_model()
    
    #The early stopping algorithm
    from tensorflow.keras.callbacks import EarlyStopping

    es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=100)
    
    EPOCHS = 50000
    pbar = tqdm(total=EPOCHS)
    
    class PrintDot(keras.callbacks.Callback):
      def on_epoch_end(self, epoch, logs):
        pbar.update()
    

    history = model.fit(
        x_train, y_train,
        epochs=EPOCHS, 
        validation_data=(x_test, y_test),
        verbose=0,
        callbacks=[PrintDot(), es]
    )

    pbar.close()
    
    
    scores = model.evaluate(x_test, y_test, verbose=0)
    print("%s: %.2f" % (model.metrics_names[1], scores[1]))
    
    file = open("accuracy.dat","a+")
    file.write(str(scores[1]) + "\n")
    file.close()
    
    
    #tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES)
    #
    #
    #weights = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, 'dense_2/kernel')
    #
    #
    #
    #init_op = tf.initialize_all_variables()
    #
    #
    #with tf.Session() as sess:
    #    sess.run(init_op) 
    #    ww = sess.run(weights)
    #    
    
    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    
    model.save_weights("model.h5")
    print("Saved model to disk")
    
    return scores[1]
    
    
