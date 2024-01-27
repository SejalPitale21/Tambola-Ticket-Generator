class wrong_sets_input(Exception):
    '''This error will be raised when sets is not an integer'''
    def __init__(self , message):
        self.errorCode = 400
        self.errorMessage = message