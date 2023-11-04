# __new__ 实例化对象，传入的参数为cls，有返回值，new一个object并返回
# __init__ 初始化对象的属性，传入的参数为self,没有返回值

class A:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        pass


# __del__ 方法 ： 当对象释放的时候调用
class B:
    def __del__(self):
        print("__del__")


# o = B()
# x = o
# del o
# print("finish")

# 代码打印结果
# finish
# __del__
# 也就是说del(o)的时候并没有调用B对象的__del__方法，而是程序执行结束的时候调用的
# ==================================================================


# __repr__  打印对象
# __str__   打印对象，优先级比__repr__更高
# __format__ 格式化输出方法
# __bytes__  使用bytes()时调用
class C:
    def __repr__(self):
        print("repr")

    def __str__(self):
        print("str")

    def __format__(self, format_spec):
        if format_spec == "x":
            return "oxC"
        return "C"


# __eq__: 比较方法，==
# __ne__: 比较方法, !=
# __gt__: >
# __lt__: <
# __ge__: >=
# __le__: <=

class Date:
    def __init__(self, year, month, date):
        self.year = year
        self.month = month
        self.date = date

    def __eq__(self, other):
        print("__eq__")
        return self.date == other.date and self.month == other.month and self.year == other.year

    def __ne__(self, other):
        print("__ne__")
        return self.date != other.date or self.month != other.month or self.year != other.year

    def __gt__(self, other):
        print("Date:__gt__")
        if self.year > other.year:
            return True
        elif self.year == other.year:
            if self.month > other.month:
                return True
            elif self.month == other.month:
                return self.date > other.date
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        print("Date:__lt__")
        if self.year < other.year:
            return True
        elif self.year == other.year:
            if self.month < other.month:
                return True
            elif self.month == other.month:
                return self.date < other.date
            else:
                return False
        else:
            return False


# x = Date(2023, 11, 1)
# y = Date(2023, 11, 2)
# print(x == y)
# print(x != y)

class NewDate(Date):
    pass


# 如果对两个不同的类实例做比较时，如果y是x的衍生类时，优先使用y的表达式方法，否则使用运算符号左边的类对象的表达式方法
# y = NewDate(2023, 11, 4)
y = Date(2023, 11, 4)
x = Date(2023, 11, 4)
print(x > y)


# __getattr__ : 当对象获取的属性不存在的时候，会调用
# __getattribute__ : 当获取对象属性的时候就会调用 getattr(o,key)
# __setattr__ : 给对象新增一个属性时会调用 setattr(o,key,value)
# __delattr__ : 删除对象的一个属性时调用 del(o.key)
class D:
    def __init__(self):
        self.exist = "exist"
        self.count = 0

    def __getattr__(self, item):
        print(f"D:__getattr__:{item}")
        return

    def __getattribute__(self, item):
        if item == "data":
            self.count += 1
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        print(f"set {key}: {value}")
        super().__setattr__(key, value)

    def __delattr__(self, item):
        print(f"del {item}")
        super().__delattr__(item)


d = D()
print(d.exist)
print(d.test)
print(getattr(d, "data"))
print(d.count)
setattr(d, "count", 10)
print(d.count)
print(d.test)
del d.count
print(d.count)

# __dir__() :  返回对象内部的属性及方法
for i in dir(d):
    print(i, type(i))


# __init_subclass__() :以当前类为基类定义一个衍生类的时候会被调用，传入的参数cls就是衍生类
#

class Base:
    def __init_subclass__(cls, name):
        cls.x = {}
        cls.name = name


class A(Base, name="huas"):
    pass


print(A.x)
print(A.name)


# __class_getitem__()
class E:
    def __class_getitem__(cls, item):
        print(f"E:{item}")
        return "E"


print(E[0])


# __prepare__(): 准备构建class的命名空间的
# __instancecheck__(): 使用isinstance()时调用
# __subclasscheck__(): 使用issubclass()时调用
class meta(type):
    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        print(name, bases, kwargs)
        return {"a": 10}

    def __instancecheck__(self, instance):
        print("instance check")
        return True

    def __subclasscheck__(self, subclass):
        print("subclass check")
        return True


class F(metaclass=meta):
    b = 20
    c = 30


print(F.a, F.b)
print(isinstance(123, F), issubclass(int, F))


# 运算符重载
# __add__(): 两个对象 +
# __sub__(): -
# __mul__(): *
# __matmul__(): @
# __truediv__(): /
# __floordiv__(): //
# __mod__(): %
# __divmod__(): 返回商和余数
#              >> divmod(7,3)
#              >> (2,1)
# __pow__ v1 ** v2 v1的v2次方
# __lshift__(): 位运算，左移
# __rshift__()： 位运算，右移
# __and__(): 与 &
# __xor__(): 异或 ^
# __or__(): 或  |


class Vector:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


vector1 = Vector(1, 2)
vector2 = Vector(3, 4)
print(vector1 + vector2)


# __neg__():  -
# __pos__():  +
# __abs__():  取绝对值
# __invert__(): 一般用来位运算 取反
# __complex__(): 复数
# __int__(): 类型转换 int()
# __float__(): 类型转换 float()

# 取整
# __round__():  四舍五入
# __trunc__():  向下取整
# __floor__():  向负取整
# __ceil__()： 向上取整


# __call__(): 对象作为函数调用时使用

class M:
    def __init__(self, mul):
        self.mul = mul

    def __call__(self, *args, **kwargs):
        return self.mul * args[0]


m = M(3)
print(m(4))


# __getitem__(): 使用[]取值的时候调用
# __setitem__(): 使用[]赋值的时候调用
# __delitem__(): 使用del l[0]时调用
# __reversed__(): 倒序返回
# __contains__(): 使用in 时调用
class L:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        self.data = self.data[:key] + self.data[key+1:]

    def __reversed__(self):
        return L(self.data[::-1])


ll = L([1, 2, 3, ])
print(ll[0])
ll[0] = 3
print(ll[0])


# context
# __enter__():  定义上下文管理器，进入时调用
# __exit__(): 定下上下文管理器， 退出时调用
