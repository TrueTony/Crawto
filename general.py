import os


def create_project(project_name, base_url):
    if not os.path.exists(project_name):
        os.mkdir(project_name)
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        with open(queue, 'w', encoding="utf-8") as f:
            f.write(base_url)
    if not os.path.isfile(crawled):
        with open(crawled, 'w', encoding="utf-8") as f: pass

def append_link(path, link):
    with open(path, 'a', encoding="utf-8") as f:
        f.write(link + '\n')

def delete_file_data(path):
    with open(path, 'w', encoding="utf-8") as f: pass

def file_to_set(file):
    results = set()
    with open(file, 'rt', encoding="utf-8") as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

def set_to_file(links, file):
    delete_file_data(file)
    with open(file, 'w', encoding="utf-8") as f:
        for link in sorted(links):
            f.write(link + '\n')
