import threading
from resource import create_resouce


first = threading.Thread(target=create_resouce, args=[1])
first.start()
