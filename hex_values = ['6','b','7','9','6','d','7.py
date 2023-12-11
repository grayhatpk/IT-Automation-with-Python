
hex_values = ['6b', '79', '6d', '7e', '68', '75', '6d', '72']  # List of hexadecimal values

username = ""

for hex_val in hex_values:
    decimal_val = int(hex_val, 16)  # Convert hexadecimal string to decimal integer
    decimal_val -= 8
    xor_result = decimal_val ^ 4
    username += chr(xor_result)  # Convert decimal XOR result to character

print(username)
