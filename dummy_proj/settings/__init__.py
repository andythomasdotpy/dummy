from decouple import config


# settings_path = "prod"

if config("settings_path") == "prod":
    from .prod import *
else:
    from .dev import *



