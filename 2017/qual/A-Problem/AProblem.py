
FILE_NAME = 'A-large';
INPUT_FILE = FILE_NAME+'.in';
OUTPUT_FILE = FILE_NAME+'.out';

def flip(S, K):
   string = list(S)
   index = S.find("-")
   if index > -1:
      for i in range(index, index+K):
         if string[i] == "-":
            string[i] = '+'
         else:
            string[i] = "-"
   return "".join(string)

def algorithm(S, K):
   try:
      flips = 0
      while S != len(S) * "+":
         S = flip(S, K)
         flips += 1
      return str(flips)
   except Exception as e:
      return "IMPOSSIBLE"

def solve(data):
   S = data[0]
   K = int(data[1])
   return str(algorithm(S, K));

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

