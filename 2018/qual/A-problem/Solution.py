from collections import Counter

def total_damage(P):
   damage = 1
   total = 0
   for instruction in P:
      if instruction == "C":
         damage *= 2
      else:
         total += damage
   return total 

def hack(P):
   list = P.rsplit("CS", 1)
   return "SC".join(list)


def algorithm(D, P):
   freq = Counter(P)

   if freq["S"] > D:
      return "IMPOSSIBLE"
   if not "S" in freq.keys():
      return 0
   if total_damage(P) <= D:
      return 0
   
   count = 0
   while(total_damage(P) > D):
      P = hack(P)
      count += 1

   return count

def solve(data):
   D = int(data[0])
   P = data[1].rstrip("C")
   return algorithm(D, P);

def run():
   n_tests = int(raw_input());
   for i in xrange(1, n_tests + 1):
      result = solve(raw_input().split())
      print "Case #%d: %s" % (i,result)

run()

