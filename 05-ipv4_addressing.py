ip_address = input("Enter the IPv4 Address to Validate: ")
fields = ip_address.split('.')
# if len(fields) != 4:
#     print("Invalid IP")

# for field in fields:
#     if not field.isdigit():
#         print("Invalid IP")
#         break

#     converted_field = int(field)
#     if not (converted_field >= 0 and converted_field <= 255):
#         print("Invalid IP")
#         break
# else:
#     print(f"The IPv4 Address: {ip_address} is valid")

flg = 0
if len(fields) != 4:
    print("Invalid IP")

for field in fields:
    if not field.isdigit() or not (int(field) >= 0 and int(field) <= 255):
        flg = 1
        break

if flg == 0:
    print(f"The IPv4 Address: {ip_address} is valid")
else:
    print("Invalid IP")