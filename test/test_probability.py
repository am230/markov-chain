import markov_chain


def test_probability():
    tokens = ["しか", "のこ", "のこ", "こし", "たん", "たん", "-"]
    chain = markov_chain.create(tokens)
    assert (
        chain.calculate_chain_probability(
            ["しか", "のこ", "のこ", "こし", "たん", "たん", "-"]
        )
        == 0.0625
    ), f"Expected {chain.calculate_chain_probability(['しか', 'のこ', 'のこ', 'こし', 'たん', 'たん', '-'])} to be 0.0625"
