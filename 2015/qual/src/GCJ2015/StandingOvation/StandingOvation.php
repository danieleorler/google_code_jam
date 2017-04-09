<?php

namespace Dalen\GoogleCodeJam\GCJ2015\StandingOvation;

use Dalen\GoogleCodeJam\Common\Input;

/**
 * Description of StandingOvation
 *
 * @author danieleorler
 */
class StandingOvation
{
    private $input;
    
    function getInput()
    {
        return $this->input;
    }

    function setInput($input)
    {
        $this->input = $input;
        return $this;
    }
        
    public function howManyFriends($shynessArray)
    {
        if(count($shynessArray) == 1 && $shynessArray[0] == 0)
        {
            return 1;
        }
        
        $standing = $shynessArray[0];
        $friends = 0;
        
        for($i=1;$i<count($shynessArray);$i++)
        {
            if($standing < $i)
            {
                $friendsToCall = $i - $standing;
                $friends += $friendsToCall;
                $standing += ($friendsToCall + $shynessArray[$i]);
            }
            else
            {
                $standing += $shynessArray[$i];
            }
        }
        
        return $friends;
    }
    
    public function runAlgorithm()
    {
        $results = array();
        
        $testCases = $this->input->getTestCases();
        
        for($i=0; $i<$this->input->getNumberOfTestCases(); $i++)
        {
            $inputString = $this->cleanInput($testCases[$i][0]);
            $result = $this->howManyFriends($inputString);
            $results[] = $result;
        }
        
        return $results;
    }
    
    private function cleanInput($string)
    {
        $tokens = explode(" ", $string);
        return str_split($tokens[1]);
    }
}
