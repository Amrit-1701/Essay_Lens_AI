from features import calculate_features


def analyze_essay(text):

    features = calculate_features(text)

    print("\n")
    print("=" * 55)
    print("              ESSAYLENS AI")
    print("           ESSAY ANALYZER")
    print("=" * 55)

    print("\nESSAY STATISTICS")
    print("-" * 55)

    print(f"{'Word Count':30} : {features['word_count']}")
    print(f"{'Sentence Count':30} : {features['sentence_count']}")
    print(f"{'Unique Words':30} : {features['unique_word_count']}")
    print(
        f"{'Average Sentence Length':30} : "
        f"{features['average_sentence_length']}"
    )
    print(
        f"{'Sentence Length Variation':30} : "
        f"{features['sentence_length_variation']}"
    )

    print("\nVOCABULARY FEATURES")
    print("-" * 55)

    print(
        f"{'Lexical Diversity':30} : "
        f"{features['lexical_diversity']}"
    )

    print(
        f"{'Long Word Ratio':30} : "
        f"{features['long_word_ratio']}"
    )

    print(
        f"{'Average Word Length':30} : "
        f"{features['average_word_length']}"
    )

    print("\nSTRUCTURE FEATURES")
    print("-" * 55)

    print(
        f"{'Paragraph Count':30} : "
        f"{features['paragraph_count']}"
    )

    print(
        f"{'Punctuation Count':30} : "
        f"{features['punctuation_count']}"
    )

    print(
        f"{'Question Count':30} : "
        f"{features['question_count']}"
    )

    print(
        f"{'Exclamation Count':30} : "
        f"{features['exclamation_count']}"
    )

    print(
        f"{'Capitalized Words':30} : "
        f"{features['capitalized_words']}"
    )

    print("\n")
    print("=" * 55)


if __name__ == "__main__":

    essay = """
    Artificial intelligence is becoming an important part of modern education.

    It can help students understand difficult concepts and provide personalized
    learning experiences. Students can use intelligent systems to practice
    questions and receive immediate feedback.

    Teachers can also use artificial intelligence to prepare learning materials
    and identify areas where students need additional support.

    However, AI should be used carefully. Students should not become completely
    dependent on technology. Human teachers continue to play an important role
    in education because they provide guidance, motivation and emotional support.

    Therefore, artificial intelligence should be treated as a tool that supports
    teachers and students rather than replacing them.
    """

    analyze_essay(essay)