# import utils
# print(utils.username_extracter("John.doe@gmail.com"))

# from utils import username_extracter

# print(username_extracter("John.doe@gmail.com"))

from utilities.utils import username_extracter as ua

print(ua("John.doe@gmail.com"))