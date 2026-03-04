def processedtypefrfr(file_path):
    try:
        processedtypefrfr = []

        with open(lefile, 'r') as file:
            for line in file:
                cleaned_line = line.strip()
                cleaned_line = cleaned_line.lower()
                try:
                    cleaned_line = int(cleaned_line)
                except ValueError:
                    pass
                processedtypefrfr.append(cleaned_line)
        return processedtypefrfr
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def get_file_from_user():
    while True:
        lefile = input("Please enter the file path: ")
        try:
            data = processedtypefrfr(lefile)
            if data is not None:
                print("File processed successfully!")
                return data
        except Exception:
            print("Something went wrong. Please try again.")

        print("Please enter a valid file path.")
