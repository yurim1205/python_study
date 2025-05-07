class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location,self.house_type,self.deal_type,\
            self.price,self.completion_year)
        
houses = []
house1 = House("강남","아파트","매매","10억","2010년")
house2 = House("마포","오피스텔","전세","5억","2007년")
house3 = House("송파","빌라","월세","500/50","2000년")

# show_detail를 통해 각각 출력하면 번거로우니까
# 간편하게 리스트를 통해 출력하기 위해 append 사용
houses.append(house1)
houses.append(house2)
houses.append(house3)

# house: 반복문을 위한 임시 변수
for house in houses:
    house.show_detail()