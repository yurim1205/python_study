import pickle

with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file))
# close() 필요없음
    
with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("파이썬 공부 중")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())

# with를 사용하면 가독성도 좋아지고, close()도 필요없음