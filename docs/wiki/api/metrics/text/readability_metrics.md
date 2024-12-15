# Readabilty Metrics API Reference
This page documents the available functions for computing various readability metrics. All functions accept either a single string or a list of strings as input. When provided with a single string, it will be treated as a single text input; when provided with a list of strings, the function will compute results for each text and return a list of results.

For a conceptual understanding of what all these functions are doing, please see the following page: [Readability Metrics](../../../metrics/text/readability_metrics.md)

**Module:** `readability_metrics`

**Dependencies:**  
- `re`  
- `math`  
- `typing.Union, typing.List`  
- `whetstone.utils.text.text_parsers.tokenize_sentence, count_syllables`

**Input Parameters:**  
- `texts (str | list[str])`: The text or texts for which to compute the metric(s).  
- Each text is expected to be a string of English words and punctuation.

**Output:**  
- Most functions return a `list[float]` corresponding to the scores for each input text.  
- For metrics that only accept a single string, a single `float` is returned.

**Error Handling:**  
- If the text is empty or no valid sentences/words are found, functions typically return `[0.0]` or `0.0` depending on the function.

---

## Functions

### calculate_flesch_kincaid_reading_ease

**Description:**  
Computes the Flesch-Kincaid Reading Ease score (0–100 scale) for one or multiple texts. Higher scores indicate easier readability.

**Signature:**  
```python
calculate_flesch_kincaid_reading_ease(texts: Union[str, List[str]]) -> List[float]
```

**Parameters:**  
- `texts (str | list[str])`: One or multiple texts to analyze.

**Returns:**  
- `list[float]`: A list of Flesch-Kincaid Reading Ease scores.

---

### calculate_flesch_kincaid_grade_level

**Description:**  
Computes the Flesch-Kincaid Grade Level, indicating the U.S. school grade level required to understand the text.

**Signature:**  
```python
calculate_flesch_kincaid_grade_level(texts: Union[str, List[str]]) -> List[float]
```

**Parameters:**  
- `texts (str | list[str])`: One or multiple texts to analyze.

**Returns:**  
- `list[float]`: A list of Flesch-Kincaid Grade Level scores.

---

### calculate_gunning_fog_index

**Description:**  
Computes the Gunning Fog Index, representing the number of years of education required to understand the text on first reading.

**Signature:**  
```python
calculate_gunning_fog_index(text: str) -> float
```

**Parameters:**  
- `text (str)`: The text to analyze.

**Returns:**  
- `float`: The Gunning Fog Index score.

**Note:**  
This function currently only supports a single text input, not a list.

---

### calculate_coleman_liau_index

**Description:**  
Computes the Coleman-Liau Index, providing a grade-level estimate based on the average number of letters per 100 words and sentences per 100 words.

**Signature:**  
```python
calculate_coleman_liau_index(texts: Union[str, List[str]]) -> List[float]
```

**Parameters:**  
- `texts (str | list[str])`: One or multiple texts to analyze.

**Returns:**  
- `list[float]`: A list of Coleman-Liau Index scores.

---

### calculate_automated_readability_index

**Description:**  
Computes the Automated Readability Index (ARI), providing a grade-level estimate based on characters per word and words per sentence.

**Signature:**  
```python
calculate_automated_readability_index(texts: Union[str, List[str]]) -> List[float]
```

**Parameters:**  
- `texts (str | list[str])`: One or multiple texts to analyze.

**Returns:**  
- `list[float]`: A list of ARI scores.

---

### calculate_smog_index

**Description:**  
Computes the SMOG (Simple Measure of Gobbledygook) Index, estimating the years of education needed to understand the text based on the frequency of complex words.

**Signature:**  
```python
calculate_smog_index(texts: Union[str, List[str]]) -> List[float]
```

**Parameters:**  
- `texts (str | list[str])`: One or multiple texts to analyze.

**Returns:**  
- `list[float]`: A list of SMOG Index scores.

---

### calculate_dale_chall_readability_score

**Description:**  
Computes the Dale-Chall Readability Score, estimating grade level based on sentence length and percentage of difficult words.

**Signature:**  
```python
calculate_dale_chall_readability_score(texts: Union[str, List[str]]) -> List[float]
```

**Parameters:**  
- `texts (str | list[str])`: One or multiple texts to analyze.

**Returns:**  
- `list[float]`: A list of Dale-Chall scores.

---

### calculate_spache_readability_formula

**Description:**  
Computes the Spache Readability Formula, often used for younger readers, based on sentence length and syllable complexity.

**Signature:**  
```python
calculate_spache_readability_formula(texts: Union[str, List[str]]) -> List[float]
```

**Parameters:**  
- `texts (str | list[str])`: One or multiple texts to analyze.

**Returns:**  
- `list[float]`: A list of Spache formula scores.

---

### calculate_linsear_write_formula

**Description:**  
Computes the Linsear Write Formula, which estimates grade level by classifying words as “easy” or “hard” and relating this to sentence length.

**Signature:**  
```python
calculate_linsear_write_formula(texts: Union[str, List[str]]) -> List[float]
```

**Parameters:**  
- `texts (str | list[str])`: One or multiple texts to analyze.

**Returns:**  
- `list[float]`: A list of Linsear Write scores.

---

### calculate_forcast_readability_formula

**Description:**  
Computes the FORCAST Readability Formula, which differs from many other metrics and uses syllable counts in a unique manner.

**Signature:**  
```python
calculate_forcast_readability_formula(texts: Union[str, List[str]]) -> List[float]
```

**Parameters:**  
- `texts (str | list[str])`: One or multiple texts to analyze.

**Returns:**  
- `list[float]`: A list of FORCAST scores.

---

### calculate_raygor_readability_estimate

**Description:**  
Computes the Raygor Readability Estimate, based on average words per sentence and the percentage of difficult words.

**Signature:**  
```python
calculate_raygor_readability_estimate(texts: Union[str, List[str]]) -> List[float]
```

**Parameters:**  
- `texts (str | list[str])`: One or multiple texts to analyze.

**Returns:**  
- `list[float]`: A list of Raygor readability estimates.

---

### calculate_lix_readability_score

**Description:**  
Computes the LIX (Läser–Lätthetsindex) score, a metric that uses sentence length and the percentage of long words to gauge complexity.

**Signature:**  
```python
calculate_lix_readability_score(texts: Union[str, List[str]]) -> List[float]
```

**Parameters:**  
- `texts (str | list[str])`: One or multiple texts to analyze.

**Returns:**  
- `list[float]`: A list of LIX scores.

---

### calculate_rix_readability_score

**Description:**  
Computes the RIX score, based on the ratio of long words to the number of sentences.

**Signature:**  
```python
calculate_rix_readability_score(texts: Union[str, List[str]]) -> List[float]
```

**Parameters:**  
- `texts (str | list[str])`: One or multiple texts to analyze.

**Returns:**  
- `list[float]`: A list of RIX scores.

---

### calculate_strain_index

**Description:**  
Computes the Strain Index, measuring the concentration of long words relative to sentences.

**Signature:**  
```python
calculate_strain_index(texts: Union[str, List[str]]) -> List[float]
```

**Parameters:**  
- `texts (str | list[str])`: One or multiple texts to analyze.

**Returns:**  
- `list[float]`: A list of Strain Index scores.

---

### calculate_new_dale_chall_readability_score

**Description:**  
Computes the “New Dale-Chall” Readability Score, a variation of the traditional Dale-Chall metric with an additional constant.

**Signature:**  
```python
calculate_new_dale_chall_readability_score(texts: Union[str, List[str]]) -> List[float]
```

**Parameters:**  
- `texts (str | list[str])`: One or multiple texts to analyze.

**Returns:**  
- `list[float]`: A list of New Dale-Chall scores.

---

### calculate_readability_consensus_grade

**Description:**  
Computes a consensus grade level by averaging multiple readability metrics into a single score.

**Signature:**  
```python
calculate_readability_consensus_grade(texts: Union[str, List[str]]) -> List[float]
```

**Parameters:**  
- `texts (str | list[str])`: One or multiple texts to analyze.

**Returns:**  
- `list[float]`: A list of consensus scores, averaging numerous metrics.

---

# Example Usage

```python
texts = [
    "This is a simple sentence suitable for many readers.",
    "Incorporating intricate vocabulary and extensive, subordinate clauses can significantly elevate the complexity of textual comprehension."
]

# Compute a single metric
fk_scores = calculate_flesch_kincaid_grade_level(texts)
print("Flesch-Kincaid Grade Levels:", fk_scores)

# Compute multiple metrics and compare
readability_report = calculate_all_readability_metrics(texts)
print("All Metrics:", readability_report)
```