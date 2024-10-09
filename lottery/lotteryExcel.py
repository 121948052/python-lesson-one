'''
Author: Bug Router
Date: 2024-09-30 10:31:48
Description: Default
'''
import requests
import xlwt
import json


def request_lottery(url):
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


book = xlwt.Workbook(encoding='utf-8', style_compression=0)

sheet = book.add_sheet('近100期', cell_overwrite_ok=True)
sheet.col(0).width = 10 * 256
sheet.col(1).width = 30 * 256
sheet.write(0, 0, '期')
sheet.write(0, 1, '结果')

n = 1


def save_to_excel(soup):
    response_str = json.loads(soup)
    
    if response_str['success'] == True:
        data_list = response_str['value']['list']
        print(data_list[0])

        for item in data_list:
            item_num = item['lotteryDrawNum']
            item_value = item['lotteryDrawResult']

            global n

            sheet.write(n, 0, item_num)
            sheet.write(n, 1, item_value)

            n = n + 1
    else:
        print('爬取失败')
        print(response_str['message'])

def main():
    url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=100&isVerify=1&pageNo=1&termLimits=100'
    soup = request_lottery(url)
    save_to_excel(soup)


if __name__ == '__main__':
    main()

book.save(u'近100期大乐透开奖结果.xls')