<?php

namespace Dalen\GoogleCodeJam\GCJ2015\InfiniteHouseOfPancakes;

/**
 * Description of InfiniteHouseOfPancakes
 *
 * @author danieleorler
 */
class InfiniteHouseOfPancakes
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
    
    function algorithm($input)
    {
        $max = max($input);
        if($max < 4)
        {
            return $max;
        }
        else
        {
            $log = log($max,2);
            if(floor($log) == $log)
            {
                return floor($log)+1;
            }
            else
            {
                return floor($log)+2;
            }
        }
    }
    
    private function cleanInput($string)
    {
        return explode(" ", $string);
    }
}
