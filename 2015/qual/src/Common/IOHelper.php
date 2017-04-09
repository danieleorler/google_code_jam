<?php

namespace Dalen\GoogleCodeJam\Common;

/**
 * Description of InputParser
 *
 * @author danieleorler
 */
class IOHelper
{
    public static function readFile($fileName,$linePerTestCase)
    {
        $handle = fopen($fileName, "r");
        $idFirstLine = TRUE;
        $counter = 0;
        $input = new Input();
        $testCase = array();
        while(($line = fgets($handle)) !== false)
        {
            if($idFirstLine)
            {
                $input->setNumberOfTestCases($line);
                $idFirstLine = FALSE;
            }
            else
            {
                if($counter < $linePerTestCase)
                {
                    $testCase[] = $line;
                    $counter ++;
                }
                if($counter == $linePerTestCase)
                {
                    $input->addTestCase($testCase);
                    $testCase = array();
                    $counter = 0;
                    
                }
            }
        }
        fclose($handle);
        return $input;
    }
    
    public static function writeToFile($fileName,$results)
    {
        $handle = fopen($fileName, "w");
        
        for($i=0;$i<count($results);$i++)
        {
            $line = sprintf("Case #%d: %s".PHP_EOL,$i+1,$results[$i]);
            fwrite($handle, $line);
        }
        
        fclose($handle);
    }
}
