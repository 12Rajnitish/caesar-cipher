import art

# Print the logo when the program starts
print(art.logo)

# Alphabet list for Caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_num, encode_or_decode):
    output_text = ""
    
    for letter in original_text:
        if letter in alphabet:
            # Shift letter based on encoding/decoding
            if encode_or_decode == 'encode':
                shifted_index = alphabet.index(letter) + shift_num
            else:
                shifted_index = alphabet.index(letter) - shift_num
            
            # Wrap around alphabet if needed
            shifted_index %= len(alphabet)
            output_text += alphabet[shifted_index]
        else:
            output_text += letter  # Non-alphabet characters remain unchanged

    # Print the result
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Main program loop
user_input = 'yes'
while user_input == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
    if direction not in ['encode','decode']:
        print("Invalid input, please type encode or decode.\n")
        continue
    
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_num=shift, encode_or_decode=direction)
    
    user_input = input("Do you want to continue? (yes/no): ").lower()
