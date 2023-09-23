from tech_news.database import db


# Requisito 7
def search_by_title(title):
    news = list(db.news.find({"title": {"$regex": title, "$options": "i"}}))
    tuplas = []
    for new in news:
        tuplas.append((new["title"], new["url"]))
    return tuplas


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
