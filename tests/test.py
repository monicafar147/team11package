from team11package import team11Module

def dictionary_of_metrics(items):
    """
    make sure dictionary_of_metrics(items) works correctly
    """
    assert team11Module.dictionary_of_metrics([39660.0, 36024.0, 32127.0, 39488.0, 18422.0, 23532.0, 8842.0, 37416.0, 16156.0, 18730.0, 19261.0, 25275.0]) == {'mean': 26244.42,
                                   'median': 24403.50,
                                   'variance': 108160153.17,
                                   'standard deviation': 10400.01,
                                   'min': 8842.00,
                                   'max': 39660.00}, 'correct'

