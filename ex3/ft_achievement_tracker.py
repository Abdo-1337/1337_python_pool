data = {
                            "alice": {
                                        "first_kill",
                                        "treasure_hunter",
                                        "speed_demon",
                                        "level_10",
                                        "first_kill",
                                        "first_kill",
                            },
                            "bob": {
                                        "level_10",
                                        "boss_slayer",
                                        "collector",
                                        "level_10",
                                        "first_kill",
                                        "level_10",
                            },
                            "charlie": {
                                        "treasure_hunter",
                                        "boss_slayer",
                                        "speed_demon",
                                        "level_10",
                                        "boss_slayer",
                                        "perfectionist",
                                        "level_10",
                                        "boss_slayer",
                                        "level_10",
                            },
    }


def ft_achievement_tracker():
    """
    Tracks and analyzes player achievements using sets.

    - Stores each player's achievements as a set to remove duplicates.
    - Computes all unique achievements across players.
    - Finds achievements common to all players using set intersection.
    - Identifies rare achievements owned by only one player.
    - Compares achievements between players (common and unique).
    """
    print("=== Achievement Tracker System ===\n")

    print("Player alice achievements: "
          f"{data['alice']}")
    print("Player bob achievements: "
          f"{data['bob']}")
    print("Player bob achievements: "
          f"{data['charlie']}")

    print("=== Achievement Analytics ===\n")

    all_achievements = set()
    for one_player_ach in data.values():
        all_achievements = all_achievements.union(one_player_ach)
    print("All unique achievements: ", all_achievements)
    print(f"Total unique achievements: {len(all_achievements)}\n")

    common_achievements = set.intersection(*data.values())
    print("Common to all players:", common_achievements)

    alice_only = data["alice"].difference(data["bob"].union(data["charlie"]))
    bob_only = data["bob"].difference(data["alice"].union(data["charlie"]))
    charlie_only = data["charlie"].difference(data["alice"].union(data["bob"]))
    rare_achievements = alice_only.union(bob_only, charlie_only)
    print(f"Rare achievements (1 player): {rare_achievements}\n")

    print(f"Alice vs Bob common: {data['alice'].intersection(data['bob'])}")
    print(f"Alice unique: {data['alice'].difference(data['bob'])}")
    print(f"Bob unique: {data['bob'].difference(data['alice'])}")


if __name__ == "__main__":
    ft_achievement_tracker()
