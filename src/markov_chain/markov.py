import random
from dataclasses import dataclass
from typing import Iterable, MutableMapping, Sequence


@dataclass
class MarkovChain[T]:
    count_matrix: MutableMapping[T, MutableMapping[T, int]]
    probability_matrix: MutableMapping[T, MutableMapping[T, float]]

    @classmethod
    def create(cls, entries: Sequence[T]) -> "MarkovChain":
        count_matrix: MutableMapping[T, MutableMapping[T, int]] = {}
        for index in range(len(entries) - 1):
            current = entries[index]
            next = entries[index + 1]
            translations: MutableMapping[T, int] = count_matrix.get(current, {})
            if next not in translations:
                translations[next] = 0
            translations[next] += 1
            count_matrix[current] = translations

        probability_matrix: MutableMapping[T, MutableMapping[T, float]] = {}
        for current, translations in count_matrix.items():
            sum_of_counts = sum(translations.values())
            probabilities: MutableMapping[T, float] = {}
            for translation, count in translations.items():
                probabilities[translation] = count / sum_of_counts
            probability_matrix[current] = probabilities

        return cls(
            count_matrix=count_matrix,
            probability_matrix=probability_matrix,
        )

    def calculate_chain_probability(self, chain: Sequence[T]) -> float:
        probability = 1
        for index in range(len(chain) - 1):
            current = chain[index]
            next = chain[index + 1]
            if current not in self.probability_matrix:
                raise Exception(f"Current {current} not found in probability matrix")
            translations = self.probability_matrix[current]
            if next not in translations:
                raise Exception(f"Next {next} not found in translations")
            probability *= translations[next]
        return probability

    def generate_sequence(self, start_entry: T, max_iteration: int) -> Iterable[T]:
        if start_entry not in self.probability_matrix:
            raise Exception(
                f"Start entry {start_entry} not found in probability matrix"
            )

        parts: list[T] = [start_entry]
        current_entry = start_entry
        iteration_count = 0
        while iteration_count < max_iteration:
            if current_entry not in self.probability_matrix:
                parts.append(current_entry)
                break
            translations = self.probability_matrix[current_entry]
            current_entry, *_ = random.choices(
                population=tuple(translations.keys()),
                weights=tuple(translations.values()),
                k=1,
            )
            parts.append(current_entry)
            iteration_count += 1
        return parts
