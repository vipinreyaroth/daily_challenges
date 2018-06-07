import os
from dotenv import load_dotenv
from dotenv import find_dotenv

load_dotenv(find_dotenv())

print('Printing username and api key from environment')

if os.environ.get('COOL_USER_NAME'):
    print(os.environ.get('COOL_USER_NAME'))

if os.environ.get('COOL_API_KEY'):
    print(os.environ.get('COOL_API_KEY'))
