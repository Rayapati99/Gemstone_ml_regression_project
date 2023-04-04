import os
import sys

import logging
from datetime import datetime

log_file=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
LOG_PATH=os.path.join(os.getcwd(),'log',log_file)
os.makedirs(LOG_PATH,exist_ok=True)

LOG_FILE_PATH=os.path.join(LOG_PATH,log_file)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__=='__main__':
    logging.info('logging has strated')