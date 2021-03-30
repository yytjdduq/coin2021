import random
menu = '쫄면','육계장','비빔밥','돈까스'
# 메뉴 출력
print(menu)
#그중에 아무거나 출력
print(random.choice(menu))

a = '쫄면'
b = '육계장'
c = '비빔밥'
d = '돈까스'

menulist = ['1. 쫄면','2. 육계장', '3. 비빔밥','4. 돈까스', '5. 짜장면']
print("메뉴 출력")
print("메뉴 갯수: ",  len(menulist))
for i in range(len(menulist)):
    print(menulist[i])
# print(menulist[0])
# print(menulist[1])
# print(menulist[2])
# print(menulist[3])
# print(menulist[4])
# print(a)
# print(b)
# print(c)
# print(d)

test_list = ['짜장', '짬뽕', '탕수육']
# for i in test_list:
#     print(i)