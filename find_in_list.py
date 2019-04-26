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

for numb, ranc in numbers.items():
    if ranc == 'jack':
        print('find!')

pl_one_sort = [
                ('queen', '♣', 12),
                ('king', '♣', 13),
                ('10', '♥', 10),
                ('jack', '♥', 11),
                ('queen', '♥', 12),
                ('queen', '♥', 13),
                ('queen', '♥', 14),
                ('10', '♦', 10),
                ('king', '♦', 13),
                ('ace', '♦', 14)
              ]

comb = 1
for i in range(len(pl_one_sort)):
    rank, suit, value = pl_one_sort[i]
    if i < len(pl_one_sort)-1:
        rank_n, suit_n, value_n = pl_one_sort[i+1]
        if suit == '♥':
            if value+1 == value_n:
                print(rank_n, suit_n, value_n)
                comb += 1
print(comb)
                
