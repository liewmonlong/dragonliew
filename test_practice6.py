from practice6 import depth,classify

def test_depth():
    assert depth(1500, 0.5)==375.0
    assert depth(2000, 0.8)==800.0
    assert depth(0, 0.5)==0.0

def test_classify():
    assert classify(300)=="Air / loose soil"
    assert classify(1000)=="Sand / Clay"
    assert classify(6000)=="Dense Crystalline Rock"
    
