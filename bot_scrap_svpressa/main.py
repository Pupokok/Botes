import requests
from time import sleep
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

all_articles = []
ua = UserAgent()
headers = {"user-agent": ua.random}

def add_article(title_text):
    if title_text not in all_articles:
        all_articles.append(title_text)
        return True
    else:
        return False

def main_card_parse():
    s = requests.Session()
    response = s.get(url='https://svpressa.ru', headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    page_count = soup.find("div", class_="b-content__main")
    main_cont = page_count.find("div", class_="b-content__index-article_main-news") #first container
    main_card = main_cont.find("article", class_="b-article")
    url_main_card = "https://svpressa.ru/" + main_card.find("a", class_="b-article__img").get("href")

    response_card = s.get(url=url_main_card, headers=headers)
    soup_card = BeautifulSoup(response_card.text, "lxml")

    card = soup_card.find("article", class_="b-text")
    header_card = card.find("header", class_="b-text__header")
    title_text = header_card.find("h1", class_="b-text__title").text

    if add_article(title_text):
        subtitle_text = header_card.find("h2", class_="b-text__subtitle").text
        img_item = f'\n<a href="https://t.me/rubanoknews">👉Подписаться. Рубанок</a>'
        text_in_card = card.find_all("p")
        text_paragraphs = [p_tag.text for p_tag in text_in_card[:2]]
        try:
            img_page = header_card.find("div", class_="b-text__info-and-img").find("div", class_="b-text__img")
            img_url = img_page.find("picture").find("source").get("srcset")
        except:
            img_url = None

        title_text += f'<a href="https://svpressa.ru/{img_url}">\u200B</a>'

        article_data = {
            "title": f"<b>{title_text}</b>",
            "subtitle": subtitle_text,
            "text_paragraphs": text_paragraphs,
            "img_url": img_item
        }

        return [article_data]

    return []

def sec_card_parse():
    s = requests.Session()
    response = s.get(url='https://svpressa.ru', headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    page_count = soup.find("div", class_="b-content__main")
    second_cards = page_count.find("div", class_="b-index__main")
    sects = second_cards.find_all("div", class_="b-articles")

    sec_articles_data = []  

    for sect in sects:
        url_list = []
        url_arts = sect.find_all("article", class_="b-article")

        for url_art in url_arts[:2]:
            try:
                url_get = "https://svpressa.ru/" + url_art.find("a", class_="b-article__img").get('href')
                url_list.append(url_get)
            except:
                pass

        for href in url_list:
            sleep(2)
            resp = requests.get(url=href, headers=headers)
            soup_hr = BeautifulSoup(resp.text, "lxml")
            card = soup_hr.find("article", class_="b-text")
            header_card = card.find("header", class_="b-text__header")
            tit_text = header_card.find("h1", class_="b-text__title").text

            if add_article(tit_text):
                sub_text = header_card.find("h2", class_="b-text__subtitle").text
                img_item = f'\n<a href="https://t.me/rubanoknews">👉Подписаться. Рубанок</a>'
                text_card = card.find_all("p")
                text_paragr = [p_tag.text for p_tag in text_card[:2]]

                try:
                    img_page = header_card.find("div", class_="b-text__info-and-img").find("div", class_="b-text__img")
                    img_ur = img_page.find("picture").find("source").get("srcset")
                except:
                    img_ur = None

                tit_text += f'<a href="https://svpressa.ru/{img_ur}">\u200B</a>'

                article_data = {
                    "title": f"<b>{tit_text}</b>",
                    "subtitle": sub_text,
                    "text_paragraphs": text_paragr,
                    "img_url": img_item
                }

                sec_articles_data.append(article_data)

    return sec_articles_data
