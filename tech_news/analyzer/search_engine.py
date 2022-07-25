from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    return [(noticia["title"], noticia["url"]) for noticia in search_news({
        "title": {"$regex": title, "$options": "i"}
    })]


# Requisito 7
def search_by_date(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    return [(noticia["title"], noticia["url"]) for noticia in search_news({
        "timestamp": {"$regex": date.strftime("%d/%m/%Y")}
    })]


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
