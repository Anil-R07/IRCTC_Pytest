import yaml
import os

class ConfigReader:
    def __init__(self):
        with open("config/config.yaml") as f:
            self.data = yaml.safe_load(f)

        #Env Override
        self.env = os.getenv("ENV", self.data["env"])

    def get(self, key):
        return self.data[self.env][key]
config = ConfigReader ()