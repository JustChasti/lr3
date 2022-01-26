from win32.win32event import CreateMutex
from loguru import logger
import time


logger.add("test.log", rotation="200 MB")


def create_resouce(name):
    logger.info(f"Поток {name} получил доступ к ресурсу")
    mutex = CreateMutex(None, False, "Secure Resouce")
    time.sleep(2)
    logger.info(f"Поток {name} заершился")
