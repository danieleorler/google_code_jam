
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


/**
 *
 * @author dalen
 */
public class ProblemD
{
    private static int nTests;
    public static void main(String[] args) throws FileNotFoundException
    {
        Scanner input = new Scanner(new File("dijkstra_test.in"));
        nTests = input.nextInt();
        for(int i=0;i<nTests;i++)
        {
            System.out.printf("Case #%d: %s\n",i+1,algorithm());
//            System.out.println(input.nextInt());
//            System.out.println(input.next());
        }
    }
    
    public static String algorithm()
    {
        return "a";
    }     
}
