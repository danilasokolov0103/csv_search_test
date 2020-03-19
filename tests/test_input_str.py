import pytest
from csv_search.script import *


def test_input_str1():
    first_name_entry.insert(0, 3)
    assert type(first_name.get()) == str


def test_input_str2():
    first_name_entry.insert(0, '3')
    assert type(first_name.get()) == str


def test_input_str3():
    first_name_entry.insert(0, float(3))
    assert type(first_name.get()) == str


def test_input_str4():
    first_name_entry.insert(0, bool(3))
    assert type(first_name.get()) == str


def test_input_str5():
    second_name_entry.insert(0, 3)
    assert type(first_name.get()) == str


def test_input_str6():
    second_name_entry.insert(0, '3')
    assert type(first_name.get()) == str


def test_input_str7():
    second_name_entry.insert(0, float(3))
    assert type(first_name.get()) == str


def test_input_str8():
    second_name_entry.insert(0, bool(3))
    assert type(first_name.get()) == str
