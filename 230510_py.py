# Quiz 1
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")
houses.append(house1)
houses.append(house2)
houses.append(house3)
print("총 {0}대의 매물이 있습니다.".format(len(houses)))

for house in houses:
    house.show_detail()

# Quiz 2
class SoldOutError(Exception): # 사용자 정의 에러
    pass

try:
    num = int(input("Input your number: "))
    if num < 1:
        raise ValueError
    elif num > 10:
        raise SoldOutError
    
except ValueError:
    print("잘못된 값을 입력하였습니다.")

except SoldOutError:
    print("재고가 소진되어 더 이상 주문을 받지 않습니다.")

# 1
class 사람():
    def __init__(self):
        print("응애응애")

human = 사람()

# 2
class 사람():
    def __init__(self, name):
        self.name = name
        print("{} 님이 태어났습니다.".format(name))

human = 사람("유종훈")
human = 사람("조현호")

# 3
class 사람():
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def 연도(self):
        print(self.year)

human = 사람("유종훈", 1986)
human.연도()

# 4
class 사람():
    def __init__(self, name):
        self.name = name
    def 성(self):
        print(self.name[0])
    def 이름(self):
        print(self.name[1:])

human = 사람("유종훈")
human.성()
human.이름()

# 5
class 사람():
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
    def 친구0(self):
        print(self.name1)
    def 친구1(self):
        print(self.name2)

human = 사람("유종훈", "조현호")
human.친구0()
human.친구1()

# 6
class 사람():
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
    def 친구(self):
        print([self.name1, self.name2])

human = 사람("유종훈", "조현호")
human.친구()

# 7
name = []
class 사람:
    def __init__(self, *name):
        self.name = name

    def 친구추가(self):

    def 친구들(self):

human = 사람()
human.친구추가("김하나")
human.친구추가("김기리")
human.친구들()
