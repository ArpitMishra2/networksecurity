import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    """Custom exception class for Network Security errors, aalso can be another 
    method but till now this is the one i know."""
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename 
    
    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))


# Example usage of the custom exception
# This is just an example, I have to remove it or modify it before final commit.
        
""" if __name__=='__main__':
    try:
        logger.logging.info("Enter the try block")  ##caused error as info should be in small letters
        a=1/0
        print("This will not be printed",a)
    except Exception as e:
           raise NetworkSecurityException(e,sys) """