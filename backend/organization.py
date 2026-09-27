from preprocessing import preprocess
import re


def analyze_organization(text):

    result = preprocess(text)

    sentences = result["sentences"]


    # -------------------------------------------------
    # Extract paragraphs
    # -------------------------------------------------

    paragraphs = [

        paragraph.strip()

        for paragraph in re.split(
            r"\n\s*\n",
            text.strip()
        )

        if paragraph.strip()

    ]


    paragraph_count = len(paragraphs)


    # -------------------------------------------------
    # Sentence count per paragraph
    # -------------------------------------------------

    paragraph_sentence_counts = []


    for paragraph in paragraphs:

        paragraph_sentences = preprocess(
            paragraph
        )["sentences"]


        paragraph_sentence_counts.append(
            len(paragraph_sentences)
        )


    # -------------------------------------------------
    # Introduction
    # -------------------------------------------------

    has_introduction = (
        paragraph_count >= 1
    )


    # -------------------------------------------------
    # Body
    # -------------------------------------------------

    has_body = (
        paragraph_count >= 2
    )


    # -------------------------------------------------
    # Conclusion detection
    # -------------------------------------------------

    conclusion_words = [

        "in conclusion",
        "to conclude",
        "therefore",
        "overall",
        "finally",
        "thus",
        "in summary",
        "to sum up"

    ]


    has_conclusion = False


    if paragraph_count >= 2:

        last_paragraph = paragraphs[-1].lower()


        for phrase in conclusion_words:

            if phrase in last_paragraph:

                has_conclusion = True

                break


    # If there are 3 or more reasonably
    # structured paragraphs, consider the
    # final paragraph as a possible conclusion.

    if paragraph_count >= 3:

       if paragraph_sentence_counts[-1] >= 2:

          has_conclusion = True


    # -------------------------------------------------
    # Paragraph balance
    # -------------------------------------------------

    balance_score = 0


    if paragraph_count >= 3:

        non_empty_counts = [

            count
            for count
            in paragraph_sentence_counts
            if count > 0

        ]


        if non_empty_counts:

            maximum = max(
                non_empty_counts
            )

            minimum = min(
                non_empty_counts
            )


            if maximum - minimum <= 3:

                balance_score = 3

            elif maximum - minimum <= 5:

                balance_score = 2

            else:

                balance_score = 1


    elif paragraph_count == 2:

        balance_score = 1


    # -------------------------------------------------
    # Transition words
    # -------------------------------------------------

    transition_words = [

        "however",
        "therefore",
        "moreover",
        "furthermore",
        "additionally",
        "although",
        "because",
        "thus",
        "also",
        "therefore",
        "finally",
        "in addition",
        "on the other hand"

    ]


    text_lower = text.lower()


    transition_count = 0


    for word in transition_words:

        if word in text_lower:

            transition_count += 1


    transition_score = min(
        transition_count,
        3
    )


    # -------------------------------------------------
    # Sentence distribution
    # -------------------------------------------------

    distribution_score = 0


    if paragraph_count >= 3:

        valid_paragraphs = [

            count
            for count
            in paragraph_sentence_counts
            if count >= 2

        ]


        if len(valid_paragraphs) >= 3:

            distribution_score = 3

        elif len(valid_paragraphs) == 2:

            distribution_score = 2

        else:

            distribution_score = 1


    elif paragraph_count == 2:

        if all(
            count >= 2
            for count
            in paragraph_sentence_counts
        ):

            distribution_score = 2

        else:

            distribution_score = 1


    # -------------------------------------------------
    # Calculate organization score
    # -------------------------------------------------

    score = 0


    # Introduction
    if has_introduction:

        score += 3


    # Body
    if has_body:

        score += 3


    # Conclusion
    if has_conclusion:

        score += 4


    # Paragraph structure
    if paragraph_count >= 3:

        score += 3

    elif paragraph_count == 2:

        score += 2


    # Paragraph balance
    score += balance_score


    # Transitions
    score += transition_score


    # Sentence distribution
    score += distribution_score


    # -------------------------------------------------
    # Penalize extremely short essays
    # -------------------------------------------------

    total_words = len(
        [
            word
            for word in result["words"]
            if word.isalpha()
        ]
    )


    if total_words < 40:

        score -= 5

    elif total_words < 70:

        score -= 3


    # -------------------------------------------------
    # Final score
    # -------------------------------------------------

    organization_score = max(
        0,
        min(score, 20)
    )


    return {

        "paragraph_count":
            paragraph_count,

        "sentence_count":
            len(sentences),

        "has_introduction":
            has_introduction,

        "has_body":
            has_body,

        "has_conclusion":
            has_conclusion,

        "transition_count":
            transition_count,

        "paragraph_sentence_counts":
            paragraph_sentence_counts,

        "organization_score":
            organization_score
    }


if __name__ == "__main__":

    essay = """

    Artificial intelligence is changing education.
    It provides new opportunities for students.

    Teachers can use AI tools to support learning.
    Students can also use technology to understand
    difficult concepts.

    Therefore, AI should be used carefully in education.
    """

    result = analyze_organization(
        essay
    )


    print(
        "\n========== ORGANIZATION ==========\n"
    )


    for key, value in result.items():

        print(
            f"{key:30} : {value}"
        )