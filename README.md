# Kaggle-dogs-and-cats (No transfer learning!)

Dogs vs Cats classification for kaggle competition. (95.5% accuracy on validation set)

## Training

Model was trained on cleaned "kaggle cats vs dogs" dataset with simple convolution model.

## Results

Most wrong predicted examples is a little tricky. For example an upside down cat is very rare in dataset. Also the background of dog's images is often green (garden etc.), this may be the reason why some cats was recognized as dogs. Other examples are just difficult (The white dog on a red background has cat-like features)

## Conclusions


After many attempts on this dataset (using only the simplest conv architectures), the conclusions are as follows:

- MaxPooling2D is much better instead of stride=2 in conv layers (3-5% higher acc)
- Dropout with batch normalization after conv layers gives spectacular regularization effects (5-7% higher acc), contrary to what is commonly believed that dropout after covolution is bad.
- Doubling the number of parameters doesn't improove performence much.





