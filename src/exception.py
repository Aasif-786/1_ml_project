import sys
import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
        
    )


class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_messgae=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_messgae
    
'''if __name__=="__main__":
    try:
      a = 12 / 5
    except Exception as e:
        logging.info("divisible")
        raise CustomException(e, sys)'''



   