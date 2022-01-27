from win32.win32event import CreateMutex, OpenMutex
from loguru import logger
import time


logger.add("test.log", rotation="200 MB")


def create_resouce(name):
    logger.info(f"Поток {name} Входит в программу ")
    flag = False
    try:
        mutex = OpenMutex(0x1F0001, False, "Secure Resouce")
        logger.info(f"Поток {name} Не получил доступ к ресурсу, так как он занят другим потоком ")
    except Exception as e:
        logger.info(f"Поток {name} создает событие")
        mutex = CreateMutex(None, True, "Secure Resouce")
        flag = True
    if flag:
        logger.info(f"Поток {name} приступил к работе ")
        time.sleep(2)
        logger.info(f"Поток {name} завершился ")
