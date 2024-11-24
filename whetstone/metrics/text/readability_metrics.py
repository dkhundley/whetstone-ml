from whetstone.utils.text.text_parsers import *

def calculate_flesch_kincaid_reading_ease(text):
    '''
    Calculate the Flesch-Kincaid Reading Ease score for a given text.

    Inputs:
        - text (str): The input text for which to calculate the Flesch-Kincaid Reading Ease score.

    Returns:
        - flesch_kincaid_reading_ease_score (float): The Flesch-Kincaid Reading Ease score for the input text.
    '''
    # Tokenizing the text into sentences and words
    sentences = tokenize_sentence(text)
    words = text.split()

    # Calculating the number of sentences, words, and syllables
    num_sentences = len(sentences)
    num_words = len(words)
    num_syllables = sum(count_syllables(word) for word in words)
    
    # Calculating the average number of words per sentence and syllables per word
    avg_words_per_sentence = num_words / num_sentences
    avg_syllables_per_word = num_syllables / num_words
    
    # Calculating the Flesch Reading Ease score
    flesch_kincaid_reading_ease_score = round(206.835 - 1.015 * avg_words_per_sentence - 84.6 * avg_syllables_per_word, 2)

    return flesch_kincaid_reading_ease_score



def calculate_flesch_kincaid_grade_level(text):
    '''
    Calculate the Flesch-Kincaid Grade Level score for a given text.

    Inputs:
        - text (str): The input text for which to calculate the Flesch-Kincaid Grade Level score.

    Returns:
        - flesch_kincaid_grade_level_score (float): The Flesch-Kincaid Grade Level for the input text.
    '''
    # Tokenizing the text into sentences and words
    sentences = tokenize_sentence(text)
    words = text.split()

    # Calculating the number of sentences, words, and syllables
    num_sentences = len(sentences)
    num_words = len(words)
    num_syllables = sum(count_syllables(word) for word in words)
    
    # Calculating the average number of words per sentence and syllables per word
    avg_words_per_sentence = num_words / num_sentences
    avg_syllables_per_word = num_syllables / num_words
    
    # Calculating the Flesch-Kincaid Grade Level score
    flesch_kincaid_grade_level_score = round(.39 * avg_words_per_sentence + 11.8 * avg_syllables_per_word - 15.59, 2)

    return flesch_kincaid_grade_level_score