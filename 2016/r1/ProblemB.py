
INPUT_FILE = 'B-small-attempt1.in';
OUTPUT_FILE = 'file.out';

def s2i(s):
   return int(s or "0")

def algorithmA(c,j):
   my_c = ''
   my_j = ''
   for i in xrange(len(c)):
      if c[i] == '?' and j[i] == '?' and s2i(my_c) == s2i(my_j):
         if i < len(c)-1 and c[i+1] != '?' and j[i+1] != '?' and abs(int(c[i+1]) - int(j[i+1])) > 5:
            print 1
            my_c += '0'
            my_j += '1'
         else:
            print 2
            my_c += '0'
            my_j += '0'
         continue
      if c[i] == '?' and j[i] == '?' and s2i(my_c) > s2i(my_j):
         print 3
         my_c += '0'
         my_j += '9'
         continue
      if c[i] == '?' and j[i] == '?' and s2i(my_c) < s2i(my_j):
         print 4
         my_c += '9'
         my_j += '0'
         continue


      if c[i] != '?' and j[i] == '?' and s2i(my_c) == s2i(my_j):
         print 5
         my_c += c[i]
         my_j += c[i]
         continue
      if c[i] != '?' and j[i] == '?' and s2i(my_c) > s2i(my_j):
         print 6
         my_c += c[i]
         my_j += '9'
      if c[i] != '?' and j[i] == '?' and s2i(my_c) < s2i(my_j):
         print 7
         my_c += c[i]
         my_j += '0'
         continue

      if c[i] == '?' and j[i] != '?' and s2i(my_c) == s2i(my_j):
         print 8
         my_c += j[i]
         my_j += j[i]
         continue
      if c[i] == '?' and j[i] != '?' and s2i(my_c) > s2i(my_j):
         print 9
         my_c += '0'
         my_j += j[i]
         continue
      if c[i] == '?' and j[i] != '?' and s2i(my_c) < s2i(my_j):
         print 10
         my_c += '9'
         my_j += j[i]
         continue


      if c[i] != '?' and j[i] != '?':
         print 11
         my_c += c[i]
         my_j += j[i]
         continue
   return my_c + ' ' + my_j

def solve(data):
   c = data[0]
   j = data[1]
   return str(algorithmA(c,j));

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