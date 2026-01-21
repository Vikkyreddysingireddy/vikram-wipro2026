def writenumfile(filename):
    try:
        with open(filename, "w") as file:
            for number in range(1, 101):
                file.write(f"{number}\n")

    except FileNotFoundError:
        print("Error: The specified file path was not found.")

    except PermissionError:
        print("Error: Permission denied while writing to the file.")

    except Exception as e:
        print(f"Unexpected error occurred: {e}")

def readnumfile(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("File content:")
            print(content)

    except FileNotFoundError:
        print("Error: File does not exist.")

    except PermissionError:
        print("Error: Permission denied while reading the file.")

    except Exception as e:
        print(f"Unexpected error occurred: {e}")

filename = "../diff b/numbers.txt"

writenumfile(filename)
readnumfile(filename)

