import json
import os
from dotenv import set_key


class EnvModel:
    def __init__(self):
        self.db_setting_path = os.getenv("DB_SETTING_PATH")
        self.log_path = os.getenv("LOG_DIR")
