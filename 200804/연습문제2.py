import re

mail = input("메일 주소를 입력하세요(아이디는 영문, 숫자, ., _만 사용가능.단, 숫자가 맨 앞에 올 수는 없음) : ")
res = re.match("(?P<id>[a-zA-Z_\.][\w_\.]+)[@](?P<domain>([\w]+\.)+[\w]+$)", mail)

if res:
    print("올바른 메일 주소입니다.")
    print("아이디 : ",res.group("id"))
    print("도메인 : ", res.group("domain"))
else:
    print("올바르지 않은 메일 주소입니다.")