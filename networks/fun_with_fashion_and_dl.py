import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import tensorflow as tf

physical_devices = tf.config.list_physical_devices('GPU')
try:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)
except:
    print("No gpu")

from tensorflow.keras.datasets import fashion_mnist

(train_images, train_labels), (test_images, test_labels) = \
    fashion_mnist.load_data()

import matplotlib.pyplot as plt

n_immagini = 10

window, ax = plt.subplots(1,  n_immagini, figsize=(10, 10))


for i in range(n_immagini):
    ax[i].axis('off')
    ax[i].imshow(train_images[i], cmap=plt.cm.binary )

plt.figtext(.45, .30, train_labels[0:n_immagini],
            style='italic',
            bbox={'facecolor': 'yellow'},
            fontsize='xx-large',
            fontweight='bold',)

plt.show()

train_images = train_images.reshape((60000, 28, 28, 1))
x_train = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28, 28, 1))
x_test = test_images.astype('float32') / 255

from tensorflow.keras.utils import to_categorical

y_train = to_categorical(train_labels)
y_test = to_categorical(test_labels)
num_classes = train_labels.shape[1]

optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001)
model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D(filters=25, kernel_size=(3,3), activation='relu', padding='same',
                                 input_shape=(28,28,1)))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.SpatialDropout2D(0.3))
model.add(tf.keras.layers.Conv2D(filters=25, kernel_size=(3,3), activation='relu', padding='valid'))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Conv2D(filters=25, kernel_size=(3,3), activation='relu', padding='valid'))
model.add(tf.keras.layers.AvgPool2D(2))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(160, activation="relu"))
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Dense(80, activation="relu"))
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Dense(10,activation=tf.nn.softmax))

model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
model.summary()

history = model.fit(
    x_train,
    y_train,
    epochs=20,
    batch_size=8)

test_loss, test_acc = model.evaluate(x_train,y_train)
print('\nAccuracy:', test_acc)
print('\nLoss: ', test_loss)

import matplotlib.pyplot as plt

history_plot = plt.figure(
    "History plot",
    figsize=(8, 8)
)

ax1 = history_plot.add_subplot(211)
ax1.set_xlabel(
    "EPOCHS",
    fontsize=20,
    fontweight='bold'
)
ax1.set_ylabel(
    "ACCURACY",
    fontsize=20,
    fontweight='bold'
)
ax1.plot(
    history.history['accuracy'],
    label='train accuracy'
)
ax1.plot(
    history.history['val_accuracy'],
    label='validation accuracy'
)

ax1.legend(loc='best')

ax2 = history_plot.add_subplot(212)
ax2.set_xlabel(
    "EPOCHS",
    fontsize=20,
    fontweight='bold'
)
ax2.set_ylabel(
    "LOSS",
    fontsize=20,
    fontweight='bold'
)
ax2.plot(
    history.history['loss'],
    label='train loss'
)
ax2.plot(
    history.history['val_loss'],
    label='validation loss'
)
ax2.legend(loc='best')

plt.show()



import numpy as np


y_pred = model.predict(x_test)


y_test_class = np.argmax(y_test, axis=1)

y_pred_class = np.argmax(y_pred, axis=1)

from sklearn.metrics import classification_report, confusion_matrix

print('\n Confusion matrix \n\n',
      confusion_matrix(y_test_class, y_pred_class))

print('\n Classification report \n\n',
      classification_report(y_test_class, y_pred_class))

test_loss, test_acc = model.evaluate(x_test, y_test)
print('\nAccuracy:', test_acc)
print('\nLoss: ', test_loss)
