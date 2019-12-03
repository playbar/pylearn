
from bs4 import BeautifulSoup
import requests
from urlparse import urlparse

import urllib2
import ssl

context1 = ssl._create_unverified_context()
response = urllib2.urlopen('https://www.python.org/',context = context1)
print(response.read().decode("utf-8"))

start_url = 'https://www.cnblogs.com'
trust_host = 'www.cnblogs.com'
ignore_path = []
history_urls = []


def parse_html(html):
    soup = BeautifulSoup(html, "lxml")
    print(soup.title)
    links = soup.find_all('a', href=True)
    return (a['href'] for a in links if a['href'])


def parse_url(url):
    url = url.strip()

    if url.find('#') >= 0:
        url = url.split('#')[0]
    if not url:
        return None
    if url.find('javascript:') >= 0:
        return None

    for f in ignore_path:
        if f in url:
            return None
    if url.find('http') < 0:
        url = start_url + url
        return url
    parse = urlparse(url)
    if parse.hostname == trust_host:
        return url


def consumer():
    html = ''
    while True:
        url = yield html
        if url:
            print('[CONSUMER] Consuming %s...' % url)
            rsp = requests.get(url)
            html = rsp.content


def produce(c):
    next(c)

    def do_work(urls):
        for u in urls:
            if u not in history_urls:
                history_urls.append(u)
                print('[PRODUCER] Producing %s...' % u)
                html = c.send(u)
                results = parse_html(html)
                work_urls = (x for x in map(parse_url, results) if x)
                do_work(work_urls)

    do_work([start_url])
    c.close()


if __name__ == '__main__':
    c = consumer()
    produce(c)
    print(len(history_urls))

