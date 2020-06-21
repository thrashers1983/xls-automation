import chapter8_modules         #引入一个模块，在这个模块中所定义的所有函数都能在这里使用
chapter8_modules.make_pizza(16, 'pepperoni')
chapter8_modules.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from chapter8_modules import make_pizza     #也可以从模块中单独引入函数，如果想引入多个函数，用逗号隔开
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from chapter8_modules import make_pizza as mp       #给函数起别名
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

import chapter8_modules as cm       #给模块起别名
cm.make_pizza(16, 'pepperoni')
cm.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from chapter8_modules import *      #这样引入的话，后面调用函数时就可以省掉模块名，这个写法不推荐
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#最推荐的是引入一个模块，然后用模块名.函数名来调用，或者如果只需要用到某一个或几个函数，就只引入那些函数
#模块名和函数名都要起有意义的名字，应该用小写字母和下划线，每个函数在函数定义下面用三引号写一下注释描述这个函数是用来干嘛的
#给参数默认值的时候，和调用函数要传参数的时候，等号两边不要有空格
#如果一个模块里有很多函数，每个函数之间空两行
#import写在程序的最开始位置
#定义函数的时候，如果有很多参数要写，则用这种格式：
# def function_name(
#         parameter_0, parameter_1, parameter_2,
#         parameter_3, parameter_4, parameter_5):
#     function body...
