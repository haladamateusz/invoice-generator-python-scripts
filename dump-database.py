import os
from dotenv import load_dotenv
from datetime import datetime
import sys
from env_map import get_env_data

load_dotenv()

if __name__ == '__main__':
    environment = sys.argv[1]  # prod, dev or local
    print("Starting backup...")
    env_data = get_env_data(environment)

    # if 'gzip' == dump_type:
    time_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    if 'local' == environment:
        os.system(f'cmd /c mongodump mongodb://{env_data["username"]}:{env_data["password"]}@{env_data["database_url"]}/{env_data["database_name"]} --authenticationDatabase=admin --gzip --archive=dump_{time_now}.gz')
    if 'dev' == environment or 'prod' == environment:
        os.system(f'cmd /c mongodump mongodb+srv://{env_data["username"]}:{env_data["password"]}@{env_data["database_url"]}/{env_data["database_name"]} --authenticationDatabase=admin --gzip --archive=dump_{time_now}.gz')
    # if 'bson' == dump_type:
    # os.system(f' cmd /c mongodump mongodb://{username}:{password}@{database_url}/{database_name}
    # --authenticationDatabase admin')
    print("Backup completed!")
    exit()
