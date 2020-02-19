from team11package import team11Module

def test_function1():
    '''make sure function 1 works well'''
    assert team11Module.dictionary_of_metrics([39660.0, 36024.0, 32127.0, 39488.0, 18422.0, 23532.0, 8842.0, 37416.0, 16156.0, 18730.0, 19261.0, 25275.0]) == {
    'max': 39660.00,
    'median': 24403.50,
    'min': 8842.00,
    'q1': 18576.00,
    'q3': 36720.00}, 'correct'