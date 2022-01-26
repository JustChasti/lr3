import threading
import time
from loguru import logger


balance = 0  # Это баланс аккаунта
balance_lock = threading.Lock()  # локер


def change_account_balance(delta, num):
    """
        Если данное дествие не заблокировать, то при запуске 2 и более потоков,
        так как действие += состоит из нескольких операций может возникнуть конфлит,
        приводящий к непредсказуемым результатам
    """
    logger.info(f"Поток {num} зашел")
    global balance
    with balance_lock: # секция блокируется для одного потока
        if delta > 0:
            time.sleep(2) # тут проверка - что второй поток не пойдет, пока 1 не закончит менять баланс
        logger.info(f"Поток {num} меняет баланс")
        balance += delta
    logger.info(f"balance = {balance}")


first = threading.Thread(target=change_account_balance, args=[110, 1])
second = threading.Thread(target=change_account_balance, args=[-100, 2])
first.start(), second.start()
