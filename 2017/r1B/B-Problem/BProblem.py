import itertools


FILE_NAME = 'practice';
INPUT_FILE = FILE_NAME+'.in';
OUTPUT_FILE = FILE_NAME+'.out';

manes = {
   "O": ["R", "Y"],
   "G": ["Y", "B"],
   "V": ["R", "B"]
}

colours = ["R", "O", "Y", "G", "B", "V"]

def is_correct(possible):
   last = len(possible) - 1
   for i in range(0,len(possible)):
      if i == 0:
         if possible[last] == possible[i] or possible[i+1] == possible[i]:
            return False
      elif i == last:
         if possible[0] == possible[last] or possible[last-1] == possible[last]:
            return False
      else:
         if possible[i-1] == possible[i] or possible[i+1] == possible[i]:
            return False

   return True

def algorithm(input):
   ponies = []
   #m = min(input[1:]) - 1
   no_zero = [x for x in input[1:] if x != '0']
   m = int(min(no_zero)) - 1
   for i in range(1,len(input)):
      for j in range(0,int(input[i])-m):
         ponies.append(colours[i-1])

   all = list(itertools.permutations(ponies))

   for possible in all:
      if is_correct(list(possible)):
         return "".join(possible)

   return "IMPOSSIBLE"

def solve(data):
   S = data[0]
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

run()

print 
