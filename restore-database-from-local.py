import os
from dotenv import load_dotenv
import sys
from env_map import get_env_data

load_dotenv()


# run this script with the environment as the first argument e.g. python restore-database-from-local.py local/dev/prod
if __name__ == '__main__':
    environment = sys.argv[1]

    # pass proper value according to the database you want to restore from:
    # local: invoice-generator
    # dev: dev-invoice-generator
    # prod: prod-invoice-generator

    from_db_name = sys.argv[2]

    print("Starting restore operation...")
    env_data = get_env_data(environment)
    uri = None

    if 'local' == environment:
        uri = f'mongodb://{env_data["username"]}:{env_data["password"]}@{env_data["database_url"]}/'
    if 'dev' == environment or 'prod' == environment:
        uri = f'mongodb+srv://{env_data["username"]}:{env_data["password"]}@{env_data["database_url"]}/?retryWrites=true&w=majority'

    print(env_data["database_name"])
    gzip_file = list(filter(lambda x: x.endswith('.gz'), os.listdir('./')))[0]
    os.system(f'cmd /c mongorestore --verbose --drop --uri="{uri}" --nsFrom="{from_db_name}.*" --nsTo="{env_data["database_name"]}.*" --gzip --archive="{gzip_file}"')
    # os.system(f' cmd /c mongodump mongodb://{username}:{password}@localhost:27017/{database_name}
    # --authenticationDatabaseadmin --gzip --archive="dump_{time_now}.gz" | mongorestore --verbose --drop
    # --uri="{uri}" --nsFrom="invoice-generator.*" --nsTo="{database_name}.*" --gzip --archive="dump_{time_now}.gz"')

    print("Restore completed!")

# cool one-liner for later usage
# mongodump --archive --gzip --db=someDistantDB |
# mongorestore --archive --gzip  --nsFrom='someLocalDB.*' --nsTo='someLocalDB.*'
