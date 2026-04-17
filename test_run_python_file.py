from functions.run_python_file import run_python_file
def main():
    print("Testing calculator dir:")
    print("Results for Run_python \"main.py\"", run_python_file("calculator", "main.py"))
    print("Results for Run_python \"main.py\" [3 + 5]", run_python_file("calculator", "main.py", ["3 + 5"])) 
    print("Results for Run_python \"tests.py\"", run_python_file("calculator", "tests.py")) 
    print("Results for Run_python \"../main.py\"", run_python_file("calculator", "../main.py"))
    print("Results for Run_python \"nonexistent.py\"", run_python_file("calculator", "nonexistent.py")) #error
    print("Results for Run_python \"lorem.txt\"",run_python_file("calculator", "lorem.txt")) #error

if __name__ == "__main__":
    main()