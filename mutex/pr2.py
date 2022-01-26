import threading
from resouce import create_resouce


second = threading.Thread(target=create_resouce, args=[2])