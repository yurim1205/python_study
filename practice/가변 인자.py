# end=" " : 줄바꿈을 안 하겠다는 의미
def profile(name, age, lang1,lang2,lang3,lang4,lang5):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    print(lang1,lang2,lang3,lang4,lang5)

# 가변인자 적용 예시
def profile(name, age, *language):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print() # 줄바꿈

profile("이유림", 26, "python", "java", "c", "c++", "c#","js")
profile("박명수",24,"kotlin","swift")