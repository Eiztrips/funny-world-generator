"""
Интерфейс командной строки для генератора слов.
"""

import argparse
import sys

from .generator import WordGenerator


def main() -> None:
    """Точка входа для CLI."""
    parser = argparse.ArgumentParser(
        description="funny-words: Генератор смешных и нелепых слов."
    )

    parser.add_argument(
        "-c", "--count",
        type=int,
        default=5,
        help="Количество слов для генерации (по умолчанию: 5)"
    )
    parser.add_argument(
        "-t", "--threshold",
        type=int,
        default=3,
        help="Минимальный порог забавности (по умолчанию: 3)"
    )

    args = parser.parse_args()

    if args.count <= 0:
        print("Ошибка: количество слов должно быть больше нуля.", file=sys.stderr)
        sys.exit(1)

    generator = WordGenerator(threshold=args.threshold)
    words = generator.generate(count=args.count)

    if not words:
        print(f"Не удалось сгенерировать слова с порогом забавности {args.threshold}. "
              "Попробуйте снизить порог.", file=sys.stderr)
        sys.exit(1)

    print(f"Сгенерировано {len(words)} забавных слов (Порог: {args.threshold}):")
    print("-" * 40)
    for w in words:
        print(w)


if __name__ == "__main__":
    main()
