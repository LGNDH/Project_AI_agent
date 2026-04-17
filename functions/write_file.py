import os

def write_file(working_directory, file_path, content):
    try:
        path_working_directory = os.path.abspath(working_directory)
        path_file = os.path.normpath(os.path.join(path_working_directory, file_path))


        #checking if file is in working dir
        print(os.path.commonpath([path_working_directory, path_file]))
        if os.path.commonpath([path_working_directory, path_file]) != path_working_directory:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'


        #checking if file is a file
        if os.path.isdir(path_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        
        #creating parent dir if not existent
        os.makedirs(os.path.dirname(path_file), exist_ok=True)

        with open(path_file, "w") as file:
            write_file = file.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except:
        print("Error: Standart library function issue")