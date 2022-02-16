from envparse import env

env.read_envfile()

TOKEN_TELEGRAM = env.str("TOKEN_TELEGRAM")
