from hazm import Normalizer
import re 
import pandas
my_normalizer = Normalizer(persian_style=True,
                correct_spacing=True,
                remove_diacritics=True,
                decrease_repeated_chars=False)
repeat_pattern = re.compile(r'(.)\1{2,}')
def normalizator(chunk):
    # solve repeating alphabet problem
    chunk = chunk.str.replace(repeat_pattern, r'\1', regex=True)
    
    # hazm normalizer
    chunk = chunk.apply(my_normalizer.normalize)
    
    #solve half-space problem
    chunk = chunk.str.replace(r'\u200c', ' ', regex=True)
    
    #solve double-space problem caused by removing half-space
    chunk = chunk.str.replace(r' {2,}', ' ', regex=True).str.strip()
    
    return chunk
    