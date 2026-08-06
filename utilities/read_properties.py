import os
import configparser

config = configparser.RawConfigParser()

config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
"configuration",
"config.ini"
)

config.read(config_path)


class ReadConfigProperties:

    @staticmethod
    def get_url():
       url =  config.get("config info", "url")
       return url


    @staticmethod
    def get_username():
        username =  config.get("config info", "username")
        return username


    @staticmethod
    def get_password():
        password =  config.get("config info", "password")
        return password