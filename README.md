 Soybean Seed Classification using CNN

 Overview
This project focuses on classifying soybean seeds into Good or Bad categories using a Convolutional Neural Network (CNN).

The pipeline includes:
- Image Labeling Script (`labaling.py`) → Prepares and labels seed images.
- CNN Training Script (`cnn_training.py`) → Trains a binary classification model on labeled images.
- Dataset → 10,000 soybean seed images (5,000 Good + 5,000 Bad).

The trained CNN achieves **~93% accuracy** with an 80/20 train-test split.

---
- **Requirements**
tensorflow
opencv-python
pillow
pillow-heif
matplotlib
numpy


