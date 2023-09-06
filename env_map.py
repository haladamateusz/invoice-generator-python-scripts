import os

env_map = {
    'local': 'LOCAL',
    'dev':  'DEV_CLOUD',
    'prod': 'PROD_CLOUD'
}


def get_env_data(value):
    return {
        'username': os.getenv(f'{env_map[value]}_DB_USER'),
        'password': os.getenv(f'{env_map[value]}_DB_PASSWORD'),
        'database_name': os.getenv(f'{env_map[value]}_DB_NAME'),
        'database_url': os.getenv(f'{env_map[value]}_DB_URL'),

    }
