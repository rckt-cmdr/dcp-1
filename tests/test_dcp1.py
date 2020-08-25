#!/usr/bin/python3

# File: test_dcp1.py
# Author: Jonathan Belden
# Descripton: Tests Daily Codding Challenge #1 - Figure out if two numbers add up to a given value


import pytest
from src import dcp1

@pytest.fixture
def exampleListValues():
    return [10, 15, 3, 7]  # these values were specified in the challenge


@pytest.fixture
def exampleKValue():
    return 17  # this was also specified by the challanged

def test_1_CheckValues(exampleListValues, exampleKValue):
   assert dcp1.evaluate(exampleListValues) == exampleKValue