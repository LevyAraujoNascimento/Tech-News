from parsel import Selector
from tech_news.database import create_news
import requests
import time


url_beTrybe = 'https://blog.betrybe.com/'


# Requisito 1
def fetch(url):
    header = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=header, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    urls = selector.css(".entry-title a::attr(href)").getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css(".next::attr(href)").get()
    if next_page:
        return next_page
    else:
        return None


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)

    t = ".meta-reading-time::text"
    s = ".entry-content > p:first-of-type *::text"

    result = {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "reading_time": int(selector.css(t).get().split(" ")[0]),
        "summary": "".join(selector.css(s).getall()).strip(),
        "category": selector.css(".label::text").get()
    }

    return result


# Requisito 5
def get_tech_news(amount):
    content_beTrybe = fetch(url_beTrybe)
    news_urls = scrape_updates(content_beTrybe)
    news = []

    for i in range(amount):
        if i == (len(news_urls) - 1):
            next_url = scrape_next_page_link(content_beTrybe)
            content_beTrybe = fetch(next_url)
            news_urls += scrape_updates(content_beTrybe)

        news_content = fetch(news_urls[i])
        final_news = scrape_news(news_content)
        news.append(final_news)

    create_news(news)

    return news
