def gen_primes(a, b):
    """ 
    Copied from stackoverflow
    Generate an infinite sequence of prime numbers.
    """
    D = {}
    q = a
    result = []
    while q <= b:
        if q not in D:
            result.append(q)
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]        
        q += 1
    return result

def solve(N, L, cyphered):
    pangram = [0] * (L+1)
    for i in range(0, L-1):
        for p in PRIMES:
            if cyphered[i] % p == 0 and cyphered[i+1] % p == 0:
                pangram[i+1] = p
                break

    pangram[0] = cyphered[0] / pangram[1]
    pangram[-1] = cyphered[-1] / pangram[-2]

    alphabet = sorted(set(pangram))
    d = {}
    ordinal = 65
    for letter in alphabet:
        d[letter] = chr(ordinal)
        ordinal = ordinal +1

    result = ""
    for j in pangram:
        result = result + d[j]

    return result

def run():
    n_tests = int(raw_input())
    for i in xrange(1, n_tests + 1):
        line1 = raw_input().split()
        N = int(line1[0])
        L = int(line1[1])
        primes = [int(x) for x in raw_input().split()]
        result = solve(N, L, primes)
        print "Case #%d: %s" % (i,result)

PRIMES = gen_primes(2, 10000)
run()

