def read_file(file_name):
    file = open(file_name, "r")
    return str(file.read())
    file.close()
