def twoSum( nums , target ) :
    num = {}
    for i, v in enumerate(nums):
        remaining = target - v
        if remaining in num:
            print([num[remaining], i])
            return [num[remaining], i]
        num[v] = i
    return []
