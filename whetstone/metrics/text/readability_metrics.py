from typing import Union, List
from whetstone.utils.text.text_parsers import tokenize_sentence, count_syllables



def calculate_flesch_kincaid_reading_ease(texts: Union[str, List[str]]) -> List[float]:
    '''
    Calculate the Flesch-Kincaid Reading Ease score for one or multiple texts.

    Inputs:
        - texts (str or list[str]): The input text(s) for which to calculate the Reading Ease score.

    Returns:
        - scores (list[float]): A list of Flesch-Kincaid Reading Ease scores corresponding to each input text.
    '''
    # If a single text string is provided, wrap it in a list
    if isinstance(texts, str):
        texts = [texts]

    results = []
    for text in texts:
        # Tokenizing the text into sentences and words
        sentences = tokenize_sentence(text)
        words = text.split()

        # Calculating the number of sentences, words, and syllables
        num_sentences = len(sentences)
        num_words = len(words)
        num_syllables = sum(count_syllables(word) for word in words)
        
        # Calculating the averages
        avg_words_per_sentence = num_words / num_sentences if num_sentences > 0 else 0
        avg_syllables_per_word = num_syllables / num_words if num_words > 0 else 0
        
        # Calculating the Flesch-Kincaid Reading Ease score
        score = round(206.835 - 1.015 * avg_words_per_sentence - 84.6 * avg_syllables_per_word, 2)
        results.append(score)

    return results



def calculate_flesch_kincaid_grade_level(texts: Union[str, List[str]]) -> List[float]:
    '''
    Calculate the Flesch-Kincaid Grade Level score for one or multiple texts.

    Inputs:
        - texts (str or list[str]): The input text(s) for which to calculate the Grade Level score.

    Returns:
        - scores (list[float]): A list of Flesch-Kincaid Grade Level scores corresponding to each input text.
    '''
    # If a single text string is provided, wrap it in a list
    if isinstance(texts, str):
        texts = [texts]

    results = []
    for text in texts:
        # Tokenizing the text into sentences and words
        sentences = tokenize_sentence(text)
        words = text.split()

        # Calculating the number of sentences, words, and syllables
        num_sentences = len(sentences)
        num_words = len(words)
        num_syllables = sum(count_syllables(word) for word in words)
        
        # Calculating the averages
        avg_words_per_sentence = num_words / num_sentences if num_sentences > 0 else 0
        avg_syllables_per_word = num_syllables / num_words if num_words > 0 else 0
        
        # Calculating the Flesch-Kincaid Grade Level score
        score = round(.39 * avg_words_per_sentence + 11.8 * avg_syllables_per_word - 15.59, 2)
        results.append(score)

    return results



def calculate_all_readability_metrics(texts: Union[str, List[str]]) -> List[dict]:
    '''
    Calculate all readability metrics for one or multiple texts.
    
    Inputs:
        - texts (str or list[str]): The input text(s) for which to calculate the readability metrics.
    
    Returns:
        - results (list[dict]): A list of dictionaries, each containing all readability metrics for the corresponding input text.
    '''
    
    # Wrapping the input in a list if it is a single string
    if isinstance(texts, str):
        texts = [texts]
    
    # Calculating all the respective metrics all metrics as lists
    fk_reading_ease_scores = calculate_flesch_kincaid_reading_ease(texts)
    fk_grade_level_scores = calculate_flesch_kincaid_grade_level(texts)
    
    # Combining into a list of dictionaries
    results = []
    for re_score, gl_score in zip(fk_reading_ease_scores, fk_grade_level_scores):
        readability_metrics = {
            'flesch_kincaid_reading_ease': re_score,
            'flesch_kincaid_grade_level': gl_score
        }
        results.append(readability_metrics)

    return results
