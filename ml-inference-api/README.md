*Simple ML Inference API*

This repository contains a simple ML inference API built using FastAPI. The API serves a pre-trained Iris classification model and provides an endpoint for making predictions based on input features.
## Features
- FastAPI framework for building the API.  
- Pydantic models for request and response validation.
- Pre-trained Iris classification model using scikit-learn.
- Single endpoint for making predictions.
## Installation
1. Clone the repository:
   ```bash
    git clone https://github.com/your-username/ml-inference-api.git  
    cd ml-inference-api
    ```
2. Create a virtual environment and activate it:
   ```bash
    python -m venv venv  
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install the required packages:
   ```bash
    pip install -r requirements.txt
    ```
## Usage
1. Start the FastAPI server:
   ```bash
    uvicorn app.main:app --reload
    ```
2. Access the API documentation at `http://localhost:8000/docs`.
3. Use the `/predict` endpoint to make predictions by sending a POST request with the required features in the request body.
## Example Request
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```
## Example Response
```json
{
  "prediction": 1,
  "probabilities": 0.08,
  "model_version": "1.0.0"
}

**This is very simple ML inference API for practicing deployment of ML models using FastAPI and architecting the project structure.**