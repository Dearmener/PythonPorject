"""
本代码演示了
"""
# 写一个字面量
print(1231)
# write a string
print("黑马程序员")

class Car:
    name = "10"
    age = 101
    def __init__(self):
        print("初始化") 
    def hello(self):
        print("hello")
    
car = Car()
car.hello()
print(f"car{car.age}")