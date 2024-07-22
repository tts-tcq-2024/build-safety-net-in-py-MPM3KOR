def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters


def soundex_length_check (soundex_word):
    soundex_complete_code = soundex_word[0:4]
    # Pad with zeros if necessary
    soundex_zeros_padded = soundex_complete_code.ljust(4, '0')
    return soundex_zeros_padded


def soundex_code_conversion(character):
    # Start with the first letter (capitalized)
    soundex = character[0].upper()
    
    for char in character[1:]:
        code = get_soundex_code(char)
        if (code!='0') and (code != soundex[-1]):
                soundex += code
               
    return soundex
    
    
def generate_soundex(name):
    if not name:
        return ""
    soundex_code = soundex_code_conversion(name)
    # Pad with zeros if necessary
    soundex_code = soundex_length_check(soundex_code)
  
    return soundex_code
