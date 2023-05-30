# 将数字类型转化为字符串
num_str = str(11)
print(type(num_str),num_str)

float_str = str(11.345)
print(type(float_str),float_str)
# 将字符串转化为数字
num = int("11")
print(type(num),num)

num2 = float("11.345")
print(type(num2),num2)

# 整数转浮点数
float_num = float(11)
print(type(float_num),float_num)

# 浮点数转整数 会丢失精度
int_num = int(11.345)
print(type(int_num),int_num)

# str转int
str_int = int("11.32")
print(type(str_int),str_int)