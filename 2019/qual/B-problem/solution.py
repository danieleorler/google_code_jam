def solve(size, lydia):
    me = ""
    for step in lydia:
        if step == "E":
            me = me + "S"
        else:
            me = me + "E"
    return me

def run():
   n_tests = int(raw_input())
   for i in xrange(1, n_tests + 1):
       size = int(raw_input())
       lydia = raw_input()
       result = solve(size, lydia)
       print "Case #%d: %s" % (i,result)

run()
