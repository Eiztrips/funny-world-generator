"""
Модуль с основным классом генерации смешных слов.
"""

import random

from .phonetics import FUNNY_SUFFIXES, HARD_STUFF, NORMAL_CONS, NORMAL_VOWELS, RARE_VOWELS
from .scorer import calculate_funniness


class WordGenerator:
    """
    Генератор слов на основе фонетических шаблонов.
    """

    def __init__(self, threshold: int = 3) -> None:
        """
        Инициализация генератора.

        :param threshold: Минимальный балл "забавности" (F-score) для прохождения фильтра.
        """
        self.threshold = threshold
        self.all_cons = HARD_STUFF + NORMAL_CONS
        self.all_vowels = RARE_VOWELS + NORMAL_VOWELS

    def _generate_candidate(self) -> str:
        """
        Внутренняя функция создания одного кандидата по шаблону.
        Шаблоны типа: (Согласная + Гласная) + Смешной суффикс
        """
        # Вероятностный выбор шаблона
        pattern_type = random.choice([1, 2, 3])

        word = ""

        if pattern_type == 1:
            # Шаблон CV + Suffix (напр. "Шо" + "кып")
            word += random.choice(HARD_STUFF)
            word += random.choice(self.all_vowels)
            if random.random() > 0.5:
                word += random.choice(HARD_STUFF)
            else:
                word += random.choice(NORMAL_CONS)
            word += random.choice(FUNNY_SUFFIXES)
        elif pattern_type == 2:
            # Шаблон CVC + Suffix
            word += random.choice(HARD_STUFF)
            word += random.choice(NORMAL_VOWELS)
            word += random.choice(HARD_STUFF)
            word += random.choice(FUNNY_SUFFIXES)
        else:
            # Шаблон CV + CV + редкий гласный
            word += random.choice(self.all_cons)
            word += random.choice(RARE_VOWELS)
            word += random.choice(HARD_STUFF)
            word += random.choice(NORMAL_VOWELS)

        return word.capitalize()

    def generate(self, count: int = 5, max_attempts: int = 1000) -> list[str]:
        """
        Генерирует список забавных слов, прошедших порог (threshold).

        :param count: Требуемое количество слов.
        :param max_attempts: Максимальное количество попыток генерации.
        :return: Список сгенерированных слов.
        """
        results: list[str] = []
        attempts = 0

        while len(results) < count and attempts < max_attempts:
            attempts += 1
            candidate = self._generate_candidate()
            score = calculate_funniness(candidate)

            if score >= self.threshold and candidate not in results:
                results.append(candidate)

        # Сортировка по убыванию F-score (вычисляем заново для ключа сортировки)
        results.sort(key=calculate_funniness, reverse=True)
        return results
