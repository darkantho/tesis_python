import os, glob
import tensorflow as tf
import cv2

apple_train_directory = "apple/Train/*/*"
apple_test_directory = "apple/Test/*/*"


Train_list = glob.glob(apple_train_directory)
Test_list = glob.glob(apple_test_directory)


# for path in Train_list:

#     newpath = 'apple_dataset/' + '/'.join(path.split('/')[1:])
    
#     image = cv2.imread(path)
#     image = tf.image.resize(image,(800,800))
#     image = image.numpy()
#     cv2.imwrite(newpath,image)


# for path in Test_list:

#     newpath = 'apple_dataset/' + '/'.join(path.split('/')[1:])
    
#     image = cv2.imread(path)
#     image = tf.image.resize(image,(800,800))
#     image = image.numpy()
#     cv2.imwrite(newpath,image)

