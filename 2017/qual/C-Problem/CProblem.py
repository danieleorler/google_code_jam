
FILE_NAME = 'C-large';
INPUT_FILE = FILE_NAME+'.in';
OUTPUT_FILE = FILE_NAME+'.out';

def algorithm(N, K):

   segments = [N]

   while K > 0:
      segments.sort(reverse=True)

      biggest_segment = segments[0]
      del segments[0]

      if(biggest_segment % 2 == 0):
         left = biggest_segment / 2 - 1
         right = biggest_segment / 2
      else:
         left = right = biggest_segment / 2

      segments.append(right)
      segments.append(left)
      K -= 1
   result = segments[-2:]
   return str(result[0]) + " " + str(result[1])

def solve(data):
   N = int(data[0])
   K = int(data[1])

   log2 = K.bit_length() - 1
   pow_log2 = 2**log2
   Kscaled = K/pow_log2
   Nscaled = N/pow_log2
   if N%pow_log2 < K%pow_log2:
      Nscaled -= 1

   return str(algorithm(Nscaled, Kscaled));

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


