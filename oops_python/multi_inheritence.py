
class A:
	def __init__(self):
		print("init of A", self)

class B:
	def __init__(self):
		print("init of B")

class C(A, B):
	def __init__(self):
		print("init of C")
		# super(C, self).__init__()
		A.__init__(self)
		B.__init__(self)




c = C()

a = A()

print(C.mro())
