import os
import json
from dotenv import load_dotenv

load_dotenv()


with open(os.path.join(os.environ.get('CONFIG_PATH'), os.environ.get('CONFIG_FILE_NAME'))) as env_file:
    env_dict = json.load(env_file)



class ConfigBasic():

    def __init__(self):
        self.SECRET_KEY = env_dict.get('SECRET_KEY')
        self.DB_LOCAL_ROOT = os.environ.get('DB_LOCAL_ROOT')
        self.DB_DEV_ROOT = os.environ.get('DB_DEV_ROOT')
        self.DB_PROD_ROOT = os.environ.get('DB_PROD_ROOT')
        

        #Email stuff
        self.MAIL_SERVER = env_dict.get('MAIL_SERVER_MSOFFICE')
        self.MAIL_PORT = env_dict.get('MAIL_PORT')
        self.MAIL_USE_TLS = True
        self.MAIL_USERNAME = env_dict.get('MAIL_EMAIL')
        self.MAIL_PASSWORD = env_dict.get('MAIL_PASSWORD')


        #web Guest
        self.GUEST_EMAIL = env_dict.get('GUEST_EMAIL')
        self.GUEST_PASSWORD = env_dict.get('GUEST_PASSWORD')

        #API
        self.API_URL = os.environ.get("API_URL")

        #Admin stuff
        self.ADMIN_EMAILS = env_dict.get('ADMIN_EMAILS')
        self.REGISTRATION_KEY =env_dict.get('REGISTRATION_KEY')
        self.BLS_API_URL = env_dict.get('BLS_API_URL')

        #Captcha
        self.SITE_KEY_CAPTCHA = env_dict.get('SITE_KEY_CAPTCHA')
        self.SECRET_KEY_CAPTCHA = env_dict.get('SECRET_KEY_CAPTCHA')
        self.VERIFY_URL_CAPTCHA = 'https://www.google.com/recaptcha/api/siteverify'

        # # Database
        # self.SQL_URI_USERS = f"sqlite:///{self.DB_ROOT}{os.environ.get('DB_NAME_USERS')}"
        # self.SQL_URI_CAGE = f"sqlite:///{self.DB_ROOT}{os.environ.get('DB_NAME_CAGE')}"
        # self.SQL_URI_BLS = f"sqlite:///{self.DB_ROOT}{os.environ.get('DB_NAME_BLS')}"
        
        # # # other directories
        # self.DIR_DB_AUXILARY = os.path.join(self.DB_ROOT,"auxilary")
        # self.DIR_DB_AUX_IMAGES_PEOPLE = os.path.join(self.DIR_DB_AUXILARY,"images_people")


class ConfigLocal(ConfigBasic):
    
    def __init__(self):
        super().__init__()
        # Database
        self.DB_ROOT = self.DB_LOCAL_ROOT
        self.SQL_URI_USERS = f"sqlite:///{self.DB_LOCAL_ROOT}{os.environ.get('DB_NAME_USERS')}"
        self.SQL_URI_CAGE = f"sqlite:///{self.DB_LOCAL_ROOT}{os.environ.get('DB_NAME_CAGE')}"
        self.SQL_URI_BLS = f"sqlite:///{self.DB_LOCAL_ROOT}{os.environ.get('DB_NAME_BLS')}"
        # # other directories
        self.DIR_DB_AUXILARY = os.path.join(self.DB_LOCAL_ROOT,"auxilary")
        self.DIR_DB_AUX_IMAGES_PEOPLE = os.path.join(self.DIR_DB_AUXILARY,"images_people")

    DEBUG = True
    # TEMPLATES_AUTO_RELOAD = False
    ## removed 2023-03-06: not clear why I had it but it certainly no good for working on the front end.
    SCHED_CONFIG_STRING = "ConfigLocal"


class ConfigDev(ConfigBasic):

    def __init__(self):
        super().__init__()
        # Database
        self.DB_ROOT = self.DB_DEV_ROOT
        self.SQL_URI_USERS = f"sqlite:///{self.DB_DEV_ROOT}{os.environ.get('DB_NAME_USERS')}"
        self.SQL_URI_CAGE = f"sqlite:///{self.DB_DEV_ROOT}{os.environ.get('DB_NAME_CAGE')}"
        self.SQL_URI_BLS = f"sqlite:///{self.DB_DEV_ROOT}{os.environ.get('DB_NAME_BLS')}"
        # # other directories
        self.DIR_DB_AUXILARY = os.path.join(self.DB_DEV_ROOT,"auxilary")
        self.DIR_DB_AUX_IMAGES_PEOPLE = os.path.join(self.DIR_DB_AUXILARY,"images_people")

    DEBUG = True
    # SQL_URI = env_dict.get('SQL_URI_DEVELOPMENT')
    TEMPLATES_AUTO_RELOAD = True
    SCHED_CONFIG_STRING = "ConfigDev"


class ConfigProd(ConfigBasic):
        
    def __init__(self):
        super().__init__()
        # Database
        self.DB_ROOT = self.DB_PROD_ROOT
        self.SQL_URI_USERS = f"sqlite:///{self.DB_PROD_ROOT}{os.environ.get('DB_NAME_USERS')}"
        self.SQL_URI_CAGE = f"sqlite:///{self.DB_PROD_ROOT}{os.environ.get('DB_NAME_CAGE')}"
        self.SQL_URI_BLS = f"sqlite:///{self.DB_PROD_ROOT}{os.environ.get('DB_NAME_BLS')}"
        # # other directories
        self.DIR_DB_AUXILARY = os.path.join(self.DB_PROD_ROOT,"auxilary")
        self.DIR_DB_AUX_IMAGES_PEOPLE = os.path.join(self.DIR_DB_AUXILARY,"images_people")

    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
    SCHED_CONFIG_STRING = "ConfigProd"