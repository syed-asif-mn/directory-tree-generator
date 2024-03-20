import os

def generate_directory_tree(root_dir, indent='', output_file=None):
    """
    Generate a directory tree structure starting from the root directory and write it to a file.
    """
    items = os.listdir(root_dir)
    for i, item in enumerate(items):
        path = os.path.join(root_dir, item).encode('unicode_escape').decode()
        if os.path.isdir(path):
            line = indent + '├── ' + item + '\n'
            if i == len(items) - 1:
                line = indent + '└── ' + item + '\n'
            print(line, end='')
            if output_file:
                output_file.write(line)
            generate_directory_tree(path, indent + ('    ' if i < len(items) - 1 else '   '), output_file)
        else:
            line = indent + '└── ' + item + '\n' if i == len(items) - 1 else indent + '├── ' + item + '\n'
            print(line, end='')
            if output_file:
                output_file.write(line)

# Example usage
root_directory = r'path\\to\\directory' # Input directory path
output_filename = r'D:\python\directory_tree.txt'  # Output file name

with open(output_filename, 'w', encoding='utf-8') as output_file:
    generate_directory_tree(root_directory, output_file=output_file)
    
print(f"Directory tree written to {output_filename}")

