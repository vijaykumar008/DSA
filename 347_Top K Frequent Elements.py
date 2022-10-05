import collections
nums = [1,2,1,2,2,7]
k=2
print(dict(collections.Counter(nums).most_common(k)).keys())
