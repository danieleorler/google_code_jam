
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.URL;
import java.util.Scanner;
import javax.xml.transform.stream.StreamSource;


/**
 *
 * @author dalen
 */
public class ProblemA
{
    private static int nTests;
    public static void main(String[] args) throws FileNotFoundException, IOException
    {
        URL url =  Thread.currentThread().getContextClassLoader().getResource("A-small-practice.in");
        Scanner input = new Scanner(url.openStream());
        nTests = input.nextInt();
        for(int i=0;i<nTests;i++)
        {
            int nlook = input.nextInt();
            int[] looks = new int[nlook];
            for(int index=0;index<nlook;index++)
            {
                looks[index] = input.nextInt();
            }
            
            System.out.printf("Case #%d: %d %d\n",i+1,algorithmA(looks),algorithmB(looks));
        }
    }
    
    public static int algorithmA(int[] looks)
    {
        int result = 0;
        for(int i=0;i<looks.length-1;i++)
        {
            if(looks[i] - looks[i+1] > 0)
            {
                result += looks[i] - looks[i+1];
            }
        }
        return result;
    }
    
    public static int algorithmB(int[] looks)
    {
        int result = 0;
        int remaining = looks[0];
        int maxdiff = 0;
        
        for(int i=0;i<looks.length-1;i++)
        {
            if(looks[i]-looks[i+1] > maxdiff)
            {
                maxdiff = looks[i]-looks[i+1];
            }
        }
        for(int i=0;i<looks.length-1;i++)
        {
            if(looks[i]<maxdiff)
            {
                result += looks[i];
            }
            else
            {
                result += maxdiff;
            }
        }
        return result;
    }
}
