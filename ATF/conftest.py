import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

def pytest_sessionstart(session):
    log_file = os.path.join(os.path.dirname(__file__), "test_run.log")
    open(log_file, "w").close()
