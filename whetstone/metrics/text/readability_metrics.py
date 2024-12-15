import re
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



def calculate_gunning_fog_index(text: str) -> float:
    '''
    Calculates the Gunning Fog Index for the given text.
    
    Inputs:
        - text (str): The input text to analyze.
    
    Returns:
        - gunning_fog_index (float): The Gunning Fog Index score
    '''
    # Tokenizing sentences (basic method using punctuation)
    sentences = re.split(r'[.!?]+', text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    # Tokenizing words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Getting the complex words (words with 3+ syllables)
    complex_words = [word for word in words if count_syllables(word) >= 3]
    
    # Getting number of sentences, words, and complex words
    num_sentences = len(sentences)
    num_words = len(words)
    num_complex_words = len(complex_words)
    
    # Avoiding division by zero
    if num_sentences == 0 or num_words == 0:
        return 0.0
    
    # Performing the Gunning Fog Index calculation
    avg_sentence_length = num_words / num_sentences
    percent_complex_words = (num_complex_words / num_words) * 100
    gunning_fog_index = 0.4 * (avg_sentence_length + percent_complex_words)
    
    return gunning_fog_index



def calculate_coleman_liau_index(texts: Union[str, List[str]]) -> List[float]:
    '''
    Calculate the Coleman-Liau Index for one or multiple texts.

    Inputs:
        - texts (str or list[str]): The input text(s) for which to calculate the Coleman-Liau Index.

    Returns:
        - cl_index_scores (list[float]): A list of Coleman-Liau Index scores corresponding to each input text.
    '''
    # Wrapping the input in a list if it is a single string
    if isinstance(texts, str):
        texts = [texts]

    cl_index_scores = []
    for text in texts:
        # Tokenizing sentences and words
        sentences = tokenize_sentence(text)
        words = re.findall(r'\b\w+\b', text)
        
        # Calculating the number of sentences, words, and characters
        num_sentences = len(sentences)
        num_words = len(words)
        num_characters = sum(len(word) for word in words)
        
        # Avoiding division by zero
        if num_words == 0 or num_sentences == 0:
            cl_index_scores.append(0.0)
            continue
        
        # Calculating average number of letters per 100 words and sentences per 100 words
        avg_letters_per_100_words = (num_characters / num_words) * 100
        avg_sentences_per_100_words = (num_sentences / num_words) * 100

        # Calculating the Coleman-Liau Index
        score = round(0.0588 * avg_letters_per_100_words - 0.296 * avg_sentences_per_100_words - 15.8, 2)
        cl_index_scores.append(score)

    return cl_index_scores



def calculate_automated_readability_index(texts: Union[str, List[str]]) -> List[float]:
    '''
    Calculate the Automated Readability Index (ARI) for one or multiple texts.

    Inputs:
        - texts (str or list[str]): The input text(s) for which to calculate the ARI.

    Returns:
        - ari_scores (list[float]): A list of ARI scores corresponding to each input text.
    '''
    # Wrapping the input in a list if it is a single string
    if isinstance(texts, str):
        texts = [texts]

    ari_scores = []
    for text in texts:
        # Tokenizing sentences and words
        sentences = tokenize_sentence(text)
        words = re.findall(r'\b\w+\b', text)
        
        # Calculating the number of sentences, words, and characters
        num_sentences = len(sentences)
        num_words = len(words)
        num_characters = sum(len(word) for word in words)
        
        # Avoiding division by zero
        if num_words == 0 or num_sentences == 0:
            ari_scores.append(0.0)
            continue
        
        # Calculating the ARI
        avg_characters_per_word = num_characters / num_words
        avg_words_per_sentence = num_words / num_sentences
        score = round(4.71 * avg_characters_per_word + 0.5 * avg_words_per_sentence - 21.43, 2)
        ari_scores.append(score)

    return ari_scores



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
    gunning_fog_scores = [calculate_gunning_fog_index(text) for text in texts]
    coleman_liau_scores = calculate_coleman_liau_index(texts)
    ari_scores = calculate_automated_readability_index(texts)

    # Combining into a list of dictionaries
    results = []
    for re_score, gl_score, gf_score, cl_score, ari_score in zip(fk_reading_ease_scores, fk_grade_level_scores, gunning_fog_scores, coleman_liau_scores, ari_scores):
        readability_metrics = {
            'flesch_kincaid_reading_ease': re_score,
            'flesch_kincaid_grade_level': gl_score,
            'gunning_fog_index': gf_score,
            'coleman_liau_index': cl_score,
            'automated_readability_index': ari_score
        }
        results.append(readability_metrics)

    return results
