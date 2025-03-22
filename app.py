from signAI.logger import logging 
from signAI.exception import SignException
import sys
# logging.info("welcome to the porject now")

try:
    a =7/ '9'

except Exception as e:
    raise SignException(e, sys) from e