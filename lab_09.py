import requests

r = requests.get('http://172.25.0.29/index.php')
#make a request to the desired webpage and load the entire response into the variable r

web_headers = r.headers
print("Here are the headers returned")
print(web_headers)
#Print the headers returned

web_html = r.text
print("Here is the html returned in the body of the webpage")
print(web_html)
#Print the body of the webpage

web_status_code = r.status_code
print("Here is the HTTP status code returned")
print(web_status_code)
#Print the status code of the request

web_cookies = r.cookies
print("Here are the cookies returned from the page")
print(web_cookies)
#Print any cookies

