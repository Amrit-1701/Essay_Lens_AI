from preprocessing import preprocess
import re


def calculate_features(text):

    result = preprocess(text)

    original_text = result["original_text"]
    sentences = result["sentences"]
    words = result["words"]

    # -----------------------------------------
    # BASIC COUNTS
    # -----------------------------------------

    valid_words = []

    for word in words:

        if word.isalpha():
            valid_words.append(word)

    word_count = len(valid_words)

    unique_words = set(valid_words)

    unique_word_count = len(unique_words)

    sentence_count = len(sentences)

    # -----------------------------------------
    # SENTENCE LENGTH
    # -----------------------------------------

    sentence_lengths = []

    for sentence in sentences:

        count = len(
            [
                word
                for word in sentence.split()
                if word.isalpha()
            ]
        )

        if count > 0:
            sentence_lengths.append(count)

    if sentence_lengths:

        average_sentence_length = (
            sum(sentence_lengths)
            / len(sentence_lengths)
        )

        if len(sentence_lengths) > 1:

            mean = average_sentence_length

            variance = sum(
                (x - mean) ** 2
                for x in sentence_lengths
            ) / len(sentence_lengths)

            sentence_length_variation = variance ** 0.5

        else:
            sentence_length_variation = 0

    else:

        average_sentence_length = 0
        sentence_length_variation = 0

    # -----------------------------------------
    # LEXICAL DIVERSITY
    # -----------------------------------------

    if word_count > 0:
        lexical_diversity = (
            unique_word_count / word_count
        )
    else:
        lexical_diversity = 0

    # -----------------------------------------
    # WORD FEATURES
    # -----------------------------------------

    long_words = [
        word
        for word in valid_words
        if len(word) >= 7
    ]

    if word_count > 0:
        long_word_ratio = (
            len(long_words) / word_count
        )
    else:
        long_word_ratio = 0

    if word_count > 0:

        average_word_length = (
            sum(len(word) for word in valid_words)
            / word_count
        )

    else:
        average_word_length = 0

    # -----------------------------------------
    # STOPWORD RATIO
    # -----------------------------------------

    stopword_count = (
        len(words) - len(result["filtered_words"])
    )

    if len(words) > 0:
        stopword_ratio = (
            stopword_count / len(words)
        )
    else:
        stopword_ratio = 0

    # -----------------------------------------
    # PUNCTUATION
    # -----------------------------------------

    punctuation_count = len(
        re.findall(r"[,.!?;:]", original_text)
    )

    question_count = original_text.count("?")

    exclamation_count = original_text.count("!")

    # -----------------------------------------
    # CAPITALIZATION
    # -----------------------------------------

    capitalized_words = len(
        re.findall(
            r"\b[A-Z][a-zA-Z]+\b",
            original_text
        )
    )

    # -----------------------------------------
    # PARAGRAPHS
    # -----------------------------------------

    paragraphs = [
        paragraph.strip()
        for paragraph in re.split(
            r"\n\s*\n",
            original_text
        )
        if paragraph.strip()
    ]

    paragraph_count = len(paragraphs)

    return {

        "word_count": word_count,

        "sentence_count": sentence_count,

        "unique_word_count": unique_word_count,

        "average_sentence_length":
            round(average_sentence_length, 2),

        "sentence_length_variation":
            round(sentence_length_variation, 2),

        "lexical_diversity":
            round(lexical_diversity, 3),

        "stopword_ratio":
            round(stopword_ratio, 3),

        "long_word_ratio":
            round(long_word_ratio, 3),

        "average_word_length":
            round(average_word_length, 2),

        "punctuation_count":
            punctuation_count,

        "question_count":
            question_count,

        "exclamation_count":
            exclamation_count,

        "capitalized_words":
            capitalized_words,

        "paragraph_count":
            paragraph_count
    }


# -----------------------------------------
# TEST
# -----------------------------------------

if __name__ == "__main__":

    essay = """
    Artificial Intelligence is changing education.

    AI tools help students understand difficult concepts.
    Teachers can also use AI to analyze student performance.

    Therefore, AI can support modern education.
    """

    result = calculate_features(essay)

    print("\n========== FEATURES ==========\n")

    for key, value in result.items():

        print(f"{key:30} : {value}")