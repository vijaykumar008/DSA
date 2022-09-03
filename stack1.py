#Implementing Stack using collections

import collections

stack = collections.deque()
stack.append(10)
stack.append(20)

stack.pop()

not stack # To check stack is empty

print(stack)

#Implementing Stack using Queue

import queue
stack1 = queue.LifoQueue() #Method to implement Stack
stack1.put(10)
stack1.put(20)
stack1.put(30)

stack1.get() #To delete the element



