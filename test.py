class A:
    var1 = 10

    def __init__(self, obj_b):
        self.b = obj_b
        obj_b.a = self

    def change_var(self):
        print("ppppppp")


class B:
    var2 = 13

    def look_for_func(self):
        pass


b = B()
a = A(b)

b.look_for_func()
