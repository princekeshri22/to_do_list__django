def write_file(file_name,s):
    file = open(file_name, "w")
    file.truncate()
    file.write(str(s))
    file.close()