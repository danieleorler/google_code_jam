def trouble_sort(L):
   done = False
   while not done:
      done = True
      for i in xrange(0, len(L)-2):
         if L[i] > L[i+2]:
            done = False
            L[i:i+3] = L[i:i+3][::-1]
   return L

def algorithm(N, L):
   trouble = trouble_sort(list(L))
   sort = sorted(L)
   i = "OK"
   for index, (first, second) in enumerate(zip(trouble, sort)):
      if first != second:
         i = index
         break 
   #return str(i)+"\n"+str(trouble)+"\n"+str(sort)
   return i

def solve(data):
   N = int(data[0])
   L = map(int, data[1])
   return algorithm(N, L);

def run():
   n_tests = int(raw_input());
   for i in xrange(1, n_tests + 1):
      data = [raw_input(), raw_input().split()]
      result = solve(data)
      print "Case #%d: %s" % (i,result)

run()

