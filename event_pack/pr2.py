import threading
from resource import create_resouce


second = threading.Thread(target=create_resouce, args=[2])
second.start()
