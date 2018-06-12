import asyncer

def test_tuple_args():

    def someFunc(one, two):
        return one + two
    def someFunc2(one, two, three):
        return one + two + three

    ones = [1]*5
    twos = [2]*5
    threes = [3]*5
    one_two = list(zip(ones, twos))    
    one_two_three = list(zip(ones, twos, threes))
    assert asyncer.asyncRun(one_two, someFunc) == [3]*5
    assert asyncer.asyncRun(one_two_three, someFunc2) == [6]*5

def test_single_args():
    def someFunc(one):
        return one * 2
    
    ones = [1]*5      
    assert asyncer.asyncRun(ones, someFunc) == [2]*5