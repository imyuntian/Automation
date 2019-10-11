import sys
sys.path.append("./model") # 将model目录添加到系统环境变量path下

from model import new_count

test = new_count.B() # 模块名.类，然后实例化，赋值给test
print(test.add(2, 5))       # test是类的实例化对象


