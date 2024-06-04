class mynumber:
    def __iter__(self):
      self.a = 2
      return self
    
    def __next__(self):
      x = self.a
      self.a += 2 # this will add +2 every time the next protocol is being called
      return x
    
myclass = mynumber()
myiter = iter(myclass)

# for x in myiter:
#    print(x)
# this will create an infinite loop as there is no limit to which the next function can be called 

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# in this case we are calling next condition 5 times giving us output - 2,4,6,8,10