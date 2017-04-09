

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;
import java.util.Stack;

/**
 *
 * @author danieleorler
 */
public class Dijkstra
{
    private static HashMap<String,HashMap> matrix = new HashMap<>();
    private static int nTests;
    
    public static void fillMatrix()
    {
        HashMap<String,String> row1 = new HashMap<>();
        row1.put("1", "1");row1.put("i", "i");row1.put("j", "j");row1.put("k", "k");
        matrix.put("1", row1);
        HashMap<String,String> rowI = new HashMap<>();
        rowI.put("1", "i");rowI.put("i", "-1");rowI.put("j", "k");rowI.put("k", "-j");
        matrix.put("i", rowI);
        HashMap<String,String> rowJ = new HashMap<>();
        rowJ.put("1", "j");rowJ.put("i", "-k");rowJ.put("j", "-1");rowJ.put("k", "i");
        matrix.put("j", rowJ);
        HashMap<String,String> rowK = new HashMap<>();
        rowK.put("1", "k");rowK.put("i", "j");rowK.put("j", "-i");rowK.put("k", "-1");
        matrix.put("k", rowK);
    }
    
    public static String multiply(String a, String b)
    {
        Boolean isNegative = false;
        
        if(a.length() + b.length() == 3)
        {
            isNegative = true;
        }
        
        a = a.substring(a.length()-1);
        b = b.substring(b.length()-1);
        
        String result = (String) matrix.get(a).get(b);
        
        if(isNegative && result.length() == 2)
        {
            return result.substring(result.length()-1);
        }
        else if(isNegative && result.length() == 1)
        {
            return "-"+result.substring(result.length()-1);
        }
        else
        {
            return result;
        }
    }
    
    public static String reduce(Stack<String> quaternions)
    {
        if(quaternions.size() == 1)
        {
            return quaternions.peek();
        }
        String reduced = multiply(quaternions.pop(),quaternions.pop());
        quaternions.push(reduced);
        return reduce(quaternions);
    }
    
    public static void main(String[] args) throws FileNotFoundException
    {
        fillMatrix();
        Scanner input = new Scanner(new File("dijkstra_test.in"));
        nTests = input.nextInt();
        for(int i=0;i<nTests;i++)
        {
            int a = input.nextInt();
            int b = input.nextInt();
            String c = input.next();
            String repeated = new String(new char[b]).replace("\0", c);
            
            for(int j=1; j<=repeated.length()-2; j++)
            {
                String tmp = repeated.substring(0, j);
                Stack<String> stack = new Stack();
                for(int t=tmp.length()-1; t>=0; t--)
                {
                    stack.push(""+tmp.charAt(t));
                }
                if(reduce(stack).compareTo("i") == 0)
                {
                    for(int x=j+2;x<=repeated.length()-2;x++)
                    {
                        String tmp2 = repeated.substring(j+1, x);
                        Stack<String> stack2 = new Stack();
                        for(int t=tmp2.length()-1; t>=0; t--)
                        {
                            stack2.push(""+tmp2.charAt(t));
                        }
                        if(reduce(stack2).compareTo("j") == 0)
                        {
                            String tmp3 = repeated.substring(x+1, repeated.length()-1);
                            Stack<String> stack3 = new Stack();
                            for(int t=tmp3.length()-1; t>=0; t--)
                            {
                                stack3.push(""+tmp3.charAt(t));
                            }
                            if(reduce(stack3).compareTo("k") == 0)
                            {
                                System.out.println("TRUE");
                            }
                        }
                    }
                }
            }
            
            //System.out.printf("Case #%d: %s\n",i+1,"");
        }
    }
    
}
