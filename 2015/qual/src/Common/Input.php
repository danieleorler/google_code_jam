<?php

namespace Dalen\GoogleCodeJam\Common;

/**
 * Description of Input
 *
 * @author danieleorler
 */
class Input
{
    private $numberOfTestCases;
    private $testCases;
    
    public function __construct()
    {
        $this->testCases = array();
    }

    public function addTestCase($testCase)
    {
        $this->testCases[] = $testCase;
    }
    
    public function getTestCases()
    {
        return $this->testCases;
    }
    
    public function getNumberOfTestCases()
    {
        return $this->numberOfTestCases;
    }
    
    public function setNumberOfTestCases($numberOfTestCases)
    {
        $this->numberOfTestCases = $numberOfTestCases;
        return $this;
    }
    
    public function toString()
    {
        $string = $this->getNumberOfTestCases().PHP_EOL;
        foreach($this->getTestCases() AS $testCase)
        {
            foreach($testCase AS $line)
            {
                $string .= $line.PHP_EOL;
            }
        }
        
        return $string;
    }
}
