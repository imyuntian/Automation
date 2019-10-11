# 模块和类库的小小理解
# 类库：先引入，再实例化，最后用类对象点方法 stu().stu_add()
# 模块：先引入，无需实例化，直接调用模块里的函数或者模块名点函数


"""================== 引用模块 ==================="""

'''
# 1 导入模块，用模块名调用函数
import time

print(time.ctime())
time.sleep(3)
print(time.ctime())

'''

# 2 导入函数，直接调用导入的函数
from time import sleep
from time import ctime

print(ctime())
sleep(3)
print(ctime())


