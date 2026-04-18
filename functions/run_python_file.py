import os
import subprocess
from google import genai
from google.genai import types

#function declaration run_python_file
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files with optional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to a file from, relative to the working directory",
            ),
             "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional arguments to run the python file, default None ",
                items=types.Schema(type=types.Type.STRING)
            ),
        },
    ),
)


def run_python_file(working_directory, file_path, args=None):
    try:
        path_working_directory = os.path.abspath(working_directory)
        path_file = os.path.normpath(os.path.join(path_working_directory,file_path))

        #checking if file in directory
        if os.path.commonpath([path_working_directory, path_file]) != path_working_directory:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        #checking if file_path exists and if it is a file
        if os.path.isfile(path_file) == False:
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if path_file.endswith(".py") == False:
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", path_file]
        if args != None:
            command.extend(args)
    
        #starting process
        Completed_process = subprocess.run(command, capture_output=True, text=True, timeout=30)
     
        #string output
        string_output = ""
        if Completed_process.returncode != 0:
            string_output += f"Process exited with code {Completed_process.returncode}"

        if Completed_process.stdout == None and Completed_process.stderr == None:
            string_output += "\nNo output produced"
        else:
            string_output += f"\nSTDOUT: {Completed_process.stdout}\nSTDERR: {Completed_process.stderr}"
        
        return string_output
    except:
        print(f"Error: executing Python file: {file_path}")