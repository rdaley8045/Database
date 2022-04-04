import json
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