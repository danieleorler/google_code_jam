import math

def solve(data):
   N = data[0]
   digits = len(N)
   a = ""
   indexes = [0] * digits
   for i in range(0, digits):
      d = int(N[i])
      if d == 4:
         a = a + str(3)
         indexes[digits-1-i] = 1
      else:
         a = a + str(d)

   b = 0
   for i in range(0,len(indexes)):
      if indexes[i] != 0:
         b = b + int(math.pow(10,i))
   return "{} {}".format(a , str(b))

def run():
   n_tests = int(raw_input())
   for i in xrange(1, n_tests + 1):
      result = solve(raw_input().split())
      print "Case #%d: %s" % (i,result)

run()

