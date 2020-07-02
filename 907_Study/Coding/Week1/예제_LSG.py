
#14681
""" if문
x=int(input())
y=int(input())

if x>0:
    if y>0:
        print("1")
    else:
        print("4")
elif x<0:
    if y>0:
        print("2")
    else:
        print("3")
"""

"""for문
#106116
number=int(input())
type(number)
for i in range(1,10):
    print("%d * %d = %d" % (number, i,number*i))

    i=i+1
"""
""" while문 (아직 작업중)
#1110
number = int(input())
if number<99 and number>=0:
    ten = int(number / 10)
    one = number % 10
    sum = ten + one
    if int(sum / 10) != 0:  # 일의 자리 수가 아니라면?
        sum = sum % 10

    number_1 = one * 10 + sum
    cycle = 1

    while True:
        ten = int(number_1 / 10)
        one = number_1 % 10
        sum = ten + one
        if int(sum / 10) != 0:  # 일의 자리 수가 아니라면?
            sum = sum % 10
        number_1 = one * 10 + sum
        cycle = cycle + 1

        if number_1 == number:
            break
    print(cycle)
"""
