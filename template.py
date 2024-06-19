import os  # Importing the os module to interact with the operating system
from pathlib import Path  # Importing Path from pathlib module for easier path manipulations
import logging  # Importing logging module to log messages

# Setting up the logging configuration to display messages of level INFO and above
logging.basicConfig(level=logging.INFO)

# Defining the project name, which will be used in the file paths
project_name = "mlproject"

# List of files to create within the project, using the project name in the paths
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

# Define the base path of the project directory
project_path = Path(r"C:\Users\Bhavna\Desktop\data_sci\project")

# Loop through each file path in the list of files
for filepath in list_of_files:
    # Construct the full path by combining the project base path with the relative file path
    full_path = project_path / filepath
    
    # Split the full path into directory and file name
    filedir, filename = os.path.split(full_path)

    # Check if there is a directory part in the path
    if filedir != "":
        # Create the directory (and any necessary parent directories) if it doesn't exist
        os.makedirs(filedir, exist_ok=True)
        # Log the directory creation action
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Check if the file doesn't exist or if it exists but is empty
    if (not os.path.exists(full_path)) or (os.path.getsize(full_path) == 0):
        # Open the file in write mode, creating it if it doesn't exist
        with open(full_path, 'w') as f:
            pass  # We only need to create the file, so we don't write anything to it
        # Log the file creation action
        logging.info(f"Creating empty file: {full_path}")
    else:
        # Log that the file already exists
        logging.info(f"{filename} already exists")
