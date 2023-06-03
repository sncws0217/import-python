#1

#2




#1
nums = [1, 2, 3, 4, 5, 6, 7]
print("max:", (max(nums)))
print("min:", (min(nums)))

#2
string = "삼성전자/LG전자/Naver"
interest = [string[0:4], string[5:9], string[10:15]]
print(interest)

#3
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

#4
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print(interest)

#5
num = tuple(range(2, 100 ,2))
print(num)

#6
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print("메로나 가격: " ,ice.get('메로나'))

#7
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

#8
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

#9
str = "rainbow"
print(sorted(str))

#10
nums = [1, 4, 1, 2, 4, 2, 4, 2, 3, 4, 4]
nums = len(nums.index())
print(nums)
