# Simple Text Uppercase Converter
# This program asks the user for text and converts it to uppercase.

def convert_to_uppercase(text):
    """Returns the text in uppercase."""
    return text.upper()

def main():
    print("Enter text to convert:")
    user_input = input()
    result = convert_to_uppercase(user_input)
    print("Uppercase version:", result)

if __name__ == "__main__":
    main()