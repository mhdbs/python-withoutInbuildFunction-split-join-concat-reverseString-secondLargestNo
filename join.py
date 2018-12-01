def custom_join(var, sep):
	''' assume var all of string type'''
	''' it works for list, tuple'''
	
	a = ''
	for elmnt in var[:-1]:
		a += elmnt + sep
	a+=var[-1]
	return a
a =  custom_join('hi', 'a')
print(a)