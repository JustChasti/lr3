import threading
from resouce import create_resouce


first = threading.Thread(target=create_resouce, args=[1])
