# 2. 회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 말한다.
# 예를 들면 "level", "SOS", "rotator"과 같은 단어와 문장이 그러하다.
# 임의의 문장을 입력받아 회문 여부를 출력하시오

word = input("단어를 입력하세요 : ")
word_list = list(word.strip())
word_rev = "".join(reversed(word_list))

if word == word_rev:
    print("회문")
else:
    print("회문아님")