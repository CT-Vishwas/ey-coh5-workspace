'''
Name: utils.py
Purpose: Utility Functions 
'''
def is_valid_email(email: str)-> bool:
    '''
    Returns True if Email is Valid
    i.e if @ is present & only once
    '''
    if email.find('@') == -1 or email.count('@') > 1:
        return False
    return True

def username_extracter(email: str)->str:
    '''
    Returns extracted username from email id
    '''
    return is_valid_email(email) and email[:email.find('@')]

if __name__ == '__main__':
    print(username_extracter("vishwas@cloudthat.com"))
    print(username_extracter("vishwas"))
