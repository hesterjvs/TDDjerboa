# multiple of 3 -> fizz
# multiple pf 5 -> buzz
# multiples of both -> fizzbuzz
# number

import pytest
import sys


def fizzbuzz(num):
  #  for number in num:
        if num%3 == 0 and num%5 == 0 :
            return("fizzbuzz")
        elif num%3 == 0:
            return("fizz")
        elif num%5 == 0:
            return("buzz")
        else:
            return(num)

def fizzbuzz_range(nn, out=sys.stdout):
    for num in (1,nn+1):
        out.write(fizzbuzz(num) + "\n")


def test_fizzbuzz():
    assert fizzbuzz(3) == "fizz"

def test_fizzbuzz():
    assert fizzbuzz(5) == "buzz"

def test_fizzbuzz():
    assert fizzbuzz(15) == "fizzbuzz"

def test_fizzbuzz():
    assert fizzbuzz(8) == 8

fizzbuzz_range(10)

#def test_fizzbuzz_range():
  #  assert fizzbuzz_range(10) == 1, 2, "fizz" 4 "buzz", 6, 7, 8, "fizz", "buzz"
