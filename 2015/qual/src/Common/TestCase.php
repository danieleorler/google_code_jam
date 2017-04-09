<?php

namespace Dalen\GoogleCodeJam\Common;

/**
 * Description of TestCase
 *
 * @author danieleorler
 */
class TestCase
{
    private $items = array();
    
    public function addItem($name,$value,$isArray)
    {
        if($isArray)
        {
            $this->items[$name] = explode(" ",$value);
        }
        else
        {
            $this->items[$name] = $value;
        }
    }
    
    public function getItem($name)
    {
        return $this->items[$name];
    }
}
