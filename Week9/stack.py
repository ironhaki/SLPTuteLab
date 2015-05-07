'''
 
1. Modify the stack class in the lecture notes to make a queue class. Name it "queue". 
 
2. Create a class named "Quack", which implements a hybrid queue/stack. It has three methods: 
push() which pushes something to the end, pop_end() which pops the value from the end 
(stack-fashion) and pop_start(), which pops from the start (queue-fashion). 
 
3. Modify your class from last question to include docstrings and a simple doctest for each of 
the methods you've written. 
 
4. Test sample programs in this week's lecture

'''
class queue(object):
  "A class implementing a stack data structure."
  def __init__(self):
    self.thestack = []
  def push(self, a):
    "Push a value to the top of the stack."
    self.thestack.append(a)
  def pop(self):
    "Remove the top element from stack and return it."
    return self.thestack.pop()

class Quack(queue):

	def __init__(self, list_a):
		self.thestack = list_a
	def pop_start(self, object):
		self.thestack.insert(0, object)

###############################
list_a = ['luffy', 'zoro', 'sanji', 'law']
q = Quack(list_a)
print q.thestack
q.pop()
print q.thestack
q.push('nami')
print q.thestack
q.pop_start('one piece')
print q.thestack