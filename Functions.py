def pr (string, num):
  print(string, " " , num)
  pass

def summ (a,b):
  res = a+b
  return res

def test(*args):
  print (args)
  pass

pr ("number is: ", 56)
a = summ (23,56)
pr ("Number is: ", a)
test("Hello ", 23, 333, 54.3)

mult = lambda x,y: x*y
print (mult(12,5))