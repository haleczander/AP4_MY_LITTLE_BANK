from dotenv import dotenv_values

CONFIG = dotenv_values(".env")
API = CONFIG['METIER']
