import json
import logging.config
from typing import Any
from pydantic import BaseSettings
import psycopg2

class Settings(BaseSettings):



    def __init__(self, **values: Any):
        super().__init__(**values)

        self.prom = mysql.connector.connect(
            host='localhost',
            user='tomandjerry',
            password='roadrunner'

        )

        print (self.prom)
        
def ConfigureLogging():
    log_config = {
        'version': 1,
        'formatters': {
            'f': {'format': "%(asctime)s - %(levelname)s - %(message)s"}
        },
        'handlers': {
            'h': {'formatter': 'f', 'level': logging.INFO, 'class': 'logging.StreamHandler'}
        },
        'loggers': {
            'root': {'level': logging.INFO, 'handlers': 'h', 'propagate': False},
            'uvicorn': {'error': {'propagate': True}}
        }
    }
    logging.config.dictConfig(log_config)
