from funny_word_generator import WordGenerator


def test_generator_creates_words() -> None:
    generator = WordGenerator(threshold=1)
    words = generator.generate(count=5)

    assert len(words) == 5
    for word in words:
        assert isinstance(word, str)
        assert len(word) >= 3

def test_generator_high_threshold() -> None:
    generator = WordGenerator(threshold=999)
    words = generator.generate(count=5, max_attempts=50)
    assert len(words) == 0

def test_words_capitalized() -> None:
    generator = WordGenerator(threshold=0)
    words = generator.generate(count=3)
    for word in words:
        assert word[0].isupper()
        assert word[1:].islower()
