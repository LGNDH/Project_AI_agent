import os
from config import size_file_read
from google import genai
from google.genai import types

#function declaration get_file_content
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the file, providing first 10000 characters from the file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to a file from, relative to the working directory",
            ),
        },
    ),
)

# function to read a file
def get_file_content(working_directory, file_path):
    try:
        path_working_directory = os.path.abspath(working_directory)
        path_file = os.path.normpath(os.path.join(path_working_directory, file_path))


        #checking if file is in working dir
        if os.path.commonpath([path_working_directory, path_file]) != path_working_directory:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'


        #checking if file is a file
        if os.path.isfile(path_file) == False:
            return f'Error: File not found or is not a regular file: "{file_path}"'


        #opening file and reading the file
        with open(path_file, "r") as file:
            content = file.read(size_file_read)


            if file.read(1):
                content += f'[...File "{file_path}" truncated at {size_file_read} characters]'

        return content

    except:
        print("Error: Standart library function issue")
