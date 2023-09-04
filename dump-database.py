import os
from dotenv import load_dotenv
from datetime import datetime
import sys

load_dotenv()

if __name__ == '__main__':
    dump_type = sys.argv[1] # gzip or bson
    print("Starting backup...")
    username = os.getenv('LOCAL_DB_USER')
    password = os.getenv('LOCAL_DB_PASSWORD')
    database_name = os.getenv('LOCAL_DB_NAME')
    database_url = os.getenv("LOCAL_DB_URL")
    output_path = os.getenv('OUTPUT_PATH')

    if 'gzip' == dump_type:
        time_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        os.system(f'cmd /c mongodump mongodb://{username}:{password}@{database_url}/{database_name} --authenticationDatabase admin --gzip --archive > dump/dump_{time_now}.gz')
    if 'bson' == dump_type:
        os.system(f'cmd /c mongodump mongodb://{username}:{password}@{database_url}/{database_name} --authenticationDatabase admin')
    print("Backup completed!")
    exit()
