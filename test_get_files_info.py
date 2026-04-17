from functions.get_files_info import get_files_info
def main():
    print("Results for current directory: \n", get_files_info("calculator", "."))
    print("Results for \'pkg' directory: \n", get_files_info("calculator", "pkg"))
    print("Results for \'/bin\' directory: \n", get_files_info("calculator", "/bin")) #error
    print("Results for \'../\' directory: \n", get_files_info("calculator", "../")) #error

if __name__ == "__main__":
    main()