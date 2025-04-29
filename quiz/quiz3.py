# 사이트별로 비밀번호를 만들어주는 프로그램 작성하기

# 예: http://naver.com
# 규칙1: naver.com만 출력
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 -> naver
# 규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

url = "http://naver.com"
my_str = url.replace("http://", "")
# print(my_str)

my_str = my_str[0:5]
# 또는
# my_str = my_str[:my_str.index(".")]
# print(my_str)
 
# print(my_str) + print(my_str.count(my_str))

password = my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password)