from decimal import Decimal
from typing import Callable
import re

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 та 154 доларів."


def generate_numbers(text: str):
    """Generate numbers from the string"""
    for match in re.finditer(r'\b\d+\.\d+\b|\b\d+\b', text):
        yield Decimal(match.group())

def sum_profit(text: str, func: Callable[[str], Decimal]) -> Decimal:
    """Calculate the sum of numbers from generator"""
    return sum(func(text))



if __name__ == "__main__":
    total = sum_profit(text, generate_numbers)
    print(f"Загальна сума доходу: {total}")




