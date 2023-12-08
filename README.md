# GeoVision

GeoVision is an image classification project designed to identify and categorize different geographical locations based on visual cues. Leveraging state-of-the-art machine learning models, the system is trained to recognize various scenes such as buildings, forests, glaciers, mountains, seas, and streets.

## File Structure ->

```.
├── Image_Location_Generator.ipynb # Main Jupyter Notebook              
├── models # Trained Model Files 
│   ├── Image_Location_Generator.h5  # Main Inference Model
├── Cloudbuild.yaml # Google Cloud Build Configuration
├── Deployment.yaml # Kubernetes Deployment Configuration
├── service.yaml # Kubernetes Service Configuration
├── ui.py # Streamlit Frontend Script
└── README.md
```


## Dataset

The dataset used for training and evaluating the model can be obtained from [Intel Image Classification on Kaggle](https://www.kaggle.com/puneet6060/intel-image-classification).

### Dataset Specifications:

This dataset consists of approximately 25,000 images, each of size 150x150 pixels, distributed across six categories:

- 'buildings' (Category 0)
- 'forest' (Category 1)
- 'glacier' (Category 2)
- 'mountain' (Category 3)
- 'sea' (Category 4)
- 'street' (Category 5)

The dataset is partitioned into Train, Test, and Prediction data, each stored in separate zip files. The distribution is as follows:

- Train Data: Around 14,000 images
- Test Data: Approximately 3,000 images
- Prediction Data: About 7,000 images


## Key Features

### Location Classification
Simply provide an image URL, and SightSpotter will promptly predict the geographical location, offering insights into the scene depicted in the image.

### Streamlit UI
SightSpotter has a user-friendly Streamlit-based interface, ensuring seamless interaction. Users can input image URLs and receive predictions about the location captured in the image.

### TensorFlow Model
The core machine learning model is constructed using TensorFlow, owing to its accuracy and robust performance in location classification tasks.

## MLops Integration:
SightSpotter goes beyond simple image classification by incorporating robust MLops practices, streamlining the deployment and orchestration processes.

### Docker Containerization:
The project embraces Docker for containerization, encapsulating the application, dependencies, and the TensorFlow model into a lightweight and portable container. The Dockerfile specifies the environment and dependencies needed to run the application, promoting consistency across different environments.

### Kubernetes Orchestration
SightSpotter embraces Kubernetes for container orchestration, providing scalability and reliability. The deployment configuration (Deployment.yaml) specifies the desired state for running the application, while the service configuration (service.yaml) defines the network access to the deployed application.

### Cloud Build Integration
Google Cloud Build automates the build and deployment process. The cloudbuild.yaml file defines the build steps, pushing the Docker image to Google Container Registry and deploying the application to Kubernetes.
