class ThailandPackage:
    def detail(self):
        print("방콕 야시장 투어 50만원")

if __name__ == "__main__":
    print("Thailand 모듈 직접 실행")
    trip_to=ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")