nums = [2,7,11,15]
target = 9
d = {}
for i,j in enumerate(nums):
    r = target-j
    if r in d:
        print(d[r],i)
    d[j]=i