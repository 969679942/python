#加减乘除，除法自动保留一个小数点，不想保留小数点再加一个/例如8//4=2，8/4=2.0
print(1+2);
print(3-4);
print(5*6);
print(8/5);
print(8//5);
# 输出结果为：
# 3
# -1
# 30
# 1.6
# 1

#变量
width=3;
height=4;
s=width * height;
print(s);
#输出结果：12

#循环语句 if  if-else  elif  while  for for-while break循环控制
#在python编程中变量自加只有两种方式；i=i+1;i+=1;没有i++;

age=18;
if(age<20):
	print("符合小于20的年龄");

if(age>20):
	age=age+1;
else:
	age=age+1;
	print(age);

if(age>19):
	print("年龄大于19");
elif(age==19):
	print("年龄等于19");

#python 的 for 遍历：从一个序列中逐一取出
for i in range(5):
	print(i,end="");
print();
#输出结果01234
#遍历大于等于1，小于5的数字，输出结果1234

for i in range(1,5):
	print(i,end="");
print();

#遍历大于等于1，小于20的数，中间间隔每次+3
for i in range(1,20,3):
	print(i,end="");
print();

#python 的 for 循环嵌套
#乘法表的输出
for i in range(1,10):
	for j in range(1,i+1):
		print(i,"*",j,"=",i*j,end=" ");
		# print(f'{j}*{i}={i*j}',end="");
	print();
# 1*1=1 
# 1*2=2 2*2=4 
# 1*3=3 2*3=6 3*3=9 
# 1*4=4 2*4=8 3*4=12 4*4=16 
# 1*5=5 2*5=10 3*5=15 4*5=20 5*5=25 
# 1*6=6 2*6=12 3*6=18 4*6=24 5*6=30 6*6=36 
# 1*7=7 2*7=14 3*7=21 4*7=28 5*7=35 6*7=42 7*7=49 
# 1*8=8 2*8=16 3*8=24 4*8=32 5*8=40 6*8=48 7*8=56 8*8=64 
# 1*9=9 2*9=18 3*9=27 4*9=36 5*9=45 6*9=54 7*9=63 8*9=72 9*9=81 

# while 输出乘法口诀表
def init():
	print('断点打印')