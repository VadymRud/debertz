cards = ['2_♥', '2_♣', '2_♦', '2_♠',
         '3_♥', '3_♣', '3_♦', '3_♠',
         '4_♥', '4_♣', '4_♦', '4_♠',
         '5_♥', '5_♣', '5_♦', '5_♠',
         '6_♥', '6_♣', '6_♦', '6_♠',
         '7_♥', '7_♣', '7_♦', '7_♠',
         '8_♥', '8_♣', '8_♦', '8_♠',
         '9_♥', '9_♣', '9_♦', '9_♠',
         '10_♥', '10_♣', '10_♦', '10_♠',
         'jack_♥', 'jack_♣', 'jack_♦', 'jack_♠',
         'queen_♥', 'queen_♣', 'queen_♦', 'queen_♠',
         'king_♥', 'king_♣', 'king_♦', 'king_♠',
         'ace_♥', 'ace_♣', 'ace_♦', 'ace_♠',
         'joker_1', 'joker_2'
         ]

SUITS_PRINTABLE = ['♠', '♥', '♦', '♣']

numbers = {
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: '10',
            11: 'jack',
            12: 'queen',
            13: 'king',
            14: 'ace',
            15: 'joker'
        }



class Card:
    
    def __init__(self, rank, suit, number):
        self.rank = rank
        self.suit = suit
        self.number = number

    def __repr__(self):
        return repr((self.rank, self.suit, self.number))
    