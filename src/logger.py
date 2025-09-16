import logging 
import os 
from datetime import datetime 

# Define the log file name using the current date and time 
log_file_name = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

# Create the path to the log file (logs folder inside current working directory)
log_file_path = os.path.join(os.getcwd(), 'logs', log_file_name)

# Create the 'logs' directory if it does not already exist
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

# Configuration for logging
logging.basicConfig(
    # specify the log file path
    filename=log_file_path,  
    
    # set the logging level to INFO - only INFO and above (WARNING, ERROR, CRITICAL) will be logged 
    level=logging.INFO,  
    
    # specify the format for each log entry
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

# Test the logger 
if __name__ == "__main__":
    # log your informative message 
    logging.info("Logging into the System!")
