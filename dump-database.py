import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

if __name__ == '__main__':
    print("Starting backup...")
    username = os.getenv('LOCAL_DB_USER')
    password = os.getenv('LOCAL_DB_PASSWORD')
    database_name = os.getenv('LOCAL_DB_NAME')
    database_url = os.getenv("LOCAL_DB_URL")
    output_path = os.getenv('OUTPUT_PATH')

    time_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    os.system(f'cmd /k mongodump mongodb://{username}:{password}@{database_url}/{database_name} --authenticationDatabase admin --gzip --archive > dump/dump_{time_now}.gz')
    print("Backup completed!")
    exit()
