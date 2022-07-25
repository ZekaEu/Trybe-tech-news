from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    return [(noticia["title"], noticia["url"]) for noticia in search_news({
        "title": {"$regex": title, "$options": "i"}
    })]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    return [(noticia["title"], noticia["url"]) for noticia in search_news({
        "tags": {"$regex": tag, "$options": "i"}
    })]


# Requisito 9
def search_by_category(category):
    return [(noticia["title"], noticia["url"]) for noticia in search_news({
        "category": {"$regex": category, "$options": "i"}
    })]
