name = "Black Coder"
message = "Come to %s to Learn Coding" % name
print(message)

class_num = 57
avg_salary = 16781
message = "Python DataScience,Beijin %s,avg salary %s" % (class_num,avg_salary)
print(message)

name = "chuanzhiboke"
set_up_year = 2006
stock_price = 19.9
message = "%s setup in %d,today's stock is %.2f" % (name,set_up_year,stock_price)
print(message)

num_1 = 11
num_2 = 11.345

print("%5d"%num_1)
print("%1d"%num_1) #宽度设置为1，但是11为两位，不生效
print("%7.2f"%num_2)
print("%.5f"%num_2)