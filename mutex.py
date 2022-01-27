import subprocess
import threading
from loguru import logger
import time


"""
    Тут я создаю 2 разныз процесса, в каждомм процессе есть поток, который получает доступ к ресурсу с мьютексом
    Мьютекс позволяет разграничивать не только потоки в одном, но и в разных процессах
    Для проверки я запускаю процессы с разницей в 1 сотую секунды, сам ресурс выполняется 2 секунды
"""


def one():
    subprocess.call(['python', 'mutex_pack/pr1.py'], shell=True)


def two():
    subprocess.call(['python', 'mutex_pack/pr2.py'], shell=True)


first = threading.Thread(target=one)
second = threading.Thread(target=two)

first.start()
time.sleep(0.01)
second.start()
