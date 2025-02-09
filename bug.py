def function_with_unclosed_file(filename):
    f = open(filename, 'r')
    # ... some code that processes the file ... 
    # Missing f.close() or with statement

# Example usage that will lead to a resource leak
function_with_unclosed_file("my_file.txt")