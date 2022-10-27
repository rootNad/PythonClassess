import threading
import queue
import urllib.request
from pprint import pprint


def get_url(q, _url):
    print(f"get_url({_url}) called from a thread")
    q.put(urllib.request.urlopen(_url).read())


urls = ["http://google.com", "http://google.de", "http://google.ca"]

thread_queue = queue.Queue()

for url in urls:
    t = threading.Thread(target=get_url, args=(thread_queue, url, ))
    t.daemon = True
    t.start()

output = thread_queue.get()
pprint(output)