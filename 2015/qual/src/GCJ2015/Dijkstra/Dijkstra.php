<?php

namespace Dalen\GoogleCodeJam\GCJ2015\Dijkstra;

/**
 * Description of Dijkstra
 *
 * @author danieleorler
 */
class Dijkstra
{
    private $matrix;
    private $input;
    private $cache;
    
    public function __construct()
    {
        $this->matrix = array
        (
            "1" => array("1"=>"1","i"=>"i","j"=>"j","k"=>"k"),
            "i" => array("1"=>"i","i"=>"-1","j"=>"k","k"=>"-j"),
            "j" => array("1"=>"j","i"=>"-k","j"=>"-1","k"=>"i"),
            "k" => array("1"=>"k","i"=>"j","j"=>"-i","k"=>"-1"),
        );
        
        $this->cache = array();
    }
    
    function getInput()
    {
        return $this->input;
    }

    function setInput($input)
    {
        $this->input = $input;
        return $this;
    }
    
    public function multiply($a,$b)
    {
        $isNegative = FALSE;
        
        if(strlen($a) + strlen($b) == 3)
        {
            $isNegative = TRUE;
        }
        
        $a = substr($a, -1);
        $b = substr($b, -1);
        
        $result = $this->matrix[$a][$b];
        
        if($isNegative && strlen($result) == 2)
        {
            return substr($result, -1);
        }
        elseif($isNegative && strlen($result) == 1)
        {
            return "-".substr($result, -1);
        }
        else
        {
            return $result;
        }
    }
    
    public function reduce($quaternions,$isFirstCall)
    {
        if($isFirstCall)
        {
            $quaternions = array_reverse($quaternions);
        }
        
        if(count($quaternions) == 1)
        {
            return $quaternions[0];
        }
        $newQuaternion = $this->multiply(array_pop($quaternions),array_pop($quaternions));
        $quaternions[] = $newQuaternion;
        return $this->reduce($quaternions,FALSE);
    }
    
    public function algorithm($input)
    {
        $time_start = microtime(true);
        $a = array();
        $b = array();
        $c = array();
        $length = count($input);
        if($length < 3)
        {
            return "NO";
        }
        
        for($i=1;$i<=$length-2;$i++)
        {
            $a = array_slice($input, 0, $i);
            
            $reducedA = $this->getReduced($a);
            if($reducedA === "i")
            {
                for($j=1;$j<=$length-$i-1;$j++)
                {
                    
                    $b = array_slice($input, $i, $j);
                    $reducedB = $this->getReduced($b);
                    
                    if($reducedB === "j")
                    {
                        $c = array_slice($input, $i+$j, $length-($i+$j));
                        $reducedC = $this->getReduced($c);
                        if($reducedC === "k")
                        {
                            $time_end = microtime(true);
                            $execution_time = ($time_end - $time_start);
                            echo($execution_time.PHP_EOL);
                            return "YES";
                        }
                    }
                }
            }
        }
        $time_end = microtime(true);
        $execution_time = ($time_end - $time_start);
        echo($execution_time.PHP_EOL);
        return "NO";
    }
    
    public function runAlgorithm()
    {
        $results = array();
        
        $testCases = $this->input->getTestCases();
        
        for($i=0; $i<$this->input->getNumberOfTestCases(); $i++)
        {
            $input = $this->cleanInput($testCases[$i][0],$testCases[$i][1]);
            if($input)
            {
                $time_start = microtime(true);
                $result = $this->algorithm($input);
                $time_end = microtime(true);
                $execution_time = ($time_end - $time_start);
                echo($execution_time.PHP_EOL);
                $results[] = $result;
            }
            else
            {
                $results[] = "NO";
            }
        }
        
        return $results;
    }
    
    private function cleanInput($line1,$line2)
    {
        $inputLine1 = rtrim(ltrim($line1));
        $inputLine2 = rtrim(ltrim($line2));
        $compressed = preg_replace('/(.)\1+/u', '$1', $inputLine2);
        if(strlen($compressed) == 1)
        {
            return FALSE;
        }
        else
        {
            $tokens = explode(" ", $inputLine1);
            $string = str_repeat($inputLine2, $tokens[1]);
            return str_split($string);
        }
    }
    
    private function implode($array)
    {
        $string = "";
        for($i=0;$i<count($array);$i++)
        {
            $string .= $array[$i];
        }
        return $string;
    }
    
    private function getReduced($a)
    {
        $string = $this->implode($a);
        if(!isset($this->cache[$string]))
        {
            $reduced = $this->reduce($a,TRUE);
            $this->cache[$string] = $reduced;
        }
        
        return $this->cache[$string];
    }
}
