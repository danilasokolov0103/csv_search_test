import pytest
from csv_search.script import *
from csv_search.script import first_name

info = 'Duky Ruttgers - 8/17/1963 - Driver'

info2 = 'Odie Lowthian - 7/19/1994 - Python Engineer'


def test_input1():
    assert info in show_info(import_from_csv('test.csv'), 'Duky', 'Ruttgers')


def test_input2():
    assert info in show_info(import_from_csv('test.csv'), '', 'Ruttgers')


def test_input3():
    assert info in show_info(import_from_csv('test.csv'), 'Duky', '')


def test_input4():
    assert info in show_info(import_from_csv('test.csv'), 'Du', '')


def test_input5():
    assert info in show_info(import_from_csv('test.csv'), ' Du', '')


def test_input6():
    assert info in show_info(import_from_csv('test.csv'), ' Du ', '')


def test_input7():
    assert info in show_info(import_from_csv('test.csv'), '', ' Ruttgers')


def test_input8():
    assert info in show_info(import_from_csv('test.csv'), '', ' Ruttgers ')


def test_input9():
    assert info in show_info(import_from_csv('test.csv'), '', 'ruttgers')


def test_input10():
    assert info in show_info(import_from_csv('test.csv'), 'duky', '')


def test_input11():
    assert info2 not in show_info(
        import_from_csv('test.csv'), 'Duky', 'Ruttgers')


def test_input12():
    assert info2 not in show_info(import_from_csv('test.csv'), 'du', '')


def test_input13():
    assert info2 in show_info(import_from_csv('test.csv'), '', '')



