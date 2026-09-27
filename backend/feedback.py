def generate_feedback(result):

    feedback = []
    suggestions = []

    # -----------------------------------------
    # CONTENT
    # -----------------------------------------

    content = result["content"]

    if content >= 20:
        feedback.append("✓ Good content development.")
    elif content >= 15:
        feedback.append("✓ Content is reasonably developed.")
        suggestions.append(
            "Develop your ideas with more supporting details."
        )
    else:
        feedback.append("⚠ Content development is limited.")
        suggestions.append(
            "Add more explanations, examples and supporting ideas."
        )

    # -----------------------------------------
    # RELEVANCE
    # -----------------------------------------

    relevance = result["relevance"]

    if relevance >= 16:
        feedback.append("✓ Essay is strongly related to the topic.")
    elif relevance >= 10:
        feedback.append("⚠ Essay has moderate topic relevance.")
        suggestions.append(
            "Keep the main discussion more closely connected to the topic."
        )
    else:
        feedback.append("⚠ Essay has low topic relevance.")
        suggestions.append(
            "Focus more directly on the given topic."
        )

    # -----------------------------------------
    # ORGANIZATION
    # -----------------------------------------

    organization = result["organization"]

    if organization >= 17:
        feedback.append("✓ Essay has good organization.")
    elif organization >= 12:
        feedback.append("⚠ Essay organization can be improved.")
        suggestions.append(
            "Improve the flow between introduction, body and conclusion."
        )
    else:
        feedback.append("⚠ Essay structure needs improvement.")
        suggestions.append(
            "Use a clear introduction, body paragraphs and conclusion."
        )

    # -----------------------------------------
    # GRAMMAR
    # -----------------------------------------

    grammar = result["grammar"]

    if grammar >= 13:
        feedback.append("✓ Grammar and spelling are generally good.")
    elif grammar >= 9:
        feedback.append("⚠ Some language errors were detected.")
        suggestions.append(
            "Review spelling and sentence construction."
        )
    else:
        feedback.append("⚠ Several language errors were detected.")
        suggestions.append(
            "Carefully check grammar, spelling and sentence structure."
        )

    # -----------------------------------------
    # VOCABULARY
    # -----------------------------------------

    vocabulary = result["vocabulary"]

    if vocabulary >= 17:
        feedback.append("✓ Good vocabulary diversity.")
    elif vocabulary >= 12:
        feedback.append("⚠ Vocabulary diversity is moderate.")
        suggestions.append(
            "Try using more varied and precise words."
        )
    else:
        feedback.append("⚠ Vocabulary diversity is limited.")
        suggestions.append(
            "Avoid repeating the same words and expand vocabulary."
        )

    # -----------------------------------------
    # GENERAL SCORE
    # -----------------------------------------

    total = result["total"]

    if total >= 85:
        overall = "Excellent overall performance."
    elif total >= 70:
        overall = "Good overall performance with some areas to improve."
    elif total >= 50:
        overall = "Average performance. Several areas need improvement."
    else:
        overall = "The essay needs significant improvement."

    return {
        "feedback": feedback,
        "suggestions": suggestions,
        "overall": overall
    }


# -----------------------------------------
# TEST
# -----------------------------------------

if __name__ == "__main__":

    sample_result = {
        "content": 20,
        "relevance": 17,
        "organization": 18,
        "grammar": 13,
        "vocabulary": 16,
        "total": 84
    }

    result = generate_feedback(sample_result)

    print("\n========== ESSAYLENS AI FEEDBACK ==========\n")

    print("Overall:")
    print(result["overall"])

    print("\nFeedback:")

    for item in result["feedback"]:
        print(item)

    print("\nSuggestions:")

    for item in result["suggestions"]:
        print("→", item)