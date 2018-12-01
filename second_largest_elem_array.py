def secondLargest(arr):
	''' assume arr length > 2'''
	if arr[0]>arr[1]:
		first = arr[0]
		second = arr[1]
	else:
		first = arr[1]
		second = arr[0]
	for elmnt in arr[2:]:
		if elmnt > first:
			second = first
			first = elmnt
		elif elmnt > second:
			second = elmnt
	return second
a = secondLargest([1,5,7,8,9,3,2])
print(a)