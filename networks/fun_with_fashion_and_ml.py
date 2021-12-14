import matplotlib
matplotlib.use("TkAgg")

import tensorflow as tf
physical_devices = tf.config.list_physical_devices('GPU')
try:
  tf.config.experimental.set_memory_growth(physical_devices[0], True)
except:
    print("No device")

from tensorflow.keras.datasets import fashion_mnist

(train_images, y_train), (test_images, y_test) = \
    fashion_mnist.load_data()
# %%
"""
Analyze MNIST dataset
"""

import matplotlib.pyplot as plt

# number of digits to plot
n_immagini = 10

# Init plot
window, ax = plt.subplots(
    1,  # n rows
    n_immagini,  # n col
    figsize=(10, 10)  # window size
)

# plot hand written digits
for i in range(n_immagini):
    ax[i].axis('off')  # toogle axis to each subplot
    ax[i].imshow(  # plot image
        train_images[i],  # input image
        cmap=plt.cm.binary  # color map
    )


plt.figtext(
    .45,
    .30,
    y_train[0:n_immagini],
    style='italic',
    bbox={'facecolor': 'yellow'},
    fontsize='xx-large',
    fontweight='bold',
)


"""
Rescale dataset to range(0,1)
"""
train_images = train_images.reshape((60000, 28*28))
x_train = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28*28))
x_test = test_images.astype('float32') / 255
# %%
from sklearn.tree import DecisionTreeClassifier
dec_tree_clf = DecisionTreeClassifier(max_depth=50, random_state=42)
dec_tree_clf.fit(x_train, y_train)

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import f1_score

y_train_predict = dec_tree_clf.predict(x_train)
dec_tree_accuracy = accuracy_score(y_train, y_train_predict)
dec_tree_precision = precision_score(y_train, y_train_predict, average='weighted')
dec_tree_recall = recall_score(y_train, y_train_predict, average='weighted')
dec_tree_f1_score = f1_score(y_train, y_train_predict, average='weighted')


print("Decision Tree Accuracy: ", dec_tree_accuracy)
print("Decision Tree Precision: ", dec_tree_precision)
print("Decision Tree Recall: ", dec_tree_precision)
print("Decision Tree F1 Score: ", dec_tree_f1_score)

################

from sklearn.linear_model import SGDClassifier
sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(x_train, y_train)

y_train_predict = sgd_clf.predict(x_train)
sgd_accuracy = accuracy_score(y_train, y_train_predict)
sgd_precision = precision_score(y_train, y_train_predict, average='weighted')
sgd_recall = recall_score(y_train, y_train_predict, average='weighted')
sgd_f1_score = f1_score(y_train, y_train_predict, average='weighted')


print("SGD Accuracy: ", sgd_accuracy)
print("SGD Precision: ", sgd_precision)
print("SGD Recall: ", sgd_precision)
print("SGD F1 Score: ", sgd_f1_score)

#################

from sklearn.ensemble import RandomForestClassifier
rnd_clf = RandomForestClassifier(n_estimators=100, max_depth=50, random_state=42)
rnd_clf.fit(x_train, y_train)
y_train_predict = rnd_clf.predict(x_train)
rnd_accuracy = accuracy_score(y_train, y_train_predict)
rnd_precision = precision_score(y_train, y_train_predict, average='weighted')
rnd_recall = recall_score(y_train, y_train_predict, average='weighted')
rnd_f1_score = f1_score(y_train, y_train_predict, average='weighted')


print("Random Forest Accuracy: ", rnd_accuracy)
print("Random Forest Precision: ", rnd_precision)
print("Random Forest Recall: ", rnd_precision)
print("Random Forest F1 Score: ", rnd_f1_score)