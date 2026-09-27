import nltk
import re


# -----------------------------------------
# CHECK REQUIRED NLTK DATA
# -----------------------------------------

def setup_nltk():

    resources = [
        ("tokenizers/punkt", "punkt"),
        ("tokenizers/punkt_tab", "punkt_tab"),
        ("corpora/stopwords", "stopwords")
    ]

    for path, package in resources:

        try:
            nltk.data.find(path)

        except LookupError:
            print(f"Downloading NLTK resource: {package}")
            nltk.download(package, quiet=True)


setup_nltk()


# -----------------------------------------
# PREPROCESSING
# -----------------------------------------

def preprocess(text):

    original_text = text

    # Lowercase version for NLP
    clean_text = text.lower()

    # Remove extra spaces
    clean_text = re.sub(r"\s+", " ", clean_text).strip()

    # Sentence tokenization
    sentences = nltk.sent_tokenize(clean_text)

    # Word tokenization
    words = nltk.word_tokenize(clean_text)

    # Stopwords
    stop_words = set(
        nltk.corpus.stopwords.words("english")
    )

    filtered_words = []

    for word in words:

        if word.isalpha() and word not in stop_words:
            filtered_words.append(word)

    return {
        "original_text": original_text,
        "text": clean_text,
        "sentences": sentences,
        "words": words,
        "filtered_words": filtered_words
    }


# -----------------------------------------
# TEST
# -----------------------------------------

if __name__ == "__main__":

    sample = """
    Artificial Intelligence is changing modern education.
    Students can use AI to improve their learning experience.
    """

    result = preprocess(sample)

    print("\n========== PREPROCESSING ==========\n")

    print("Sentences:")
    print(result["sentences"])

    print("\nWords:")
    print(result["words"])

    print("\nFiltered Words:")
    print(result["filtered_words"])