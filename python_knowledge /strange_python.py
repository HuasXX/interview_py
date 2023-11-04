import dis
import sys

print(sys.getsizeof([0] * 3))  # >> 80
print(sys.getsizeof([0, 0, 0]))  # >> 120
print(sys.getsizeof([0 for _ in range(3)]))  # >>88

dis.dis("[0] * 3")
dis.dis("[0,0,0]")
dis.dis("[0 for _ in range(3)]")


# =====
# strange params when default value is mutable
class Tool:
    def __init__(self, name, items=[]):
        self.name = name
        self.items = items


r1 = Tool("box_1")
r2 = Tool("box_2")
r3 = Tool("box_3", items=["candy"])

r1.items.append("sugar")
r2.items.append("ice cream")

print(r1.items)  # >>['sugar', 'ice cream']
print(r2.items)  # >> ['sugar', 'ice cream']
print(r3.items)  # >> ['candy']


# use None replace mutable
class Tool:
    def __init__(self, name, items=None):
        self.name = name
        if items is None:
            self.items = []
        else:
            self.items = items


# python pep289
# https://peps.python.org/pep-0289/

lst = [1, 2, 3, 4, 5]
g = (i for i in lst if i in lst)
lst = [0, 1, 2]
print(list(g))  # >> [1,2]


class C:
    def f(self):
        pass


o = C()
a = id(o.f)
print(a)  # >> 4409594432
b = id(o.f)
print(a, b)  # >> 4409594432 4409594432



