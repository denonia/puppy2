import secrets

from envparse import env

env.read_envfile()

TOKEN_TELEGRAM = env.str("TOKEN_TELEGRAM")

# DOMAIN = env.str("DOMAIN", default="localhost")
# SECRET_KEY = secrets.token_urlsafe(48)
# WEBHOOK_BASE_PATH = env.str("WEBHOOK_BASE_PATH", default="/webhook")
# WEBHOOK_PATH = f"{WEBHOOK_BASE_PATH}/{SECRET_KEY}"
# WEBHOOK_URL = f"https://{DOMAIN}{WEBHOOK_PATH}"
