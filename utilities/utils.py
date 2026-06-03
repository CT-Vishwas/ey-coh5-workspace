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

def is_valid_ip(ip_address: str) -> bool:
    '''
    Validates a given IPv4 Address

    Returns True if given string is a valid IPv4
    '''
    fields = ip_address.split('.')
    if len(fields) != 4:
        return False

    for field in fields:
        if not field.isdigit():
            return False

        converted_field = int(field)
        if not (converted_field >= 0 and converted_field <= 255):
            return False
    else:
    
        return True
    
def is_non_local_ip(ip_address: str) -> bool:
    '''
    Returns True if the ip_address is non-local
    '''
    if is_valid_ip(ip_address):
        if (ip_address.startswith("10.") or ip_address.startswith("192.168.")):
            return False
        
        elif (ip_address.startswith("172.") and int(ip_address.split('.')[1]) >= 16 and int(ip_address.split('.')[1]) <= 31):
            return False
        else:
            return True

if __name__ == '__main__':
    print(username_extracter("vishwas@cloudthat.com"))
    print(username_extracter("vishwas"))
    ips = ["10.0.0.1", "172.16.21.1", "192.168.1.1","3.5.17.1", "72.58.1.6"]
    for ip in ips:
        result = is_non_local_ip(ip)
        print(f"Is {ip} nonlocal? {result}")
