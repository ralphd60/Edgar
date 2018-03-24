import requests
from bs4 import BeautifulSoup


def get_file_list(url):
    """using the request module, this will retrieve a sudo html list of the files in the director
    it will then use the Beautiful soup module to format the returned data into better formed html
    thrn filter snd return the file  list."""

    # create response object
    r = requests.get(url + 'index.html')

    # create beautiful-soup object
    soup = BeautifulSoup(r.content, "html.parser")

    # find all files in the directory using the tag <a>
    links = soup.find_all('a')
    file_list = [link['href'] for link in links if link['href'].endswith('idx')]
    file_list  = [x for x in file_list if x.startswith('master')]
    return file_list
