
import math
import itertools

FILE_NAME = 'A-large';
INPUT_FILE = FILE_NAME+'.in';
OUTPUT_FILE = FILE_NAME+'.out';

def side(r, h):
   return 2*math.pi*r*h

def top(r):
   return (r**2) * math.pi

def area(stack):
   area = 0.0
   for i in range(0,len(stack)):
      area += stack[i][1]
      if(i < len(stack)-1):
         area += stack[i][0] - stack[i+1][0]
      else:
         area += stack[i][0]   

   return area

def algorithm(candidate, input):
   tmp = []
   for i in candidate:
      r = input[i][0]
      h = input[i][1]
      tmp.append([top(r),side(r,h)])

   tmp.sort(key=lambda e: e[0], reverse=True)
   # li = []
   # for t in input:
   #    r = int(t[0])
   #    h = int(t[1])
   #    ratio = float(h)/float(r)
   #    #li.append([r,h, top(r), side(r,h), top(r)+side(r,h)])
   #    li.append([r,h,ratio*top(r),top(r), side(r,h)])

   # li.sort(key=lambda e: (e[2], e[3]), reverse=True)

   # li = li[:int(dim[1])]

   # li.sort(key=lambda e: e[3], reverse=True)

   return area(tmp)

   # return li

def algorithm2(dim, input):
   max = 0.0
   for stack in itertools.combinations(range(0,int(dim[0])), int(dim[1])):
      area = algorithm(stack, input)
      if area > max:
         max = area

   return max

def solve(data):
   return str(algorithm2(data[0], data[1:]));

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
         input.append(map(int,a))
         lines_per_test = int(a[0])
         next_line += 1 
         for i in range(next_line, next_line + step(lines_per_test)):
            input.append(map(int,lines[i].split()))
            next_line += 1
      
      result = solve(input)
      string_result = "Case #%d: %s\n" % (count,result)
      out_file.write(string_result);
      print string_result
      count += 1

run(singleLine=False)

