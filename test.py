# multiple of 3 -> fizz
# multiple pf 5 -> buzz
# multiples of both -> fizzbuzz
# number

import pytest
import sys

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0 :
        return("fizzbuzz")
    elif num % 3 == 0:
        return("fizz")
    elif num % 5 == 0:
        return("buzz")
    else:
        return(str(num))

def fizzbuzz_range(nn):
    for num in range(1, nn+1):
        print(str(fizzbuzz(num)))

def test_fizzbuzz():
    assert fizzbuzz(3) == "fizz"

def test_fizzbuzz():
    assert fizzbuzz(5) == "buzz"

def test_fizzbuzz():
    assert fizzbuzz(15) == "fizzbuzz"

def test_fizzbuzz():
    assert fizzbuzz(8) == "8"

def test_fizzbuzz_range():
    value = fizzbuzz_range(10)
    assert value == print("1\n2\nfizz\n4\nbuzz\nfizz\n7\n8\nfizz\nbuzz")
