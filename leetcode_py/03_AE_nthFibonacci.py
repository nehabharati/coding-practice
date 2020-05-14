# solution 1
def getNthFib(n):
    if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return getNthFib(n - 1) + getNthFib(n - 2)
    pass

#solution 2
def getNthFib(n,memoize = {1:0,2:1}):
    if n in memoize:
		return memoize[n]
	else:
		memoize[n] = getNthFib(n-1,memoize) + getNthFib(n-2,memoize) 
	return memoize[n]
    pass

#solution 3
def getNthFib(n):
    nums = [0, 1]
	count = 3
	while count <= n:
		new = nums[0] + nums[1]
		nums[0] = nums[1]
		nums[1] = new
		count += 1
	return nums[1] if n > 1 else nums[0]
    pass


