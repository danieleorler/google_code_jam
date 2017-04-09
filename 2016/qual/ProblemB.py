
INPUT_FILE = 'B-large.in';
OUTPUT_FILE = 'A-small-practice.out';

def algorithmA(stack):
   flips = 0
   if len(stack) > 1:
      for i in range(1,len(stack)):
         if stack[i] != stack[i-1]:
            flips += 1
   if stack[-1] == '-':
      flips += 1
   return flips

def solve(data):
   stack = list(data[0])
   return str(algorithmA(stack));

def run():
   with open(INPUT_FILE) as in_file:
      lines = in_file.readlines()

   n_tests = int(lines[0]);

   out_file = open(OUTPUT_FILE,'w')

   count = 1
   for i in range(1,len(lines)):
      result = solve([lines[i].strip(' \t\n\r')])
      string_result = "Case #%d: %s\n" % (count,result)
      out_file.write(string_result);
      print string_result
      count += 1

run()
