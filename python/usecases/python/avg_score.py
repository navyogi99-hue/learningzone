def average_score(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)
kohli_scores = [85, 90, 78, 92, 88]
avg_kohli_score = average_score(kohli_scores)
print(f"Average score for Kohli: {avg_kohli_score}")
dhoni_scores = [80, 85, 82, 88, 90]
average_score(dhoni_scores)
average_score(kohli_scores)
print(average_score(dhoni_scores))