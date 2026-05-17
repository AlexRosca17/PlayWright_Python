import logging
import os

_log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "test_run.log")

_handler_file = logging.FileHandler(_log_file, mode="a", encoding="utf-8")
_handler_file.setLevel(logging.INFO)
_handler_file.setFormatter(logging.Formatter("%(asctime)s - [%(thread)d] - %(levelname)s - %(message)s"))

_handler_console = logging.StreamHandler()
_handler_console.setLevel(logging.INFO)
_handler_console.setFormatter(logging.Formatter("%(asctime)s - [%(thread)d] - %(levelname)s - %(message)s"))

_root_logger = logging.getLogger()
_root_logger.setLevel(logging.INFO)
_root_logger.addHandler(_handler_file)
_root_logger.addHandler(_handler_console)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
