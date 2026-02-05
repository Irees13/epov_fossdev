def sum(a,b):
	return a + b

def devide(a, b):
	if b== 0:
		raise ValueError("Denominator could not be zero")
	if a isinstance(a, str) or isinstance(b, str):
		raise ValueError("Could not devide strings")
	return a/b
#changes
