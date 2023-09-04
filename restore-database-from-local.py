import os
from dotenv import load_dotenv
import sys

load_dotenv()

env_map = {
    'local': 'LOCAL',
    'dev':  'DEV_CLOUD',
    'prod': 'PROD_CLOUD'
}

# run this script with the environment as the first argument e.g. python restore-database-from-local.py local/dev/prod
if __name__ == '__main__':
    environment = sys.argv[1]
    print("Starting restore operation...")
    username = os.getenv(f'{env_map[environment]}_DB_USER')
    password = os.getenv(f'{env_map[environment]}_DB_PASSWORD')
    database_name = os.getenv(f'{env_map[environment]}_DB_NAME')
    database_url = os.getenv(f'{env_map[environment]}_DB_URL')
    output_path = os.getenv('OUTPUT_PATH')
    uri = None

    if 'local' == environment:
        uri = f"mongodb://{username}:{password}@{database_url}/"
    if 'dev' == environment or 'prod' == environment:
        uri = f"mongodb+srv://{username}:{password}@{database_url}/?retryWrites=true&w=majority"

    os.system(f'cmd /c mongorestore --verbose --drop --uri="{uri}" --nsFrom="invoice-generator.*" --nsTo="{database_name}.*" --gzip --archive="dump/dump_2023-09-04_11-12-32.gz"')

    print("Restore completed!")

# cool one liner for later usage
# mongodump --archive --gzip --db=someDistantDB |
# mongorestore --archive --gzip  --nsFrom='someLocalDB.*' --nsTo='someLocalDB.*'