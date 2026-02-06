n=1
file_name = str(input("Type the file name with extension you want to open: "))
try:
    with open (file_name,'rt') as fh:
        file_lines = fh.readlines()
        print("Reading file Contents")
        n = 1
        for i in file_lines:
            print(f"Line {n}: {i.rstrip('\n')}")
            n+=1
        fh.close()
except FileNotFoundError:
    print(f"Error: File name '{file_name}' was not found")



