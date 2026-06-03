'''
Module to validate IPv4 Address
'''

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


ip_address = input("Enter the IPv4 Address to Validate: ")
if is_valid_ip(ip_address):
    print(f"The IPv4 Address: {ip_address} is valid")
else:
    print(f"{ip_address} is INVALID!")