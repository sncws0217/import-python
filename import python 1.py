#1
station = "사당"
print(f"{station}행 열차가 들어오고 있습니다.")
station = "신도림"
print(f"{station}행 열차가 들어오고 있습니다.")
station = "인천공항"
print(f"{station}행 열차가 들어오고 있습니다.")

#2
from random import *
print(int(random() * 29) + 4)

#3
print("Hello World")

#4
print("Mary\'s cosmetics")

#5
print("신씨가 소리질렀다. \"도둑이야\".")

#6
print(2 + 2 * 3) # =8

#7
print("3" + "4") # =34

#8
print("#"*100)

#9
print(87720//34)

#10
letters = 'python'
print(letters[0], letters[2])

#11
license_plate = "24가 2210"
print(license_plate[4:])

#12
string = "홀짝홀짝홀짝"
print(string[::2])     

#13
string = "PYTHON"
print(string[::-1])

#14
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))

#15
print(phone_number.replace("-", ""))

#16
url = "https://sharebook.kr"
print(url[-2:])

#17
string = 'abcdfe2a354a32a'
print(string.replace('a', 'A'))

#18
string = 'abcd'
string.replace('b', 'B')
print(string) # aBcd