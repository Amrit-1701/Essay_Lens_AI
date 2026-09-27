from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re


def calculate_relevance(essay, topic):

    # -------------------------------------------------
    # Clean topic and essay
    # -------------------------------------------------

    topic = topic.lower().strip()
    essay = essay.lower().strip()


    # -------------------------------------------------
    # Extract important words from topic
    # -------------------------------------------------

    topic_words = re.findall(
        r"\b[a-zA-Z]{3,}\b",
        topic
    )


    # Remove very common words
    common_words = {
        "the",
        "and",
        "for",
        "with",
        "from",
        "into",
        "about",
        "impact",
        "effect",
        "role",
        "importance"
    }


    important_topic_words = [

        word
        for word in topic_words
        if word not in common_words

    ]


    # -------------------------------------------------
    # TF-IDF similarity
    # -------------------------------------------------

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )


    try:

        vectors = vectorizer.fit_transform(
            [
                topic,
                essay
            ]
        )


        similarity = cosine_similarity(
            vectors[0:1],
            vectors[1:2]
        )[0][0]


    except ValueError:

        similarity = 0


    # -------------------------------------------------
    # Keyword coverage
    # -------------------------------------------------

    essay_words = set(
        re.findall(
            r"\b[a-zA-Z]{3,}\b",
            essay
        )
    )


    if important_topic_words:

        matched_words = [

            word
            for word in important_topic_words
            if word in essay_words

        ]


        keyword_coverage = (
            len(matched_words)
            / len(set(important_topic_words))
        )

    else:

        keyword_coverage = 0


    # -------------------------------------------------
    # Combined relevance
    # -------------------------------------------------

    combined_score = (

        (similarity * 0.40)
        +
        (keyword_coverage * 0.60)

    )


    # -------------------------------------------------
    # Convert to /20
    # -------------------------------------------------

    relevance_score = (
        combined_score * 20
    )


    # -------------------------------------------------
    # Small calibration
    #
    # Relevant essays should not receive
    # extremely low scores simply because
    # the topic phrase is short.
    # -------------------------------------------------

    if keyword_coverage >= 0.75:

        relevance_score += 5

    elif keyword_coverage >= 0.50:

        relevance_score += 3

    elif keyword_coverage >= 0.25:

        relevance_score += 1


    relevance_score = min(
        relevance_score,
        20
    )


    return {

        "similarity":
            round(
                float(similarity),
                3
            ),

        "keyword_coverage":
            round(
                float(keyword_coverage),
                3
            ),

        "relevance_score":
            round(
                float(relevance_score),
                2
            )
    }