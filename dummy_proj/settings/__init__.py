import os
from decouple import config


SETTINGS_PROD = "prod"

print(f"printing **before** {config('SETTINGS_PATH')}")

if SETTINGS_PROD == "prod":
    print("prod.py settings activated!")
    from .prod import *
else:
    print("dev.py settings activated!")
    from .dev import *



