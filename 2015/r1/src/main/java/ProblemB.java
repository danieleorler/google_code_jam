
import java.io.File;
import java.io.FileNotFoundException;
import java.math.BigInteger;
import java.util.Scanner;

/**
 *
 * @author dalen
 */
public class ProblemB
{
    private static long nTests;
    public static void main(String[] args) throws FileNotFoundException
    {
        
        Scanner input = new Scanner(new File("B-large-practice.in"));
        nTests = input.nextInt();
        for(int i=0;i<nTests;i++)
        {
            long startTime = System.currentTimeMillis();
            int nB = input.nextInt();
            int N = input.nextInt();
            long[] b = new long[nB];
            for(int index=0;index<nB;index++)
            {
                b[index] = input.nextBigInteger().longValue();
            }
            System.out.printf("Case #%d: %s\n",i+1,solve(b,N)+1);
            long endTime = System.currentTimeMillis();
            long duration = (endTime - startTime);
            System.out.printf("Time: %d ms:\n",duration);
        }
        
    }
    
    public static long solve(long[] b, long N)
    {
        if(N <= b.length)
        {
            return N-1;
        }
        
        long min = min(b);
        long max = max(b);
        
        
        if(max-min == 0)
        {
            if((N%b.length) == 0)
                return b.length-1;
            else
                return (N%b.length)-1;
        }
        
        BigInteger lcm = lcm(b);
        long sum = 0;
        for(int i=0;i<b.length;i++)
        {
            sum += lcm.divide(BigInteger.valueOf(b[i])).longValue();
        }
        
        long Nc = N;
        
        while(Nc > sum)
        {
            Nc -= sum;
        }
        
        return algorithm(b, Nc);
        
    }
    
    public static long algorithm(long[] b, long N)
    {
        long[] w = new long[b.length];
        for(int i=0;i<w.length;i++)
        {
            w[i] = 0;
        }
        //System.arraycopy(b, 0, w, 0, b.length);
        
        long my = 1;
        while(my <= N)
        {
//            for(long l=0; l<w.length; l++)
//            {
//                System.out.print(w[l]+" ");
//            }
//            System.out.println();
//            System.out.print("[ ");
            long minB = min(w);
            for(int j=0; j<w.length; j++)
            {
                if(w[j] < 2)
                {
                    if(my == N)
                    {
//                        System.out.println(my+" ]");
                        return j;
                    }
                    else
                    {
                        w[j] = b[j];
//                        System.out.print(my+", ");
                        my++;
                    }
                }
                else
                {
                    w[j] -= 1;
                }
            }
//            System.out.println(" ]");
        }
        return -1;
    }
    
    private static long min(long[] b)
    {
        long min = b[0];
        for(int i=0;i<b.length;i++)
        {
            if(b[i] < min)
            {
                min = b[i];
            }
        }
        return min;
    }
    
    private static long max(long[] b)
    {
        long max = 0;
        for(int i=0;i<b.length;i++)
        {
            if(b[i] > max)
            {
                max = b[i];
            }
        }
        return max;
    }
    
    private static BigInteger gcd(BigInteger a, BigInteger b)
    {
        while (b.signum() == 1)
        {
            BigInteger temp = b;
            b = a.mod(b); // % is remainder
            a = temp;
        }
        return a;
    }
    
    private static BigInteger gcd(long[] input)
    {
        BigInteger result = BigInteger.valueOf(input[0]);
        for(int i = 1; i < input.length; i++) result = gcd(result, BigInteger.valueOf(input[i]));
        return result;
    }

    private static BigInteger lcm(BigInteger a, BigInteger b)
    {
        return a.multiply((b.divide(gcd(a, b))));
    }
    
    private static BigInteger lcm(long[] input)
    {
        BigInteger result = BigInteger.valueOf(input[0]);
        for(int i = 1; i < input.length; i++)
            result = lcm(result, BigInteger.valueOf(input[i]));
        return result;
    }
}
