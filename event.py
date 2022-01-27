import subprocess
import threading
from loguru import logger
import time


"""
    Тут я создаю 2 разныз процесса, в каждомм процессе есть поток, который получает доступ к ресурсу с событием
    событие позволяет дождаться окончания работы одного потока с помощью setEvent и в этот момент 2 поток,
    который пребывал в режиме ожидания WaitForSingleObject начнет свою работу
"""


def one():
    subprocess.call(['python', 'event_pack/pr1.py'], shell=True)


def two():
    subprocess.call(['python', 'event_pack/pr2.py'], shell=True)


first = threading.Thread(target=one)
second = threading.Thread(target=two)

first.start()
time.sleep(0.01)
second.start()
