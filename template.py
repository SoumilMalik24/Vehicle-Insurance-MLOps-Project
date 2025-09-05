import os
from pathlib import Path

project_name = "src"

list_of_files = [

    f"{project_name}/__init__.py",
    f"{project_name}/comoponents/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py",
    f"{project_name}/configuration/aws_connection.py",
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/aws_storage.py",
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/proj1_data.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/estimator.py",
    f"{project_name}/entity/s3_estimator.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.py",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml",
    
]

for file in list_of_files:
    file = Path(file) #Converts the string to a pathlib.Path object

    #Splits path into directory part (head) and final component (tail)
    filedir,filename = os.path.split(file)

    #Checks if there’s a directory component
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)

    #If the file doesn’t exist, or exists but is empty (size 0), then create/truncate it
    if (not os.path.exists(file)) or (os.path.getsize(file)==0):
        with open (file,"w") as f:
            pass

    else:
        print(f"the file is already at:{file}")