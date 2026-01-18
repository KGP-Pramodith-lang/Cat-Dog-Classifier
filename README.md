# Cat-Dog-Classifier

A deep learning-based image classifier that distinguishes between cats and dogs using a Convolutional Neural Network (CNN) with a user-friendly GUI interface.

## Dataset

The dataset used for this project can be found on Kaggle:
[Cats and Dogs for Classification](https://www.kaggle.com/datasets/dineshpiyasamara/cats-and-dogs-for-classification)

## Model Architecture

This project uses a Convolutional Neural Network (CNN) built with TensorFlow/Keras to classify images as either cats or dogs. The model architecture consists of:

### Data Augmentation Layer

- **RandomFlip**: Horizontal flipping to increase data variability
- **RandomRotation**: 20% rotation to improve model robustness
- **RandomZoom**: 20% zoom for better generalization

### Convolutional Layers

1. **Conv2D Layer 1**: 32 filters with 3x3 kernel and ReLU activation
   - MaxPooling2D for spatial dimension reduction
2. **Conv2D Layer 2**: 64 filters with 3x3 kernel and ReLU activation
   - MaxPooling2D for further feature extraction
3. **Conv2D Layer 3**: 128 filters with 3x3 kernel and ReLU activation
   - MaxPooling2D for deep feature learning

### Regularization

- **Dropout**: 0.2 dropout rate to prevent overfitting
- **BatchNormalization**: For stable and faster training

### Dense Layers

- **Flatten Layer**: Converts 2D feature maps to 1D vector
- **Dense Layer 1**: 128 neurons with ReLU activation
- **Dense Layer 2**: 128 neurons with ReLU activation
- **Dense Layer 3**: 32 neurons with ReLU activation
- **Output Layer**: 1 neuron with sigmoid activation for binary classification

### Model Configuration

- **Input Size**: 128x128 RGB images
- **Optimizer**: Adam optimizer
- **Loss Function**: Binary Focal Crossentropy (handles class imbalance)
- **Metrics**: Accuracy
- **Training**: 20 epochs with 90-10 train-validation split
- **Batch Size**: 32

### Data Preprocessing

- Images are normalized by dividing pixel values by 255 (scaling to 0-1 range)
- Train-validation split: 90% training, 10% validation

## Features

- Binary classification (Cat vs Dog)
- GUI application built with CustomTkinter
- Real-time image prediction with confidence scores
- Pre-trained model saved as `cnn_model.keras`
- Image preprocessing and normalization
