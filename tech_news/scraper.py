import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if response.status_code == 200:
            return response.text
    except (requests.ReadTimeout, requests.HTTPError):
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return [
        link for link in selector.css("a.cs-overlay-link::attr(href)").getall()
        ]


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css("a.next::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    noticia = {}
    noticia["url"] = selector.css("link[rel=canonical]::attr(href)").get()
    noticia["title"] = selector.css(".entry-title::text").get().strip()
    noticia["timestamp"] = selector.css(".meta-date::text").get()
    noticia["writer"] = selector.css(".author a::text").get()
    comments = selector.css(".tithe-block::text").get()
    if comments is None:
        comments = 0
    noticia["comments_count"] = comments
    noticia["summary"] = ''.join(
            selector.css(".entry-content > p:nth-of-type(1) *::text").getall()
        ).strip()
    noticia["tags"] = selector.css("a[rel=tag]::text").getall()
    noticia["category"] = selector.css(
        ".category-style .label::text").get()

    if noticia["comments_count"] is None:
        noticia["comments_count"] = 0

    return noticia


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
