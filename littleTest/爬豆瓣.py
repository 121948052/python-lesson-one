import requests
from bs4 import BeautifulSoup
import openpyxl


def request_douban(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.146 Safari/537.36',
    }

    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def save_to_excel(soup, workbook):
    sheet = workbook.active
    sheet.title = '豆瓣电影Top250'
    sheet.append(['名称', '图片', '排名', '评分', '作者', '简介'])

    movie_list = soup.find(class_='grid_view').find_all('li')

    for item in movie_list:
        item_name = item.find(class_='title').string
        item_img = item.find('a').find('img').get('src')
        item_index = item.find('em').string
        item_score = item.find(class_='rating_num').string
        item_author = item.find('p').text
        if item.find(class_='inq') is not None:
            item_intr = item.find(class_='inq').string
        else:
            item_intr = 'NOT AVAILABLE'

        print('爬取电影：' + item_index + ' | ' + item_name + ' | ' + item_score + ' | ' + item_intr)

        sheet.append([item_name, item_img, item_index, item_score, item_author, item_intr])


def main(page):
    url = 'https://movie.douban.com/top250?start=' + str(page * 25) + '&filter='
    html = request_douban(url)
    soup = BeautifulSoup(html, 'lxml')
    workbook = openpyxl.Workbook()
    save_to_excel(soup, workbook)
    workbook.save(u'豆瓣最受欢迎的250部电影.xlsx')


if __name__ == '__main__':
    for i in range(0, 10):
        main(i)