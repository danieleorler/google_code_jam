<?php

require_once('./vendor/autoload.php');

use Dalen\GoogleCodeJam\Common\IOHelper;
use Dalen\GoogleCodeJam\GCJ2015\StandingOvation\StandingOvation;
use Dalen\GoogleCodeJam\GCJ2015\OminousOmino\OminousOmino;
use Dalen\GoogleCodeJam\GCJ2015\Dijkstra\Dijkstra;

//$input = IOHelper::readFile("./tests/data/gcj2015/A-large.in",1);
//$standingOvation = new StandingOvation();
//$standingOvation->setInput($input);
//$results = $standingOvation->runAlgorithm();
//IOHelper::writeToFile("./results/gcj2015/standing_ovation_big.out", $results);

//$input = IOHelper::readFile("./tests/data/gcj2015/D-small-attempt0.in",1);
//$standingOvation = new OminousOmino();
//$standingOvation->setInput($input);
//$results = $standingOvation->runAlgorithm();
//IOHelper::writeToFile("./results/gcj2015/omino_small.out", $results);

$input = IOHelper::readFile("./tests/data/gcj2015/C-small-attempt0.in",2);
$object = new Dijkstra();
$object->setInput($input);
$results = $object->runAlgorithm();
IOHelper::writeToFile("./results/gcj2015/dijkstra_test.out", $results);
