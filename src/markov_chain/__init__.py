from typing import Sequence

from .markov import MarkovChain

__all__ = [
    "MarkovChain",
]


def create[T](items: Sequence[T]) -> MarkovChain[T]:
    return MarkovChain.create(items)
