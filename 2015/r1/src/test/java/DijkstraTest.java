/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.util.ArrayList;
import java.util.Stack;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author danieleorler
 */
public class DijkstraTest {
    
    public DijkstraTest() {
    }
    
    @BeforeClass
    public static void setUpClass() {
    }
    
    @AfterClass
    public static void tearDownClass() {
    }
    
    @Before
    public void setUp()
    {
        Dijkstra.fillMatrix();
    }
    
    @After
    public void tearDown() {
    }

    /**
     * Test of multiply method, of class Dijkstra.
     */
    @Test
    public void testMultiply()
    {
        System.out.println("multiply");
        assertEquals("k", Dijkstra.multiply("i", "j"));
        assertEquals("k",Dijkstra.multiply("i","j"));
        assertEquals("-k",Dijkstra.multiply("i","-j"));
        assertEquals("k",Dijkstra.multiply("-i","-j"));
        assertEquals("k",Dijkstra.multiply("-i","-j"));
        assertEquals("-k",Dijkstra.multiply("-1","k"));
        assertEquals("1",Dijkstra.multiply("-1","-1"));
        assertEquals("-j",Dijkstra.multiply("j","-1"));
        assertEquals("-1",Dijkstra.multiply("k","k"));
        assertEquals("-k",Dijkstra.multiply("j","i"));
        assertEquals("i",Dijkstra.multiply("-k","j"));
    }
    
    @Test
    public void testReduce()
    {
        System.out.println("reduce");
        Stack<String> test = new Stack();
        
        System.out.println("ijk");
        test.push("k");test.push("j");test.push("i");
        assertEquals("-1", Dijkstra.reduce(test));
        System.out.println("jij");
        test = new Stack();test.push("j");test.push("i");test.push("j");
        assertEquals("i", Dijkstra.reduce(test));
        System.out.println("iji");
        test = new Stack();test.push("i");test.push("j");test.push("i");
        assertEquals("j", Dijkstra.reduce(test));
        System.out.println("jijiji");
        test = new Stack();test.push("i");test.push("j");test.push("i");test.push("j");test.push("i");test.push("j");
        assertEquals("k", Dijkstra.reduce(test));
    }
    
}
