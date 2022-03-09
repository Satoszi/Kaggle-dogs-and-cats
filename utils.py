import os
import cv2
import numpy as np

def create_set(dataset_path,IMG_SIZE):
    x_train = [] 
    y_train = []
    cats_path = dataset_path + "\\cats"
    dogs_path = dataset_path + "\\dogs"
    for label, class_path in enumerate([cats_path,dogs_path]):
        for img_path in os.listdir(class_path):
            try:
                img_path = os.path.join(class_path,img_path)
                img = cv2.resize(cv2.imread(img_path), (IMG_SIZE,IMG_SIZE))
                x_train.append(img)
                y_train.append(label)
            except: None
    x_train = np.array(x_train, dtype = np.float16)/255.0 #normalization to 0 - 1
    y_train = np.array(y_train)
    shuffler = np.random.permutation(len(x_train)) #Shuffle data
    x_train = x_train[shuffler]
    y_train = y_train[shuffler]
    return x_train, y_train