import re

def count_syllables(word):
    '''
    Counts the number of syllables in a word using a simple algorithm

    Inputs:
        - word (str): The word to count syllables for

    Returns:
        - syllable_count (int): The number of syllables in the word
    '''
    
    # Cleaning the word
    word = word.lower().strip()
    word = re.sub(r'[^a-z]', '', word)  # Remove non-alphabetic characters

    # If the word is empty after cleaning, return 0
    if not word:
        return 0

    # Defining vowel patterns
    vowels = 'aeiouy'

    # Removing silent 'e' at the end of the word
    if word.endswith('e'):
        if len(word) > 2 and not re.match(r'.*[aeiouy][^aeiouy]e$', word):
            word = word[:-1]

    # Counting the number of vowel groups
    vowel_groups = re.findall(r'[aeiouy]+', word)

    # Setting the syllable count to the number of vowel groups
    syllable_count = len(vowel_groups)

    # Adjusting syllable count for specific patterns
    subtract_patterns = [
        r'[^aeiouy]e$',  # Silent 'e' at the end
        r'[^aeiouy]le$',  # 'le' ending where 'e' is pronounced
        r'ia$',           # Ending 'ia' sometimes forms one syllable
        r'tio$',          # 'tion' ending pronounced as one syllable
        r'^y',            # 'y' at the start doesn't form a syllable
    ]

    add_patterns = [
        r'ia',            # 'ia' in the middle increases syllable count
        r'io',            # 'io' in the middle increases syllable count
        r'ii',            # Double 'i' increases syllable count
        r'ua',            # 'ua' in the middle increases syllable count
        r'iu',            # 'iu' in the middle increases syllable count
        r'iy',            # 'iy' combination increases syllable count
        r'ue$',           # Ending 'ue' can form a separate syllable
        r'^re',           # 're' at the start can form a separate syllable
    ]

    for pattern in subtract_patterns:
        if re.search(pattern, word):
            syllable_count -= 1

    for pattern in add_patterns:
        if re.search(pattern, word):
            syllable_count += 1

    # Ensuring at least one syllable
    syllable_count = max(syllable_count, 1)

    return syllable_count