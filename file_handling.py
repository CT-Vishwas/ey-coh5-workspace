# try:
#     with open(r"C:\Users\VishwasKSingh\Workspace\ey-coh5-workspace\01-basic.py", "r") as fh:
#         data = fh.readlines()
#         print(data)

# except FileNotFoundError:
#     print("File you are trying to read does not exist")
# except Exception:
#     print("Unnown Error")


try:
    with open(r"data_write.txt", "a") as fh:
        fh.write("I am Learning Python")

    with open("data_write.txt","r+") as fh:
        data = fh.read()
        print(data)
        
except FileNotFoundError:
    print("File you are trying to read does not exist")
except FileExistsError:
    print("Trying to overwrite existing data")
except Exception:
    print("Unnown Error")
