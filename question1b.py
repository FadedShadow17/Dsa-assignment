def decipher_message(s, shifts):
    
    s = list(s)
    for start_disc, end_disc, direction in shifts:
        
        for i in range(start_disc, end_disc + 1):
            # Calculate the current position in the alphabet (0-based index)
            current_char_index = ord(s[i]) - ord('a')
            
            # Apply the shift: +1 for clockwise, -1 for counterclockwise
            if direction == 1:
                new_char_index = (current_char_index + 1) % 26
            else:
                new_char_index = (current_char_index - 1) % 26
            
            # Convert back to the character and update the string
            s[i] = chr(new_char_index + ord('a'))
    
    # Return the final deciphered message as a string
    return ''.join(s)


s = "hello"
shifts = [[0, 1, 1], [2, 3, 0], [0, 2, 1]]
print(decipher_message(s, shifts))  