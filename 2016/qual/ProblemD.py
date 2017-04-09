
import itertools

INPUT_FILE = 'test.in';
OUTPUT_FILE = 'A-small-practice.out';

def algorithmA(tails,complexity,students):
   originals = map(list, itertools.product(['L', 'G'], repeat=tails))

   print tails,complexity,students
   fractals = []
   for original in originals:
      f = fractal(''.join(original),complexity)
      fractals.append(f)
      print original, f

   howmany = 0
   for ef in fractals:
      if ef[3] == 'L' and ef[6] == 'L':
         howmany += 1
   print howmany

def solve(data):
   args = map(int,data[0].split())
   return str(algorithmA(args[0],args[1],args[2]));

def fractal(original, C):
   l = list(original)
   f = original
   for i in range(1,C):
      f = ''
      for tile in l:
         if tile == 'G':
            f += 'G' * len(original)
         else:
            f += original
      l = list(f)
   return f

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
