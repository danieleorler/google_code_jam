import sys

def print_no_buff(s):
   print s
   sys.stdout.flush()

def algorithm(a):
   completed = set([])
   if a == 10:
      path = set(["100 100", "100 101"])
   if a == 20:
      path = set(["100 100", "100 101", "99 100", "99 101", "98 100", "98 101"])
   current_pos = path.pop()
   
   while True:
      print_no_buff(current_pos)
      prepared = raw_input()
      if prepared == "0 0" or prepared == "-1 -1":
         break

      completed.add(prepared)
      if(len(completed) == 9):
         current_pos = path.pop()
         completed.clear()
      
   sys.stderr.write("\nfinished: " + str(prepared))

   if prepared == "-1 -1":
      raise Exception('Failed!')


T = input()
for _ in xrange(T):
   a = input()
   try:
      sys.stderr.write("\nTEST #"+str(_+1)+"\n")
      algorithm(a)
   except Exception as e:
      sys.stderr.write(str(e))
      sys.stderr.write("\nfailed\n")
      sys.exit();

