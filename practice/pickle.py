import pickle
profile_file = open("profile.pickle","wb")
profile={"이름":"이유림", "나이":26, "취미":["음악 듣기","카페 투어"]}
print(profile)

# profile에 있는 정보를 file에 저장함
pickle.dump(profile, profile_file)
profile_file.close()


# file에 있는 정보 불러오기
profile_file = open("profile.pickle","rb")
profile=pickle.load(profile_file)
print(profile)
profile_file.close()