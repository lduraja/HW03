import pytest
import random

from assignment_3_1 import play_rock_paper_scissor


@pytest.mark.parametrize(
    ("user_name", "user_choice", "test_seed", "expected_winner"),
    [
        ("michal", "Paper", 1, "Michal"),
        ("MICHAL", "paper", 2, "Michal"),
    ]
)
def test_user_name(user_name, user_choice, test_seed, expected_winner):
    random.seed(test_seed)
    assert play_rock_paper_scissor(user_name, user_choice) == expected_winner


@pytest.mark.parametrize(
    ("user_name", "user_choice", "test_seed", "expected_winner"),
    [
        ("Michal", "paper", 1, "Michal"),
        ("Michal", "rock", 0, "computer"),
        ("Michal", "rock", 5, "Michal"),
        ("Michal", "scissors", 2, "computer"),
        ("Michal", "scissors", 7, "Michal"),
        ("Michal", "paper", 6, "computer"),
        ("Michal", "rock", 3, "Tie"),
        ("Michal", "paper", 9, "Tie"),
        ("Michal", "scissors", 10, "Tie"),
        ("michal", "rock", 3, "Tie"),
        ("Michal", "Paper", 9, "Tie"),
        ("Michal", "scissor", 10, None),
        ("michal", "", 10, None),
    ]
)
def test_play_game(user_name, user_choice, test_seed, expected_winner):
    random.seed(test_seed)
    assert play_rock_paper_scissor(user_name, user_choice) == expected_winner
