"""Script to create a jwt token."""
import jwt
import yaml

try:
    with open('config.yml') as file:
        env = yaml.load(file, Loader=yaml.FullLoader)
except FileNotFoundError:
    print("Error: make sure you run it in the root directory: `python3 bin/generate_token.py`, and that the config.yml file exists.")
else:
    print(jwt.encode({'github': 'DrBluefall'}, env.get('jwt_secret')))
