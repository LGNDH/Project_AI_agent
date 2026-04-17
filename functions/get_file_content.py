import os
from config import size_file_read

# function to read a file
def get_file_content(working_directory, file_path):
    #try:
        path_working_directory = os.path.abspath(working_directory)
        file_path = os.path.normpath(os.path.join(path_working_directory, file_path))


        #checking if file is in working dir
        print(os.path.commonpath([path_working_directory, file_path]))
        if os.path.commonpath([path_working_directory, file_path]) != path_working_directory:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'


        #checking if file is a file
        if os.path.isfile(file_path) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'


        #opening file and reading the file
        with open(file_path, "r") as file:
            content = file.read(size_file_read)


            if file.read(1):
                content += f'[...File "{file_path}" truncated at {size_file_read} characters]'

        return content

    #except:
        #print("Error: Standart library function issue")
