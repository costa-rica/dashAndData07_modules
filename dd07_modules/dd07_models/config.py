import os
from dd07_config import ConfigDev, ConfigProd, ConfigLocal

match os.environ.get('FLASK_CONFIG_TYPE'):
    case 'dev':
        config = ConfigDev()
        print('- dd07_models/config: Development')
    case 'prod':
        config = ConfigProd()
        print('- dd07_models/config: Production')
    case _:
        config = ConfigLocal()
        print('- dd07_models/config: Local')
    