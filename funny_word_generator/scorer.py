"""
Модуль для оценки "забавности" (funniness) сгенерированных слов.
"""

from .phonetics import FUNNY_SUFFIXES, HARD_STUFF, RARE_VOWELS, STOP_WORDS


def calculate_funniness(word: str) -> int:
    """
    Рассчитывает баллы "забавности" (F-score) для заданного слова.

    Правила:
    +1 за звук «ы» или «э» (особенно после твердых согласных)
    +1 за повтор «п», «ч» или «ш»
    +1 за присутствие "детского" или нелепого суффикса
    -1 если слово слишком короткое
    -10 за совпадение со стоп-листом

    :param word: Сгенерированное слово.
    :return: Сумма баллов (целое число).
    """
    word = word.lower()
    score = 0

    # Штраф за стоп-лист
    if word in STOP_WORDS:
        score -= 10

    # Бонус за редкие гласные
    score += sum(1 for v in RARE_VOWELS if v in word)

    # Бонус за "тяжелые" согласные
    for hard in HARD_STUFF:
        if hard in word:
            score += 1

    # Бонус за повторения характерных согласных ('п', 'ч', 'ш', 'к')
    for ch in ['п', 'ч', 'ш', 'к']:
        if word.count(ch) >= 2:
            score += 2

    # Бонус за специфичные суффиксы
    for suf in FUNNY_SUFFIXES:
        if word.endswith(suf):
            score += 2
            break

    # Разнообразие звуков (слишком однообразные слова менее смешные)
    unique_chars = len(set(word))
    if unique_chars < 3:
        score -= 2

    return score
