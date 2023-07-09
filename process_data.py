import os, glob

orange_train_directory = "Dataset1/dataset/train/*/*"
orange_test_directory = "Dataset1/dataset/test/*/*"

apple_train_directory = "Dataset2/apple_disease_classification/Train/*/*"
apple_test_directory = "Dataset2/apple_disease_classification/Test/*/*"

print(len(glob.glob(orange_train_directory)))
print(len(glob.glob(orange_test_directory)))


print(len(glob.glob(apple_train_directory)))
print(len(glob.glob(apple_test_directory)))


