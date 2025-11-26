import os
from datetime import datetime

from model.env_model import EnvModel


class Logging:
    def __init__(self):
        self.env = EnvModel()

    def _write_in_file(self, path: str, text: str) -> None:
        full_path = self.env.log_path + "/" + path
        with open(full_path, "a") as f:
            f.write(text)

    def write_error(self, error: str) -> None:
        error_name = datetime.now().strftime("%Y%m%d-%H%M%S") + "_error.txt"
        self._write_in_file(error_name, error)

    def write_warning(self, warning: str) -> None:
        warning_name = datetime.now().strftime("%Y%m%d-%H%M%S") + "_warning.txt"
        self._write_in_file(warning_name, warning)

    def write_info(self, info: str) -> None:
        info_path = datetime.now().strftime("%Y%m%d-%H%M%S") + "_info.txt"
        self._write_in_file(info_path, info)
