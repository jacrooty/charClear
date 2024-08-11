# pass in the characters that you want to remove from text file
# example: python clean_text.py your_file.txt == ** -

import re
import sys

def remove_patterns(text, patterns):
    # Loop through each pattern
    for pattern in patterns:
        # Replace the pattern with an empty string (essentially removing it)
        text = re.sub(re.escape(pattern), '', text)
    
    return text

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <filename> <pattern1> [<pattern2> ...]")
        sys.exit(1)
    
    filename = sys.argv[1]
    patterns = sys.argv[2:]
    
    try:
        with open(filename, 'r') as file:
            text = file.read()
            cleaned_text = remove_patterns(text, patterns)
            with open(f"cleaned_{filename}", 'w') as cleaned_file:
                cleaned_file.write(cleaned_text)
        print(f"Cleaned file saved as cleaned_{filename}")
    except FileNotFoundError:
        print(f"File {filename} not found")

if __name__ == "__main__":
    main()