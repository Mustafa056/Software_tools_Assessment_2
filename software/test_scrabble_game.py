from scrabble_game import calculate_score, is_valid_word


def test_calculate_score():
    
    #Testing if the scrabble scores are correctly calculated
    assert calculate_score("cabbage") == 14, "Error: Score for 'cabbage' should be 14"
    assert calculate_score("quiz") == 22, "Error: Score for 'quiz' should be 22"
    assert calculate_score("apple") == 9, "Error: Score for 'apple' should be 9"
    assert calculate_score("banana") == 8, "Error: Score for 'banana' should be 8"

def test_is_valid_word():

    # Testing if the word is valid in the predefined dictionary
    assert is_valid_word("apple") is True, "Error: 'apple' should be a valid word"
    assert is_valid_word("quiz") is True, "Error: 'quiz' should be a valid word"
    assert is_valid_word("notaword") is False, "Error: 'notaword' should not be a valid word"
    assert is_valid_word("grape") is True, "Error: 'grape' should be a valid word"
