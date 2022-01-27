from win32.win32event import CreateEvent, OpenEvent, WaitForSingleObject, SetEvent
from loguru import logger
import time


logger.add("test.log", rotation="200 MB")


def create_resouce(name):
    logger.info(f"Поток {name} Входит в программу ")
    try:
        event = OpenEvent(0x1F0003, True, "Secure Resouce")
        logger.info(f"Поток {name} ждет пока закончит другой поток")
        WaitForSingleObject(event, 100000)
    except Exception as e:
        logger.info(f"Поток {name} создает событие")
        event = CreateEvent(None, True, False, "Secure Resouce")

    logger.info(f"Поток {name} приступил к работе ")
    time.sleep(2)
    SetEvent(event)  # сигнализируем 2-му потоку, что нужно приступить к работе
    logger.info(f"Поток {name} завершился ")
