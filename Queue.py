#Implementing Queue using List

queue = []
queue.append(10)
queue.append(20)
queue.append(30)


queue.pop(0)
queue.pop(0)


print(queue)

not queue #Empty queue check

#Implementing queue using Collections

import collections
q = collections.deque()
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)

q.pop()
q.pop()
print(q)

#One more method to implement queue

q = collections.deque()
q.append(10)
q.append(20)

q.popleft()
q.popleft()





