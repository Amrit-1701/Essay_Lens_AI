from preprocessing import preprocess


def analyze_vocabulary(text):

    result = preprocess(text)

    words = result["words"]

    # Keep only normal alphabetic words
    valid_words = []

    for word in words:
        if word.isalpha():
            valid_words.append(word.lower())

    total_words = len(valid_words)

    # Find unique words
    unique_words = set(valid_words)
    unique_word_count = len(unique_words)

    # Lexical diversity
    if total_words > 0:
        lexical_diversity = unique_word_count / total_words
    else:
        lexical_diversity = 0

    # Count long words
    long_words = []

    for word in valid_words:
        if len(word) >= 7:
            long_words.append(word)

    if total_words > 0:
        long_word_ratio = len(long_words) / total_words
    else:
        long_word_ratio = 0

    # Vocabulary score out of 20
    vocabulary_quality = (
        lexical_diversity * 0.7
        + long_word_ratio * 0.3
    )

    vocabulary_quality = min(vocabulary_quality, 1)

    vocabulary_score = vocabulary_quality * 20

    return {
        "total_words": total_words,
        "unique_words": unique_word_count,
        "lexical_diversity": round(lexical_diversity, 3),
        "long_word_ratio": round(long_word_ratio, 3),
        "vocabulary_score": round(vocabulary_score, 2)
    }


if __name__ == "__main__":

    essay = """
    Artificial intelligence provides personalized educational
    experiences for students. Intelligent systems can analyze
    learning patterns and provide useful recommendations.
    """

    result = analyze_vocabulary(essay)

    print("\n========== VOCABULARY ANALYSIS ==========\n")

    for key, value in result.items():
        print(f"{key:25} : {value}")