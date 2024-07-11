import threading
from queue import Queue
from spider import Spider
import domain as dm
import general as gen

project_name = input("Enter the project name: ")
home_page = input("Enter the homepage URL: ")
#https://www.vit.edu/
#https://www.viit.ac.in/
DOMAIN_NAME = dm.get_domain_name(home_page)
QUEUE_FILE = project_name + '/queue.txt'
CRAWLED_FILE = project_name + '/crawled.txt'
NUMBER_OF_THREADS = 4
queue = Queue()

Spider(project_name, home_page, DOMAIN_NAME)

def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True 
        t.start()

def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()



def create_jobs():
    for link in gen.file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join() 
    crawl()

def crawl():
    queued_links = gen.file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()

create_workers()
crawl()
#https://pict.edu/
#https://www.pictmodelschool.edu.in/