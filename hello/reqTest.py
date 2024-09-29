'''
Author: Bug Router
Date: 2024-09-27 13:11:53
Description: Default
'''
import requests
# from openpyxl import Workbook
params = {'gameNo': '350133', 'provinceId': '0', 'pageSize': '30', 'isVerify': '0', 'pageNo': '1', 'termLimits': '8' }
get_url = "http://webapi.sporttery.cn.com/gateway/lottery/getHistoryPageListV1.qry"
# 发送 GET 请求
response = requests.get(get_url, params=params)

# 检查请求状态码
if response.status_code == 200:
    print('请求成功')
    # 打印响应内容
    print(response)
    with open('example_zw.text', 'w', encoding='utf-8') as file:
        file.write(response.text)
    # 解析响应内容
else:
    print(f'请求失败，状态码：{response.status_code}')
