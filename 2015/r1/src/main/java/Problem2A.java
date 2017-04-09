
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


/**
 *
 * @author dalen
 */
public class Problem2A
{
    private static int nTests;
    public static void main(String[] args) throws FileNotFoundException
    {
//        Scanner input = new Scanner(new File("A-small-practice.in"));
//        nTests = input.nextInt();
//        for(int i=0;i<nTests;i++)
//        {
//            int nlook = input.nextInt();
//            
//            System.out.printf("Case #%d: %d\n",i+1,algorithm(nlook));
//        }
        System.out.printf("Case #100: %d\n",algorithm(350));
    }
    
    public static int algorithm(int N)
    {
        if(N < 21)
        {
            return N;
        }
        
        if(N >=22 && N <= 99)
        {
            return 10 + ((int)Math.floor(N/10)) + N%10;
        }
        
        if(N >= 100 && N <= 999)
        {
            return 29 + (((int)Math.floor(N/100))-1)*3 + (N%100)/(((int)Math.floor(N/100))-1);
        }
        
        int length = (int)(Math.log10(N));
        int count = 0;
        if(length < 2)
        {
            count = 0;
        }
        else if(length == 2)
        {
            count = 19+10;
        }
        else
        {
            count += 19+10;
            
            for(int i=2; i<length; i++)
            {
                count += Math.pow(10, i)+9;
            }
        }
        
        length = (int)(Math.log10(N)+1);
        
        String sn = N+"";
        int lastN = Integer.parseInt(sn.substring(0, (int) Math.floor(length/2)));
        int reversedLastN = reverse(lastN);
        count += reversedLastN;
        int tillNow = reverse((int) (Math.pow(10, length-1) + reversedLastN));
        count += N - tillNow;
        count ++;
        
        return count;
    }
    
    public static int reverse(int input)
    {
        int reversedNum = 0;
        while (input != 0)
        {
            reversedNum = reversedNum * 10 + input % 10;
            input = input / 10;   
        }
        
        return reversedNum;
    }
}
