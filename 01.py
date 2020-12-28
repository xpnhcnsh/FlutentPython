import collections

card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """Note how to use 'key' method in inbuild func sorted()."""
    rank = [str(n) for n in range(2, 11)] + list('JQKA')
    suit = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [card(ranks, suits) for suits in self.suit
                       for ranks in self.rank]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(c):
    rank_value = FrenchDeck.rank.index(c.rank)
    return rank_value * len(suit_values) + suit_values[c.suit]


d = FrenchDeck()
for card in sorted(d, key=spades_high):
    print(card)
