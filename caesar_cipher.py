def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + (shift if mode == "encrypt" else -shift)) % 26
            result += chr(base + shifted)
        else:
            result += char
    return result

while True:
    print("\n--- Caesar Cipher Tool ---")
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Exit")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1" or choice == "2":
        message = input("Enter your message: ")
        shift = int(input("Enter shift value: "))
        mode = "encrypt" if choice == "1" else "decrypt"
        result = caesar_cipher(message, shift, mode)
        print(f"\n{mode.title()}ed message: {result}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")