from functions.get_file_content import get_file_content
def main():
    print("Results for file:\"lorem.txt\": \n", get_file_content("calculator", "lorem.txt"))
    print("Results for file:\"main.py\": \n", get_file_content("calculator", "main.py"))
    print("Results for file:\"pkg/calculator.py\": \n", get_file_content("calculator", "pkg/calculator.py"))
    print("Results for file:\"/bin/cat\": \n", get_file_content("calculator", "/bin/cat"))
    print("Results for file:\"pkg/does_not_exist.py\": \n", get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    main()