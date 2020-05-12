"""Set up local enviroment."""
import yaml

try:
    with open('config.yml') as file:
        env = yaml.load(file, Loader=yaml.FullLoader)

except FileNotFoundError:
    env = {}
