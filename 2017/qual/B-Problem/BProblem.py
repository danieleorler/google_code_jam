
FILE_NAME = 'B-large';
INPUT_FILE = FILE_NAME+'.in';
OUTPUT_FILE = FILE_NAME+'.out';

def isAsc(n):
   while n > 0:
      right = n%10
      n /= 10
      left = n%10
      if right < left:
         return False

   return True

def reduce(n):
   number = str(n)
   need_reduce = False
   last = ""
   to_reduce = "0"
   for digit in number:
      if digit < last:
         need_reduce = True
      if need_reduce:
         to_reduce += digit
      last = digit

   r = int(to_reduce)
   if r > 0:
      return r + 1
   return 0

def algorithm(N):
   if isAsc(N):
      return str(N)

   candidate = N - reduce(N)
   while not isAsc(candidate):
      candidate -= 1
      candidate -= reduce(candidate)
   return str(candidate)

def solve(data):
   N = int(data[0])

   return str(algorithm(N));

def run():
   with open(INPUT_FILE) as in_file:
      lines = in_file.readlines()

   n_tests = int(lines[0]);

   out_file = open(OUTPUT_FILE,'w')

   count = 1
   for i in range(1,len(lines)):
      result = solve(lines[i].split())
      string_result = "Case #%d: %s\n" % (count,result)
      out_file.write(string_result);
      print string_result
      count += 1

run()

