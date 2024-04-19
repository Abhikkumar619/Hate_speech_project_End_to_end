from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s : %(message)s]')

project_name="Hate_speech"

list_of_file=[
    f'{project_name}/components/__init__.py',
    f'{project_name}/components/data_ingestion.py',
    f'{project_name}/components/data_transformation.py',
    f'{project_name}/components/model_trainer.py',
    f'{project_name}/components/model_evaluation.py',
    f'{project_name}/components/model_pusher.py',
    f'{project_name}/configuration/__init__.py',
    f'{project_name}/configuration/gcloude_syncer.py',
    f'{project_name}/constants/__init__.py',
    f'{project_name}/entity/__init__.py',
    f'{project_name}/entity/config_entity.py',
    f'{project_name}/entity/artifacts_entity.py',
    f'{project_name}/exception/__init__.py',
    f'{project_name}/logger/__init__.py',
    f"{project_name}/pipeline/__init__.py",
    f'{project_name}/pipeline/train_pipeline.py',
    f'{project_name}/pipeline/predication_pipeline.py',
    f"{project_name}/ml/__init__.py",
    f"{project_name}/ml/model.py",
    "app.py",
    "demo.py",
    "requirement.txt",
    "Dockerfile",
    "setup.py",
    ".dockerignore",

]

for file in list_of_file: 
    file_path=Path(file)
    file_dir, file_name=os.path.split(file_path)
    # logging.info(f"file directory: {file_dir}, file name: {file_name}")

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"file directory is created: {file_dir} for file {file_name}")

    if (not os.path.exists(file)) or (os.path.getsize(file)==0):
        with open(file, 'w') as f:
            pass
            logging.info(f"file is created: {file}")

    else:
        logging.info("file is already created: {file}")






    

    