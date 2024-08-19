def decipher_message(s, shifts):
    
    s = list(s)
    for start_disc, end_disc, direction in shifts:
        
        for i in range(start_disc, end_disc + 1):
            current_char_index = ord(s[i]) - ord('a')
            
            if direction == 1:
                new_char_index = (current_char_index + 1) % 26
            else:
                new_char_index = (current_char_index - 1) % 26
            
            s[i] = chr(new_char_index + ord('a'))
    
    return ''.join(s)


s = "hello"
shifts = [[0, 1, 1], [2, 3, 0], [0, 2, 1]]
print(decipher_message(s, shifts))  