import re

domain = input("url을 입력하세요 : ")
res = re.match("^(http://|https://)(?P<add>w{3}\.[\w_]+\.[a-zA-Z\.]+)(?P<path>(/[\w_]+)*)/(?P<file>([\w_]+(\.|\?|=))+[\w_]+$)", domain)

if res:
    print("올바른 도메인")
else:
    print("올바르지 않은 도메인")