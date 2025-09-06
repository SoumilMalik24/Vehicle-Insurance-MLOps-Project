import sys
import logging

def error_message_detail(error: Exception, error_detail:sys) -> str:
    # Extract traceable details(exception info)
    _, _, exc_tb = error_detail.exc_info() #Retrieves the current exception type, value, and traceback from sys.exc_info(); underscores ignore the first two values, keeping only the traceback object exc_tb

    #get the file name where exception occured
    file_name = exc_tb.tb_frame.f_code.co_filename

    #create a formatted error message string with file name, line number, and the actual error
    line_number = exc_tb.tb_lineno
    error_message=f"Error occured in python script:[ {file_name} ] at line number [ {line_number} ]: {str(error)}"

    #log the error for tracking
    logging.error(error_message)

    return error_message

class MyException(Exception):
    def __init__(self,error_message:str,error_detail:sys):
        #call the base class constructor with error message
        super().__init__(error_message)

        #format the detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error_message,error_detail) #Calls the helper to convert the message plus current traceback into a detailed, formatted error string and stores it on the instance.
    
    def __str__(self) -> str:
        return self.error_message