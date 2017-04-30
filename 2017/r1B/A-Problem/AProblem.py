
FILE_NAME = 'A-large';
INPUT_FILE = FILE_NAME+'.in';
OUTPUT_FILE = FILE_NAME+'.out';

def algorithm(input):
   D = float(input[0][0])
   ETAs = []
   for i in range(1,len(input)):
      K = float(input[i][0])
      S = float(input[i][1])
      ETA = (D-K)/S
      ETAs.append(ETA)

   return str(D/max(ETAs))

def solve(data):
   S = data
   return str(algorithm(S));

def run(singleLine=True, step=lambda x: x):
   with open(INPUT_FILE) as in_file:
      lines = in_file.readlines()
   n_tests = int(lines[0]);
   out_file = open(OUTPUT_FILE,'w')

   count = 1
   next_line = 1
   
   while count <= n_tests:
      input = []

      if singleLine:
         input.append(lines[count].split())
      else:
         a = lines[next_line].split()
         lines_per_test = int(a[1]) + 1
         for i in range(next_line, next_line + step(lines_per_test)):
            input.append(lines[i].split())
            next_line += 1
      
      result = solve(input)
      string_result = "Case #%d: %s\n" % (count,result)
      out_file.write(string_result);
      print string_result
      count += 1

run(singleLine=False)


