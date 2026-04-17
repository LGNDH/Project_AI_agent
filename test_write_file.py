from functions.write_file import write_file
def main():
    print("Results for write in file: \"lorem.txt\" : \n", write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print("Results for write in file: \"pkg/morelorem.txt\" : \n", write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print("Results for write in file: \"/tmp/temp.txt\" : \n", write_file("calculator", "/tmp/temp.txt", "this should not be allowed")) #error

if __name__ == "__main__":
    main()