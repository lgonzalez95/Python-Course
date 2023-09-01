# In python the method resolution order is: Depth first - Left to right

class A:
    def show(self):
        print('Show')


class B(A):
    pass


class C(B):
    pass


class D(C, A):
    pass


c = C()
c.show()
print(C.mro())
print(D.mro())
