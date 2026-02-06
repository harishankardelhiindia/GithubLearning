first_txt = input("Enter the text to write to the 'Ouput.txt' File: ")
fh = open('Output.txt','wt')
fh.write(first_txt)
print("Data successfully written to 'Output.txt\n")
fh.close()
append_txt = input("Enter additional text to append: ")
fh = open('Output.txt','at')
fh.write(f"\n{append_txt}")
print("Data Successfully Appended")
fh.close()


