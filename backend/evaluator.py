from features import calculate_features
from grammar import analyze_grammar
from vocabulary import analyze_vocabulary
from organization import analyze_organization
from semantic import calculate_relevance
from feedback import generate_feedback


def calculate_content(features, vocabulary, organization):

    score = 0

    word_count = features["word_count"]
    sentence_count = features["sentence_count"]
    lexical_diversity = vocabulary["lexical_diversity"]

    # Word count
    if word_count >= 250:
        score += 4
    elif word_count >= 150:
        score += 3
    elif word_count >= 100:
        score += 2
    elif word_count >= 50:
        score += 1

    # Sentence count
    if sentence_count >= 8:
        score += 3
    elif sentence_count >= 5:
        score += 2
    elif sentence_count >= 3:
        score += 1

    # Paragraph structure
    if organization["paragraph_count"] >= 3:
        score += 4
    elif organization["paragraph_count"] >= 2:
        score += 2

    # Introduction
    if organization["has_introduction"]:
        score += 2

    # Conclusion
    if organization["has_conclusion"]:
        score += 2

    # Vocabulary diversity
    if lexical_diversity >= 0.70:
        score += 7
    elif lexical_diversity >= 0.50:
        score += 5
    elif lexical_diversity >= 0.30:
        score += 3
    else:
        score += 1

    return min(score, 25)


def evaluate_essay(essay, topic):

    features = calculate_features(essay)

    grammar = analyze_grammar(essay)

    vocabulary = analyze_vocabulary(essay)

    organization = analyze_organization(essay)

    relevance = calculate_relevance(
        essay,
        topic
    )

    content_score = calculate_content(
        features,
        vocabulary,
        organization
    )

    grammar_score = grammar["grammar_score"]

    vocabulary_score = vocabulary["vocabulary_score"]

    organization_score = organization["organization_score"]

    relevance_score = relevance["relevance_score"]

    total_score = (
        content_score
        + relevance_score
        + organization_score
        + grammar_score
        + vocabulary_score
    )

    total_score = min(total_score, 100)

    result = {

        "content": content_score,

        "relevance": relevance_score,

        "organization": organization_score,

        "grammar": grammar_score,

        "vocabulary": vocabulary_score,

        "total": round(total_score, 2),

        "features": features,

        "grammar_details": grammar,

        "vocabulary_details": vocabulary,

        "organization_details": organization,

        "relevance_details": relevance
    }

    result["feedback"] = generate_feedback(result)

    return result


# =====================================================
# INTERACTIVE PROGRAM
# =====================================================

if __name__ == "__main__":

    print("\n")
    print("============================================")
    print("              ESSAYLENS AI")
    print("         Intelligent Essay Evaluator")
    print("============================================")

    print("\nEnter the essay topic.")

    topic = input("\nTopic: ").strip()

    print("\nNow enter your essay.")
    print("Type your essay paragraph by paragraph.")
    print("When finished, type END on a new line.")
    print("--------------------------------------------")

    essay_lines = []

    while True:

        line = input()

        if line.strip().upper() == "END":
            break

        essay_lines.append(line)

    essay = "\n".join(essay_lines).strip()

    # Validation
    if not topic:

        print("\nERROR: Topic cannot be empty.")
        exit()

    if not essay:

        print("\nERROR: Essay cannot be empty.")
        exit()

    print("\nAnalyzing essay...")
    print("Please wait...\n")

    result = evaluate_essay(
        essay,
        topic
    )

    # =================================================
    # RESULT
    # =================================================

    print("============================================")
    print("              ESSAY EVALUATION")
    print("============================================")

    print("\nTOPIC")
    print("--------------------------------------------")
    print(topic)

    print("\nSCORES")
    print("--------------------------------------------")

    print(
        f"Content              : "
        f"{result['content']} / 25"
    )

    print(
        f"Relevance            : "
        f"{result['relevance']} / 20"
    )

    print(
        f"Organization         : "
        f"{result['organization']} / 20"
    )

    print(
        f"Grammar              : "
        f"{result['grammar']} / 15"
    )

    print(
        f"Vocabulary           : "
        f"{result['vocabulary']} / 20"
    )

    print("--------------------------------------------")

    print(
        f"TOTAL SCORE          : "
        f"{result['total']} / 100"
    )

    print("\nFEEDBACK")
    print("--------------------------------------------")

    print(
        result["feedback"]["overall"]
    )

    print("\nObservations:")

    for item in result["feedback"]["feedback"]:

        print(item)

    print("\nSuggestions:")

    for item in result["feedback"]["suggestions"]:

        print("->", item)

    print("\n============================================")
    print("          ANALYSIS COMPLETED")
    print("============================================")