import sys


def score_analytics():
    """
    Processes player scores from command-line arguments and
    displays basic score statistics.
    """
    print("=== Player Score Analytics ===")
    count = len(sys.argv)
    if count == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              "<score1> <score2> ...")
    else:
        try:
            score_list = []
            i = 1
            while i < count:
                score_list += [int(sys.argv[i])]
                i += 1
        except ValueError as e:
            raise e
        print(f"Scores processed: {score_list}")
        print(f"Total players: {count - 1}")
        print(f"Total score: {sum(score_list)}")
        print(f"Average score: {sum(score_list) / (count - 1)}")
        print(f"High score: {max(score_list)}")
        print(f"Low score: {min(score_list)}")
        print(f"Score range: {max(score_list) - min(score_list)}\n")


if __name__ == "__main__":
    try:
        score_analytics()
    except ValueError:
        print("Error! Invalide Score.")
