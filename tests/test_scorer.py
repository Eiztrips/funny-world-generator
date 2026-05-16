from funny_word_generator.scorer import calculate_funniness


def test_funniness_score_stop_words() -> None:
    score = calculate_funniness("привет")
    assert score < 0  # Срабатывает стоп-лист

def test_funniness_rare_vowels_and_hard_stuff() -> None:
    # 'ш' (твердая, +1), 'о' (обычная), 'к' (твердая, +1), 'ы' (редкая, +1), 'п' (твердая, +1)
    # Повтор? Нет. Итого: > 0
    score = calculate_funniness("шокып")
    assert score >= 3

def test_funniness_funny_suffix() -> None:
    test_word = "абуып" # оканчивается на 'ып' (+2)
    score1 = calculate_funniness(test_word)
    score2 = calculate_funniness("абуот")
    assert score1 > score2
