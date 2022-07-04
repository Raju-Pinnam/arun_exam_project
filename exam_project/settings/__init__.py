import os

APP_ENV = os.environ.get("APP_ENV", "local")

if APP_ENV == "prod":
    from .prod import *
else:
    from .local import *