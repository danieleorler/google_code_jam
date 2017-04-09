<?php

namespace Dalen\GoogleCodeJam\GCJ2015\OminousOmino;



/**
 * Description of OminousOmino
 *
 * @author danieleorler
 */
class OminousOmino
{
    private $matrix;
    private $columnsGroup;
    private $input;
    
    public function __construct()
    {
        $this->columnsGroup = array
        (
            1 => array("1-ominoI"),
            2 => array("2-ominoI"),
            3 => array("3-ominoI","3-ominoL"),
            4 => array("4-ominoSquare","4-ominoL","4-ominoT","4-ominoS","4-ominoI")
        );
        
        $this->matrix = array
        (
            "1x1" => array
            (
                "1-ominoI"      =>1,
                "2-ominoI"      =>0,
                "3-ominoI"      =>0,
                "3-ominoL"      =>0,
                "4-ominoSquare" =>0,
                "4-ominoL"      =>0,
                "4-ominoT"      =>0,
                "4-ominoS"      =>0,
                "4-ominoI"      =>0
            ),
            "1x2" => array
            (
                "1-ominoI"      =>1,
                "2-ominoI"      =>1,
                "3-ominoI"      =>0,
                "3-ominoL"      =>0,
                "4-ominoSquare" =>0,
                "4-ominoL"      =>0,
                "4-ominoT"      =>0,
                "4-ominoS"      =>0,
                "4-ominoI"      =>0
            ),
            "1x3" => array
            (
                "1-ominoI"      =>1,
                "2-ominoI"      =>0,
                "3-ominoI"      =>1,
                "3-ominoL"      =>0,
                "4-ominoSquare" =>0,
                "4-ominoL"      =>0,
                "4-ominoT"      =>0,
                "4-ominoS"      =>0,
                "4-ominoI"      =>0
            ),
            "1x4" => array
            (
                "1-ominoI"      =>1,
                "2-ominoI"      =>1,
                "3-ominoI"      =>0,
                "3-ominoL"      =>0,
                "4-ominoSquare" =>0,
                "4-ominoL"      =>0,
                "4-ominoT"      =>0,
                "4-ominoS"      =>0,
                "4-ominoI"      =>1
            ),
            "2x2" => array
            (
                "1-ominoI"      =>1,
                "2-ominoI"      =>1,
                "3-ominoI"      =>0,
                "3-ominoL"      =>0,
                "4-ominoSquare" =>1,
                "4-ominoL"      =>0,
                "4-ominoT"      =>0,
                "4-ominoS"      =>0,
                "4-ominoI"      =>0
            ),
            "2x3" => array
            (
                "1-ominoI"      =>1,
                "2-ominoI"      =>1,
                "3-ominoI"      =>1,
                "3-ominoL"      =>1,
                "4-ominoSquare" =>0,
                "4-ominoL"      =>0,
                "4-ominoT"      =>0,
                "4-ominoS"      =>0,
                "4-ominoI"      =>0
            ),
            "2x4" => array
            (
                "1-ominoI"      =>1,
                "2-ominoI"      =>1,
                "3-ominoI"      =>0,
                "3-ominoL"      =>0,
                "4-ominoSquare" =>1,
                "4-ominoL"      =>1,
                "4-ominoT"      =>0,
                "4-ominoS"      =>0,
                "4-ominoI"      =>1
            ),
            "3x1" => array
            (
                "1-ominoI"      =>1,
                "2-ominoI"      =>0,
                "3-ominoI"      =>1,
                "3-ominoL"      =>0,
                "4-ominoSquare" =>0,
                "4-ominoL"      =>0,
                "4-ominoT"      =>0,
                "4-ominoS"      =>0,
                "4-ominoI"      =>0
            ),
            "3x3" => array
            (
                "1-ominoI"      =>1,
                "2-ominoI"      =>0,
                "3-ominoI"      =>1,
                "3-ominoL"      =>1,
                "4-ominoSquare" =>0,
                "4-ominoL"      =>0,
                "4-ominoT"      =>0,
                "4-ominoS"      =>0,
                "4-ominoI"      =>0
            ),
            "3x4" => array
            (
                "1-ominoI"      =>1,
                "2-ominoI"      =>1,
                "3-ominoI"      =>1,
                "3-ominoL"      =>1,
                "4-ominoSquare" =>1,
                "4-ominoL"      =>1,
                "4-ominoT"      =>1,
                "4-ominoS"      =>1,
                "4-ominoI"      =>1
            ),
            "4x4" => array
            (
                "1-ominoI"      =>1,
                "2-ominoI"      =>1,
                "3-ominoI"      =>0,
                "3-ominoL"      =>0,
                "4-ominoSquare" =>1,
                "4-ominoL"      =>1,
                "4-ominoT"      =>1,
                "4-ominoS"      =>1,
                "4-ominoI"      =>1
            )
        );
        
        $this->matrix["2x1"] = $this->matrix["1x2"];
        $this->matrix["3x2"] = $this->matrix["2x3"];
        $this->matrix["3x2"] = $this->matrix["2x3"];
        $this->matrix["4x1"] = $this->matrix["1x4"];
        $this->matrix["4x2"] = $this->matrix["2x4"];
        $this->matrix["4x3"] = $this->matrix["3x4"];
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
    
    public function algorithm($x,$r,$c)
    {
        $dim = sprintf("%dx%d",$r,$c);
        
        $winner = "GABRIEL";
        
        foreach($this->columnsGroup[$x] AS $column)
        {
            if(!$this->matrix[$dim][$column])
            {
                return "RICHARD";
            }
        }
        
        return $winner;
    }
    
    public function runAlgorithm()
    {
        $results = array();
        
        $testCases = $this->input->getTestCases();
        
        for($i=0; $i<$this->input->getNumberOfTestCases(); $i++)
        {
            $input = $this->cleanInput($testCases[$i][0]);
            $result = $this->algorithm($input[0],$input[1],$input[2]);
            $results[] = $result;
        }
        
        return $results;
    }
    
    private function cleanInput($string)
    {
        return explode(" ", $string);
    }
}
