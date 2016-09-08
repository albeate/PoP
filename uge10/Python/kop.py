class Kop(object):
	"""En klasse af kopper"""


	def __init__(self, val1="", val2=""):
		self.value = val1
		self.value2 = val2

	def __str__(self):
		return "En kop med " + self.value.__str__()	+ " og " + self.value2.__str__() 

	def get_val(self):
		return self.value

a = Kop('kaffe') 
print a

b = Kop('kage', 'rosiner') 
print b

e = Kop(val2='kage', val1='rosiner') 
print e

print a.get_val() + b.get_val()

c = Kop()
print c





