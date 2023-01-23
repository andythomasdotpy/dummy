import os
from decouple import config


# settings_path = "prod"

# os.environ.get('TWITTER_ACCESS_TOKEN')

if os.environ.get('SETTINGS_PATH') == "prod":
    from .prod import *
else:
    from .dev import *



