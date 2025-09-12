# Vehicle Data MLOps Project  

## Overview  
This project implements a complete end-to-end **Machine Learning Operations (MLOps) pipeline** for vehicle-related data. The pipeline covers all essential components, from environment setup, data ingestion, data validation, feature engineering, and model training, to deployment using **AWS, Docker, GitHub Actions, and MongoDB Atlas**.  

The goal is to provide a scalable, production-ready architecture for managing datasets, training ML models, evaluating them, and deploying predictions through an API-based application.  

---

## Project Workflow  

### 1. Environment Setup  
1. Generate the initial project structure using `template.py`.  
2. Configure `setup.py` and `pyproject.toml` for managing local packages.  
3. Create a virtual environment using Conda:  
   conda create -n vehicle python=3.10 -y  
   conda activate vehicle  
   pip install -r requirements.txt  
4. Verify installed packages with `pip list`.  

---

### 2. MongoDB Setup  
1. Create a **MongoDB Atlas** account and project.  
2. Deploy a free-tier **M0 cluster**.  
3. Configure database user credentials.  
4. Set network access with IP `0.0.0.0/0`.  
5. Obtain the Python connection string.  
6. Create a `notebook/mongoDB_demo.ipynb` file to push and query datasets.  
7. Verify dataset insertion in the MongoDB Atlas collections.  

---

### 3. Logging, Exception Handling, and Notebooks  
1. Implement a centralized logging utility and test with `demo.py`.  
2. Implement custom exception handling and test with `demo.py`.  
3. Perform **Exploratory Data Analysis (EDA)** and **Feature Engineering** in notebooks.  

---

### 4. Data Ingestion  
1. Define constants in `constants/__init__.py`.  
2. Configure database connections in `configuration/mongo_db_connections.py`.  
3. Implement data access in `data_access/proj1_data.py`.  
4. Define ingestion configuration and artifacts in:  
   - `entity/config_entity.py`  
   - `entity/artifact_entity.py`  
5. Implement ingestion logic in `components/data_ingestion.py`.  
6. Add ingestion to the **training pipeline** and execute via `demo.py`.  
7. Set MongoDB URL in environment variables for local and cloud execution.  

---

### 5. Data Validation, Transformation, and Model Training  
1. Define dataset schema in `config/schema.yaml`.  
2. Implement validation utilities in `utils/main_utils.py`.  
3. Build **Data Validation** component.  
4. Build **Data Transformation** component, including feature engineering and estimator logic (`entity/estimator.py`).  
5. Build **Model Trainer** component to train and store models.  

---

### 6. AWS Setup for Model Storage  
1. Configure IAM user with **AdministratorAccess**.  
2. Set AWS credentials as environment variables.  
3. Define AWS constants in `constants/__init__.py`.  
4. Implement AWS connection utilities in `src/configuration/aws_connection.py`.  
5. Create an **S3 bucket** (`my-model-mlopsproj`) to store models.  
6. Implement logic in `src/aws_storage` and `entity/s3_estimator.py` for pushing and pulling models from S3.  

---

### 7. Model Evaluation and Model Pusher  
1. Implement **Model Evaluation** to compare trained models against thresholds.  
2. Implement **Model Pusher** to save and push the best model to S3.  

---

### 8. Prediction Pipeline and Application Setup  
1. Create a **prediction pipeline** for inference.  
2. Develop `app.py` as the Flask-based web application.  
3. Add `static` and `templates` directories for serving the application.  

---

### 9. CI/CD Setup with GitHub Actions and Docker  
1. Create a `Dockerfile` and `.dockerignore`.  
2. Configure GitHub Actions workflow (`.github/workflows/aws.yaml`).  
3. Setup a new IAM user (`usvisa-user`) with appropriate access.  
4. Create an **ECR repository** (`vehicleproj`) to store Docker images.  
5. Launch an **EC2 instance** (`vehicledata-machine`) with Ubuntu, t2.medium, and storage (30GB).  
6. Install Docker on EC2.  
7. Configure GitHub self-hosted runner on EC2.  
8. Setup GitHub secrets:  
   - `AWS_ACCESS_KEY_ID`  
   - `AWS_SECRET_ACCESS_KEY`  
   - `AWS_DEFAULT_REGION`  
   - `ECR_REPO`  

---

### 10. Deployment  
1. CI/CD pipeline is triggered on every commit push.  
2. Open EC2 security group inbound rules and allow access to custom port (5080).  
3. Access the application at:  
   http://<EC2_PUBLIC_IP>:5080  
4. Train models via `/training` route if required.  

---

## Key Features  
- Automated data ingestion from MongoDB Atlas.  
- Centralized logging and custom exception handling.  
- Modular pipeline with reusable components for ingestion, validation, transformation, and training.  
- Model storage and versioning using AWS S3.  
- Continuous Integration and Deployment (CI/CD) using GitHub Actions, Docker, and AWS EC2.  
- Flask-based web interface for predictions.  

---

## Tech Stack  
- **Programming Language**: Python 3.10  
- **Database**: MongoDB Atlas  
- **Cloud**: AWS (S3, EC2, ECR, IAM)  
- **Containerization**: Docker  
- **Orchestration**: GitHub Actions (CI/CD)  
- **Framework**: Flask  
- **Libraries**: Pandas, Numpy, Scikit-learn, PyMongo, Boto3  

---

## Project Structure  
├── constants/<br>
├── configuration/<br>
├── data_access/<br>
├── entity/<br>
├── components/<br>
├── utils/<br>
├── src/<br>
│   ├── configuration/<br>
│   ├── aws_storage/<br>
├── notebook/<br>
├── static/<br>
├── templates/<br>
├── app.py<br>
├── demo.py<br>
├── setup.py<br>
├── pyproject.toml<br>
├── requirements.txt<br>
├── Dockerfile<br>
└── .github/workflows/aws.yaml<br>


---

## How to Run  
1. Clone the repository.
```
git clone <repo link>
```  
2. Create and activate the virtual environment.
```
python -m venv .veh_env
```  
3. Install dependencies:
```  
pip install -r requirements.txt  
```
4. Set environment variables (MongoDB, AWS).
```
$env:ENV_NAME=""
```  
5. Run the training pipeline:  
```
python demo.py  
```
6. Launch the Flask app:  
```
python app.py  
```
7. Access the application via browser.  
