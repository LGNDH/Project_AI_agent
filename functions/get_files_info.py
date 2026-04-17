import os


def get_files_info(working_directory , directory="."):
    try:
        path_working_directory = os.path.abspath(working_directory)
        path_directory = os.path.normpath(os.path.join(path_working_directory, directory))
        if os.path.commonpath([path_working_directory, path_directory]) != path_working_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if os.path.isdir(path_directory) == False:
            return f'Error: "{directory}" is not a directory'

        tring_items = ""
        for item in os.listdir(path_directory):
        
            name = item
            path = os.path.normpath(os.path.join(path_directory, item))
            size = os.path.getsize(path)
            is_dir = os.path.isdir(path)

            
            if string_items == "":
                string_items = f"- {name}: file_size={size} bytes, is_dir={is_dir}"
            lse:
                string_items = "\n- ".join([string_items, f"{name}: file_size={size} bytes, is_dir={is_dir}"])
    
    
        return string_items

    except:
        print("Error: Standart library function issue")