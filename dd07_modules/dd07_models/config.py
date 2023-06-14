import os
from dd07_config import ConfigDev, ConfigProd, ConfigLocal

if os.environ.get('FLASK_ENV')=='local':
    config = ConfigLocal()
    print('- dd07_models/config: Local')
elif os.environ.get('FLASK_ENV')=='dev':
    config = ConfigDev()
    print('- dd07_models/config: Development')
elif os.environ.get('FLASK_ENV')=='prod':
    config = ConfigProd()
    print('- dd07_models/config: Production')