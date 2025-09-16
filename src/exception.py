import sys 
from logger import logging 

# Define a method that will extract the error message 
def error_message_detail(error, error_details_object: sys): 
    # exc_info() returns (type, value, traceback)
    _, _, exc_tb = error_details_object.exc_info()
    
    # extract file name from traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename  
    
    # format the error message with file, line number and actual error message
    formatted_error_message = f"Error in Python Script: [{file_name}] line number [{exc_tb.tb_lineno}] error_message [{error}]"
    return formatted_error_message


# Define a custom exception class
class FileOperatorError(Exception): 
    def __init__(self, formatted_error_message, error_details_object: sys): 
        # call the parent Exception constructor with the error message
        super().__init__(formatted_error_message)  
        
        # store the formatted error message using helper function
        self.formatted_error_message = error_message_detail(formatted_error_message, error_details_object=error_details_object)

    # override the string representation to return formatted error
    def __str__(self): 
        return self.formatted_error_message


# Testing the custom exception
if __name__ == "__main__": 
    try: 
        # cause a ZeroDivisionError
        a = 1/0
    except Exception as e: 
        # log some additional info
        logging.info("It is not possible: Division by Zero Error")
        
        # raise the custom error with detailed message
        raise FileOperatorError(e, sys)
