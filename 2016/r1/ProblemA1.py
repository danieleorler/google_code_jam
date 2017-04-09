
INPUT_FILE = 'test.in';
OUTPUT_FILE = 'file.out';

def s2i(s):
   return int(s or "0")

def algorithmA(N,P):
   print N
   print P
   print sum(P)

def solve(data):
   N = int(data[0])
   P = map(int,data[1].split())
   return str(algorithmA(N,P));

def run():
   with open(INPUT_FILE) as in_file:
      lines = in_file.readlines()

   n_tests = int(lines[0]);

   out_file = open(OUTPUT_FILE,'w')

   count = 1
   for i in range(2,len(lines),2):
      result = solve([lines[i-1].strip(),lines[i].strip()])
      string_result = "Case #%d: %s\n" % (count,result)
      out_file.write(string_result);
      print string_result
      count += 1

run()