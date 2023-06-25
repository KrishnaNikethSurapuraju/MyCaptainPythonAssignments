file=input("Input the filename: ")

dot_index=file.rfind(".")

extension=file[dot_index + 1:]

print("The extension of the file is : ", extension)
