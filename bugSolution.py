def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some code that processes the file ... 
            contents = f.read()
            # Process contents
            print(contents)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Example usage with proper file closure
function_with_closed_file("my_file.txt")
