import re
import math
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



def calculate_smog_index(texts: Union[str, List[str]]) -> List[float]:
    '''
    Calculate the SMOG (Simple Measure of Gobbledygook) Index for one or multiple texts.

    The SMOG Index estimates the number of years of education a person needs to understand a piece of text. 
    It is based on the count of complex words (3 or more syllables) per 30 sentences.

    Formula:
    SMOG = 1.043 * sqrt(# of complex words * (30 / # of sentences)) + 3.1291

    Inputs:
        - texts (str or list[str]): The input text(s) to analyze.

    Returns:
        - smog_scores (list[float]): A list of SMOG scores corresponding to each input text.
    '''
    if isinstance(texts, str):
        texts = [texts]

    smog_scores = []
    for text in texts:
        sentences = tokenize_sentence(text)
        words = re.findall(r'\b\w+\b', text)
        num_sentences = len(sentences)
        num_words = len(words)

        if num_sentences == 0 or num_words == 0:
            smog_scores.append(0.0)
            continue

        # Count complex words (3+ syllables)
        complex_words_count = sum(1 for w in words if count_syllables(w) >= 3)

        # Avoid division by zero
        if num_sentences == 0:
            smog_scores.append(0.0)
            continue

        # Apply the SMOG formula
        smog = 1.043 * math.sqrt(complex_words_count * (30 / num_sentences)) + 3.1291
        smog_scores.append(round(smog, 2))

    return smog_scores



def calculate_dale_chall_readability_score(texts: Union[str, List[str]]) -> List[float]:
    '''
    Calculate the Dale-Chall Readability Score for one or multiple texts.

    Dale-Chall estimates grade level based on the percentage of difficult words and average sentence length.
    Difficult words traditionally require a lookup against a known list of easy words. 
    Here, we approximate difficult words as those with 3+ syllables.

    Formula (as provided):
    Dale-Chall = 0.1579 * (percentage_of_difficult_words + 0.0496 * average_words_per_sentence)

    Inputs:
        - texts (str or list[str]): The input text(s).

    Returns:
        - dale_chall_scores (list[float]): A list of Dale-Chall scores.
    '''
    if isinstance(texts, str):
        texts = [texts]

    dale_chall_scores = []
    for text in texts:
        sentences = tokenize_sentence(text)
        words = re.findall(r'\b\w+\b', text)
        num_sentences = len(sentences)
        num_words = len(words)

        if num_sentences == 0 or num_words == 0:
            dale_chall_scores.append(0.0)
            continue

        # Identify difficult words (3+ syllables)
        difficult_words = [w for w in words if count_syllables(w) >= 3]
        percentage_of_difficult_words = (len(difficult_words) / num_words) * 100
        average_words_per_sentence = num_words / num_sentences

        score = 0.1579 * (percentage_of_difficult_words + 0.0496 * average_words_per_sentence)
        dale_chall_scores.append(round(score, 2))

    return dale_chall_scores



def calculate_spache_readability_formula(texts: Union[str, List[str]]) -> List[float]:
    '''
    Calculate the Spache Readability Formula for one or multiple texts.

    The Spache formula is often used for texts intended for children up to about 4th grade. 
    It considers sentence length and the complexity of words. 
    Here, we treat "difficult words" similarly to Dale-Chall (3+ syllables as a proxy).

    Formula:
    Spache = 0.121 * average_sentence_length + 0.082 * average_syllables_per_word - 0.659

    Inputs:
        - texts (str or list[str]): The input text(s).

    Returns:
        - spache_scores (list[float]): A list of Spache formula scores.
    '''
    if isinstance(texts, str):
        texts = [texts]

    spache_scores = []
    for text in texts:
        sentences = tokenize_sentence(text)
        words = re.findall(r'\b\w+\b', text)

        num_sentences = len(sentences)
        num_words = len(words)
        if num_sentences == 0 or num_words == 0:
            spache_scores.append(0.0)
            continue

        num_syllables = sum(count_syllables(w) for w in words)
        average_sentence_length = num_words / num_sentences
        average_syllables_per_word = num_syllables / num_words

        score = 0.121 * average_sentence_length + 0.082 * average_syllables_per_word - 0.659
        spache_scores.append(round(score, 2))

    return spache_scores



def calculate_linsear_write_formula(texts: Union[str, List[str]]) -> List[float]:
    '''
    Calculate the Linsear Write Formula for one or multiple texts.

    The Linsear Write Formula is used to determine the U.S. grade level of a text.
    It categorizes words into easy (fewer than 3 syllables) and hard (3 or more syllables).

    Formula:
    Linsear Write = ((number_of_easy_words + number_of_hard_words) * 2 / number_of_sentences) - 2

    Inputs:
        - texts (str or list[str]): The input text(s).

    Returns:
        - linsear_write_scores (list[float]): A list of Linsear Write scores.
    '''
    if isinstance(texts, str):
        texts = [texts]

    linsear_write_scores = []
    for text in texts:
        sentences = tokenize_sentence(text)
        words = re.findall(r'\b\w+\b', text)

        num_sentences = len(sentences)
        num_words = len(words)
        if num_sentences == 0 or num_words == 0:
            linsear_write_scores.append(0.0)
            continue

        easy_words = [w for w in words if count_syllables(w) < 3]
        hard_words = [w for w in words if count_syllables(w) >= 3]

        score = ((len(easy_words) + len(hard_words)) * 2 / num_sentences) - 2
        linsear_write_scores.append(round(score, 2))

    return linsear_write_scores



def calculate_forcast_readability_formula(texts: Union[str, List[str]]) -> List[float]:
    '''
    Calculate the FORCAST Readability Formula for one or multiple texts.

    The FORCAST formula estimates readability without considering sentence length directly in the traditional sense.
    The given formula is:

    FORCAST = 20 - ((number_of_syllables * 0.1) / number_of_sentences)

    Inputs:
        - texts (str or list[str]): The input text(s).

    Returns:
        - forcast_scores (list[float]): A list of FORCAST scores.
    '''
    if isinstance(texts, str):
        texts = [texts]

    forcast_scores = []
    for text in texts:
        sentences = tokenize_sentence(text)
        words = re.findall(r'\b\w+\b', text)

        num_sentences = len(sentences)
        if num_sentences == 0:
            forcast_scores.append(0.0)
            continue

        num_syllables = sum(count_syllables(w) for w in words)

        score = 20 - ((num_syllables * 0.1) / num_sentences)
        forcast_scores.append(round(score, 2))

    return forcast_scores



def calculate_raygor_readability_estimate(texts: Union[str, List[str]]) -> List[float]:
    '''
    Calculate the Raygor Readability Estimate for one or multiple texts.

    The Raygor formula considers the average words per sentence and the percentage of difficult words.
    As above, we define difficult words as those with >=3 syllables for demonstration.

    Formula:
    Raygor = 0.1579 * average_words_per_sentence + 0.0496 * percentage_of_difficult_words + 3.6365

    Inputs:
        - texts (str or list[str]): The input text(s).

    Returns:
        - raygor_scores (list[float]): A list of Raygor readability estimates.
    '''
    if isinstance(texts, str):
        texts = [texts]

    raygor_scores = []
    for text in texts:
        sentences = tokenize_sentence(text)
        words = re.findall(r'\b\w+\b', text)

        num_sentences = len(sentences)
        num_words = len(words)
        if num_sentences == 0 or num_words == 0:
            raygor_scores.append(0.0)
            continue

        difficult_words = [w for w in words if count_syllables(w) >= 3]
        percentage_of_difficult_words = (len(difficult_words) / num_words) * 100
        average_words_per_sentence = num_words / num_sentences

        score = 0.1579 * average_words_per_sentence + 0.0496 * percentage_of_difficult_words + 3.6365
        raygor_scores.append(round(score, 2))

    return raygor_scores



def calculate_lix_readability_score(texts: Union[str, List[str]]) -> List[float]:
    '''
    Calculate the LIX (Läser–Lätthetsindex) readability score for one or multiple texts.

    The LIX formula uses average sentence length and the percentage of long words (words > 6 letters).

    Formula:
    LIX = (number_of_words / number_of_sentences) + ((number_of_long_words * 100) / number_of_words)

    Inputs:
        - texts (str or list[str]): The input text(s).

    Returns:
        - lix_scores (list[float]): A list of LIX scores.
    '''
    if isinstance(texts, str):
        texts = [texts]

    lix_scores = []
    for text in texts:
        sentences = tokenize_sentence(text)
        words = re.findall(r'\b\w+\b', text)

        num_sentences = len(sentences)
        num_words = len(words)
        if num_sentences == 0 or num_words == 0:
            lix_scores.append(0.0)
            continue

        long_words = [w for w in words if len(w) > 6]
        score = (num_words / num_sentences) + ((len(long_words) * 100) / num_words)
        lix_scores.append(round(score, 2))

    return lix_scores



def calculate_rix_readability_score(texts: Union[str, List[str]]) -> List[float]:
    '''
    Calculate the RIX readability score for one or multiple texts.

    RIX is a simple measure that compares the number of long words to the number of sentences.

    Formula:
    RIX = number_of_long_words / number_of_sentences

    Inputs:
        - texts (str or list[str]): The input text(s).

    Returns:
        - rix_scores (list[float]): A list of RIX scores.
    '''
    if isinstance(texts, str):
        texts = [texts]

    rix_scores = []
    for text in texts:
        sentences = tokenize_sentence(text)
        words = re.findall(r'\b\w+\b', text)

        num_sentences = len(sentences)
        if num_sentences == 0:
            rix_scores.append(0.0)
            continue

        long_words = [w for w in words if len(w) > 6]
        score = len(long_words) / num_sentences
        rix_scores.append(round(score, 2))

    return rix_scores



def calculate_strain_index(texts: Union[str, List[str]]) -> List[float]:
    '''
    Calculate the Strain Index for one or multiple texts.

    The Strain Index measures the concentration of long words relative to the number of sentences.

    Formula:
    Strain Index = (number_of_long_words * 100) / number_of_sentences

    Inputs:
        - texts (str or list[str]): The input text(s).

    Returns:
        - strain_scores (list[float]): A list of Strain Index scores.
    '''
    if isinstance(texts, str):
        texts = [texts]

    strain_scores = []
    for text in texts:
        sentences = tokenize_sentence(text)
        words = re.findall(r'\b\w+\b', text)

        num_sentences = len(sentences)
        if num_sentences == 0:
            strain_scores.append(0.0)
            continue

        long_words = [w for w in words if len(w) > 6]
        score = (len(long_words) * 100) / num_sentences
        strain_scores.append(round(score, 2))

    return strain_scores



def calculate_new_dale_chall_readability_score(texts: Union[str, List[str]]) -> List[float]:
    '''
    Calculate the "New Dale-Chall Readability Score" for one or multiple texts.

    This metric is mentioned in the Readability Consensus Grade formula.
    Since the exact formula was not provided in the prompt, we will use the well-known 
    Dale-Chall formula from literature as the "New Dale-Chall":

    New Dale-Chall = 0.1579 * (percentage_of_difficult_words) + 0.0496 * (average_words_per_sentence) + 3.6365

    Inputs:
        - texts (str or list[str]): The input text(s).

    Returns:
        - new_dale_chall_scores (list[float]): A list of New Dale-Chall scores.
    '''
    if isinstance(texts, str):
        texts = [texts]

    new_dale_chall_scores = []
    for text in texts:
        sentences = tokenize_sentence(text)
        words = re.findall(r'\b\w+\b', text)
        num_sentences = len(sentences)
        num_words = len(words)

        if num_sentences == 0 or num_words == 0:
            new_dale_chall_scores.append(0.0)
            continue

        difficult_words = [w for w in words if count_syllables(w) >= 3]
        percentage_of_difficult_words = (len(difficult_words) / num_words) * 100
        average_words_per_sentence = num_words / num_sentences

        score = 0.1579 * percentage_of_difficult_words + 0.0496 * average_words_per_sentence + 3.6365
        new_dale_chall_scores.append(round(score, 2))

    return new_dale_chall_scores



def calculate_readability_consensus_grade(texts: Union[str, List[str]]) -> List[float]:
    '''
    Calculate the Readability Consensus Grade for one or multiple texts.

    This metric aggregates multiple readability scores and averages them:
    The formula provided is:

    Readability Consensus Grade = 
    (Flesch-Kincaid Grade Level
    + Gunning Fog Index
    + Coleman-Liau Index
    + Automated Readability Index
    + SMOG
    + Dale-Chall Readability Score
    + Spache Readability Formula
    + New Dale-Chall Readability Score
    + Linsear Write Formula
    + FORCAST Readability Formula
    + Raygor Readability Estimate
    + LIX Readability Formula
    + RIX Readability Formula
    + Strain Index) / 14

    Inputs:
        - texts (str or list[str]): The input text(s).

    Returns:
        - consensus_scores (list[float]): A list of consensus scores corresponding to each input text.
    '''
    if isinstance(texts, str):
        texts = [texts]

    # Using the previously defined metrics
    fk_grade_level = calculate_flesch_kincaid_grade_level(texts)
    gunning_fog = [calculate_gunning_fog_index(text) for text in texts]
    coleman_liau = calculate_coleman_liau_index(texts)
    ari = calculate_automated_readability_index(texts)
    smog = calculate_smog_index(texts)
    dale_chall = calculate_dale_chall_readability_score(texts)
    spache = calculate_spache_readability_formula(texts)
    new_dale_chall = calculate_new_dale_chall_readability_score(texts)
    linsear_write = calculate_linsear_write_formula(texts)
    forcast = calculate_forcast_readability_formula(texts)
    raygor = calculate_raygor_readability_estimate(texts)
    lix = calculate_lix_readability_score(texts)
    rix = calculate_rix_readability_score(texts)
    strain = calculate_strain_index(texts)

    consensus_scores = []
    for i in range(len(texts)):
        sum_scores = (fk_grade_level[i] 
                      + gunning_fog[i] 
                      + coleman_liau[i] 
                      + ari[i] 
                      + smog[i]
                      + dale_chall[i] 
                      + spache[i] 
                      + new_dale_chall[i] 
                      + linsear_write[i] 
                      + forcast[i] 
                      + raygor[i] 
                      + lix[i] 
                      + rix[i] 
                      + strain[i])
        
        consensus = sum_scores / 14
        consensus_scores.append(round(consensus, 2))

    return consensus_scores



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
    smog_scores = calculate_smog_index(texts)
    dale_chall_scores = calculate_dale_chall_readability_score(texts)
    spache_scores = calculate_spache_readability_formula(texts)
    new_dale_chall_scores = calculate_new_dale_chall_readability_score(texts)
    linsear_write_scores = calculate_linsear_write_formula(texts)
    forcast_scores = calculate_forcast_readability_formula(texts)
    raygor_scores = calculate_raygor_readability_estimate(texts)
    lix_scores = calculate_lix_readability_score(texts)
    rix_scores = calculate_rix_readability_score(texts)
    strain_scores = calculate_strain_index(texts)
    consensus_scores = calculate_readability_consensus_grade(texts)

    # Combining into a list of dictionaries
    results = []
    for i in range(len(texts)):
        readability_metrics = {
            'flesch_kincaid_reading_ease': fk_reading_ease_scores[i],
            'flesch_kincaid_grade_level': fk_grade_level_scores[i],
            'gunning_fog_index': gunning_fog_scores[i],
            'coleman_liau_index': coleman_liau_scores[i],
            'automated_readability_index': ari_scores[i],
            'smog_index': smog_scores[i],
            'dale_chall_readability_score': dale_chall_scores[i],
            'spache_readability_formula': spache_scores[i],
            'new_dale_chall_readability_score': new_dale_chall_scores[i],
            'linsear_write_formula': linsear_write_scores[i],
            'forcast_readability_formula': forcast_scores[i],
            'raygor_readability_estimate': raygor_scores[i],
            'lix_readability_score': lix_scores[i],
            'rix_readability_score': rix_scores[i],
            'strain_index': strain_scores[i],
            'readability_consensus_grade': consensus_scores[i]
        }
        results.append(readability_metrics)

    return results
