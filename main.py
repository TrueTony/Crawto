import sys
import threading
from urllib.parse import urlparse
from queue import Queue
from spider import Spider
from general import file_to_set


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():
    while True:
        url = thread_queue.get()
        Spider.crawled_page(threading.current_thread().name, url)
        thread_queue.task_done()

def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        thread_queue.put(link)
    thread_queue.join()
    crawl()

def crawl():
    queue_links= file_to_set(QUEUE_FILE)
    if len(queue_links) > 0:
        print(f'{len(queue_links)} links in the queue')
        create_jobs()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('You must to pass a link')
        sys.exit(0)
    if (isinstance(sys.argv[2], int)) or (int(sys.argv[2]) < 1):
        print('Second argument must be an integer above 0')
        sys.exit(0)
    HOMEPAGE = sys.argv[1]
    PROJECT_NAME = urlparse(sys.argv[1]).netloc
    if len(sys.argv) == 3:
        NUMBER_OF_THREADS = int(sys.argv[2])
    else:
        NUMBER_OF_THREADS = 4
    QUEUE_FILE = PROJECT_NAME + '/queue.txt'
    CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
    thread_queue = Queue()
    Spider(PROJECT_NAME, HOMEPAGE)
    create_workers()
    crawl()
