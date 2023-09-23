from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    # campo de busca
    c = "title"

    news = list(db.news.find({c: {"$regex": title, "$options": "i"}}))
    tuplas = []
    for new in news:
        tuplas.append((new["title"], new["url"]))
    return tuplas


# Requisito 8
def search_by_date(date):
    # campo de busca
    c = "timestamp"

    try:
        date_format = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        news = list(db.news.find({c: {"$regex": date_format}}))
        tuplas = []
        for new in news:
            tuplas.append((new["title"], new["url"]))
        return tuplas
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    # campo de busca
    c = "category"

    news = list(db.news.find({c: {"$regex": category, "$options": "i"}}))
    tuplas = []
    for new in news:
        tuplas.append((new["title"], new["url"]))
    return tuplas
