def profile(name, age, main_lang):
    print("이름: {0}\t나이: {1}\t공부하는 언어: {2}"\
          .format(name, age, main_lang))
    
profile("유재석",20,"파이썬")
profile("박명수",25,"자바")

# 기본값 적용 예시
def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t나이: {1}\t공부하는 언어: {2}"\
          .format(name, age, main_lang))
    
profile("유재석")
profile("박명수")