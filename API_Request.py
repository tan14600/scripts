def myfunc(n):
  b = lambda a : a * n
#   print ("b = ", b)
  return b

mydoubler = myfunc(2)

print(mydoubler(22))