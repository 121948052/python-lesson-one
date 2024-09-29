'''
Author: Bug Router
Date: 2024-09-27 18:05:19
Description: Default
'''
from scapy.all import IP, ICMP, sr
 
def scan(target_ip):
    # 构建一个ICMP回显请求数据包
    request = IP(dst=target_ip) / ICMP()
    # 发送数据包，并接收回显响应或超时
    responses = sr(request, timeout=2, verbose=False)
 
    # 打印收到的响应数据包
    for index, response in enumerate(responses):
        response_ip = response[IP]
        if response_ip.proto == 1:  # 1代表ICMP
            response_icmp = response[ICMP]
            print(f"响应{index+1}: Type = {response_icmp.type}, Code = {response_icmp.code}")
 
# 使用示例
target_ip = "10.220.184.32"  # 替换为目标IP地址
scan(target_ip)