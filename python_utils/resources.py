import time as _time
from functools import wraps

__doc__ = """Provides tools that help you to know
how many system resources are used from a piece of code
(i.e. a function).

time(function) tells you how much time the function spend to
return its value. It can be used as a decorator too """

def time(func):
	@wraps(func)
	def wrapper(*args,**kwargs):
		t2 = func(*args,**kwargs)
		print(_time.time() - t)
		return t2
	t = _time.time()
	return wrapper
