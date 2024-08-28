# from datetime import datetime
# def test(a):
#     year,month,day=map(int, a)
#     res = datetime(year,month,day)
#     if res.month==10 and res.day==31:
#         print("Bonfire toffee")
#     else:
#         print("toffee")
# a=input().split('/')
# test(a)

# from datetime import datetime
# def test(a):
#     return (a+99)//100
# a=int(input())
# print(test(a))

# def func(a, b):
#     if a == "" :
#         return "year missing"
#     if b == "" :
#         return "month missing"
#     s = b // 12
#     return a + s
# print(func(2020, 24))
# print(func(1832, 2)) 
# print(func(1444, 60))
# print(func("", 24))  
# print(func(2020, ""))

# def func(a):
#     month, day, year = a.split('/')
#     s = f"{year}{day}{month}"
#     return s
# print(func("11/12/2019"))
# print(func("12/31/2019"))

# from datetime import date
# def func(a):
#     return a.month == 12 and a.day == 24
# print(func(date(2013, 12, 24)))
# print(func(date(2013, 12, 23)))
# print(func(date(3000, 12, 24)))

# from datetime import datetime
# def func(a):
#     a = datetime.strptime(a, '%m/%d/%Y')
#     b = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#     c = (a.weekday() + 1) % 7
#     return b[c]
# print(func("12/07/2016")) 
# print(func("09/04/2016")) 
# print(func("12/08/2011"))