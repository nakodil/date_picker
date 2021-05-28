from bs4 import BeautifulSoup
import requests


def get_site_content(urls: list) -> str:
    page_content = []
    for url in urls:
        response = requests.get(url)
        response.encoding = 'utf-8'
        page_content.append(response.text)
    return " ".join(page_content)


def make_holidays_list(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    cals = soup.find_all("table", class_="cal")

    # Парсим праздничные дни
    holidays_list = []
    for cal in cals:
        cal_content_str = str(cal)
        cal_soup = BeautifulSoup(cal_content_str, 'html.parser')
        month_str = cal_soup.find("th", class_="month").text
        holidays = cal_soup.find_all("td", class_="holiday weekend")
        for holiday in holidays:
            if len(holiday.text) < 2:
                holidays_list_item = month_str + " " + "0" + holiday.text
            else:
                holidays_list_item = month_str + " " + holiday.text
            holidays_list.append(holidays_list_item)
    return holidays_list

