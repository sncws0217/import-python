# 1
for n in range(1, 51):
    with open(str(n) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(n))
        report_file.write("\n부서: ")
        report_file.write("\n이름: ")
        report_file.write("\n업무 요약: ")



import csv
with open("매수종목.csv", mode="wt", encoding="cp949", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["종목명", "종목코드", "PER"])
    writer.writerow(["삼성전자", "005930", 15.59])
    writer.writerow(["NAVER", "035420", 55.82])
file.close()



# 6, 7, 8
class Human:
    def __init__(self):
        print("응애응애")

areum = Human()

# 9, 10
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("이름: {}, 나이: {}, 성별: {}".format(self.name, self.age, self.gender))

areum = Human("김이룸", "25", "여자")

# 11
class 사람:
    def __init__(self):
        print("응애응애")
human = 사람()

# 12
class 사람:
    def __init__(self, name):
        self.name = name
        print("{} 님이 태어났습니다.".format(self.name))

human = 사람("유종훈")
human = 사람("조현호")

# 13
class 사람:
    def __init__(self, 이름, 연도):
        self.연도 = 연도
        print(연도)

human = 사람("유종훈", 1986)
human.연도

# 14
class 사람:
  def __init__(self, 사람0, 사람1):
    self.친구 = [사람0, 사람1]
human = 사람("유종훈", "조현호")
human.친구

