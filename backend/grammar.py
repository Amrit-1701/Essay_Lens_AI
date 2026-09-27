from textblob import TextBlob
import re


def analyze_grammar(text):

    # Create TextBlob object
    blob = TextBlob(text)

    # --------------------------------
    # BASIC SENTENCE ANALYSIS
    # --------------------------------

    sentences = list(blob.sentences)

    sentence_count = len(sentences)

    words = re.findall(r"\b[a-zA-Z]+\b", text)

    word_count = len(words)

    # --------------------------------
    # SPELLING ANALYSIS
    # --------------------------------

    spelling_errors = 0

    corrections = []

    for word in words:

        word_blob = TextBlob(word)

        corrected_word = str(word_blob.correct())

        if corrected_word.lower() != word.lower():

            spelling_errors += 1

            if len(corrections) < 10:

                corrections.append({
                    "word": word,
                    "suggestion": corrected_word
                })

    # --------------------------------
    # ERROR RATE
    # --------------------------------

    if word_count > 0:

        error_rate = spelling_errors / word_count

        grammar_accuracy = max(
            0,
            1 - error_rate
        )

    else:

        grammar_accuracy = 0

    # --------------------------------
    # GRAMMAR SCORE
    # --------------------------------

    grammar_score = grammar_accuracy * 15

    return {

        "sentence_count":
            sentence_count,

        "word_count":
            word_count,

        "spelling_errors":
            spelling_errors,

        "grammar_accuracy":
            round(
                grammar_accuracy * 100,
                2
            ),

        "grammar_score":
            round(
                grammar_score,
                2
            ),

        "corrections":
            corrections
    }


# -----------------------------------
# TEST
# -----------------------------------

if __name__ == "__main__":

    essay = """
    Artificial intelligence are changing education.
    Students is using AI tools for learning.
    It help students understand difficult topics.
    """

    result = analyze_grammar(essay)

    print("\n======================================")
    print("       ESSAYLENS AI GRAMMAR")
    print("======================================")

    print(
        "\nSentence Count :",
        result["sentence_count"]
    )

    print(
        "Word Count     :",
        result["word_count"]
    )

    print(
        "Spelling Issues:",
        result["spelling_errors"]
    )

    print(
        "Grammar Accuracy:",
        result["grammar_accuracy"],
        "%"
    )

    print(
        "Grammar Score  :",
        result["grammar_score"],
        "/ 15"
    )

    print("\nPossible Corrections:")

    for correction in result["corrections"]:

        print(
            correction["word"],
            "→",
            correction["suggestion"]
        )

    print("\n======================================")