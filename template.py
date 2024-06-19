import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)
project_name = "mlproject"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/data_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

# Use a raw string or forward slashes
project_path = Path(r"C:\Users\Bhavna\Desktop\data_sci\project")

for filepath in list_of_files:
    # Combine project path with filepath
    full_path = project_path / filepath
    filedir, filename = os.path.split(full_path)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(full_path)) or (os.path.getsize(full_path) == 0):
        with open(full_path, 'w') as f:
            pass
        logging.info(f"Creating empty file: {full_path}")
    else:
        logging.info(f"{filename} already exists")
