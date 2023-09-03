import os
from dotenv import load_dotenv
import pymongo
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
    print(environment)
    print("Starting restore operation...")
    username = os.getenv(f'{env_map[environment]}_DB_USER')
    password = os.getenv(f'{env_map[environment]}_DB_PASSWORD')
    database_name = os.getenv(f'{env_map[environment]}_DB_NAME')
    database_url = os.getenv(f'{env_map[environment]}_DB_URL')
    output_path = os.getenv('OUTPUT_PATH')
    uri = None
    client = None

    if 'local' == environment:
        #client = pymongo.MongoClient(f"mongodb://{username}:{password}@{database_url}/")
        uri = f"mongodb://{username}:{password}@{database_url}/"
    if 'dev' == environment or 'prod' == environment:
        uri = f"mongodb+srv://{username}:{password}@{database_url}/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(f'mongodb+srv://{username}:{password}@{database_url}/')
    #if database_name in client.list_database_names():
    #    print(f'Dropping existing database {database_name}...')
    #    client.drop_database(database_name)
    # --authenticationDatabase admin

    print(client.list_database_names())
    print(database_name)

    os.system(f'cmd /k mongorestore --drop {uri} --db dev-invoice-generator --gzip --archive=dump_2023-09-03_23-21-26.gz')
    print("Restore completed!")
    exit()
