import os

def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
   
def delete_file_contents(path):
    with open(path, 'w'):
        pass

def file_to_set(fileName):
    results = set()
    with open(fileName, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

def set_to_file(links, fileName):
    delete_file_contents(fileName)
    for link in sorted(links):
        append_to_file(fileName, link)


def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating project: ", directory)
        os.makedirs(directory)

def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url) 
    if not os.path.isfile(crawled):
        write_file(crawled, '')
    