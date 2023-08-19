# Bird_Disease_Classification

![app](https://github.com/weedu34/Bird_Disease_Classification/blob/main/App.png)
Welcome to the Bird Disease Classification Application repository! This application is designed to classify bird diseases using images of bird fecal samples. It utilizes a Keras VGG16 model as the base architecture to achieve accurate disease identification.

## Introduction

Bird diseases pose a significant challenge for avian researchers and conservationists. This application aims to simplify the process of identifying bird diseases by automating the classification using AI and image analysis techniques.

## Application Overview

This application follows a data pipeline that downloads bird fecal sample images from GitHub and then utilizes a pre-trained Keras VGG16 model for disease classification. The application offers an end-to-end solution for bird disease identification.

## Dataset

Link to the data set is here [Data Set](https://github.com/entbappy/Branching-tutorial/raw/master/Chicken-fecal-images.zip)

## WorkFlow
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml


## Model Architecture

The core of this application is a Keras VGG16 model, which has proven to be effective in image classification tasks. The model's architecture is optimized for capturing intricate features in the images.

## Training

The model is trained on the training dataset using a specific set of hyperparameters, including the optimizer and loss function. Data augmentation techniques are applied to enhance the model's generalization capabilities.

## Evaluation

The model's performance is evaluated using the validation dataset. The accuracy matrix is calculated to assess the model's ability to classify bird diseases accurately.

## App
There are three buttons named **Upload** used for uploading the test image, **Predict** used for predicting the test image, an the last button named **Training model** is used for processing the whole pipeline starting from the data ingestion till validating the model.

Thank you BAPPY AHMED entbappy for tutorials.
