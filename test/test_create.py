import markov_chain


def test_create():
    tokens = ["しか", "のこ", "のこ", "こし", "たん", "たん", "-"]
    chain = markov_chain.create(tokens)
    assert (
        chain.probability_matrix
        == {
            "しか": {"のこ": 1.0},
            "のこ": {"のこ": 0.5, "こし": 0.5},
            "こし": {"たん": 1.0},
            "たん": {"たん": 0.5, "-": 0.5},
        }
    ), f"Expected {chain.probability_matrix} to be {{'しか': {{'のこ': 1.0}}, 'のこ': {{'のこ': 0.6666666666666666, 'こし': 0.3333333333333333}}, 'こし': {{'たん': 1.0}}, 'たん': {{'たん': 0.5, '-': 0.5}}}}"
