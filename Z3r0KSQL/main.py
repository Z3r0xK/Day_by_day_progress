import requests
url = input("Enter url: ")
try:
    response = requests.get(url)
except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.InvalidURL) as error:
    print("Enter Valid Url {}".format(error))
if "?" in url:
    print("Another Something")
else:
    print("Another Something")
