import pytest
import random
from treaps import Treap

def test_checkHeapProp():
    T = Treap()
    for i in range(10000):
        T.insert(i, "o")
    assert T.checkHeapProp() == True

def test_checkTreeProp():
    T = Treap()
    for i in range(10000):
        T.insert(i, "h")
    assert T.checkTreeProp() == True
    
def test_countInserts():
    T = Treap()
    count = 0
    for i in range(1, 101):
        T.insert(i, "r")
    for i in range(1, 101):
        if T.find(i):
            count += 1
    assert count == 100
    
def test_delete():
    T = Treap()
    count = 0
    nones = 0
    for i in range(1, 1000):
        T.insert(i, "a")
    for i in range(100, 1000, 20):
        T.delete(i)
    for i in range(1, 1000):
        if T.find(i):
            count+=1
        else:
            nones += 1
    assert count == 954
    assert nones == 45
    
def test_allThree():
    T = Treap()
    ans = []
    for i in range(1, 6):
        T.insert(i, "a"*i)
    T.delete(2)
    T.delete(5)
    T.delete(3)
    for i in range(1, 6):
        ans += [T.find(i)]
    assert ans == ["a", None, None, "aaaa", None]
    
pytest.main(["-v"])
    