from tech_news.database import db


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
    pass


# Requisito 9
def search_by_category(category):
    # campo de busca
    c = "category"

    news = list(db.news.find({c: {"$regex": category, "$options": "i"}}))
    tuplas = []
    for new in news:
        tuplas.append((new["title"], new["url"]))
    return tuplas
