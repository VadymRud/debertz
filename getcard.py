"""
card	[ kɑːd ]	карта
card games	[ kɑːd ɡeɪmz ]	карточные игры
game	[ ɡeɪm ]	кон / партия / раздача
to deal the cards	[ tə diːl ðə kɑːdz ]	сдавать карты
to shuffle the cards / the deck	[ tə ˈʃʌfl̩ ðə kɑːdz ] [ ðə dek ]	тасовать карты
to cut the cards	[ tə kʌt ðə kɑːdz ]	снимать колоду
pack / deck of cards	[ pæk ] [ dek ] [ əv kɑːdz ]	колода карт
suit	[ s(j)uːt ]	масть
hearts	[ hɑːts ]	черви
clubs	[ klʌbz ]	трефы
diamonds	[ ˈdaɪəməndz ]	бубны
spades	[ speɪdz ]	пики
trump	[ trʌmp ]	козырь
non-trump cards	[ nɒn trʌmp kɑːdz ]	некозырные карты
trump suit	[ trʌmp s(j)uːt ]	козырная масть
lower / higher card	[ ləʊə ] [ haɪə kɑːd ]	младшая / старшая карта
lowest trump	[ˈləʊɪst trʌmp ]	младший козырь
denomination / rank	[dɪˌnɒmɪˈneɪʃn̩ ] [ ræŋk ]	достоинство (карты)
ace	[ eɪs ]	туз
king	[ kɪŋ ]	король
queen	[ kwiːn ]	дама
jack	[ dʒæk ]	валет
joker	[ ˈdʒəʊkə ]	джокер
a trump 7	[ ə trʌmp ˈsevn̩ ]	козырная семерка
ten of clubs	[ ten əv klʌbz ]	десятка треф
three twos	[ θriː tuːz ]	три двойки
ace of hearts	[ eɪs əv hɑːts ]	туз червей
face	[ feɪs ]	лицо (карты)
back of a card	[ ˈbæk əv ə kɑːd ]	рубашка (карты)
hand	[ hænd ]	карты ((имеющиеся) на руках)
to put down / to lay (a card)	[ tə ˈpʊt daʊn ] [ tə leɪ ] [ ə kɑːd ]	положить (карту)
attack	[ əˈtæk ]	заходить / заход
attacker	[ əˈtækə ]	заходящий игрок
discard	[ dɪˈskɑːd ]	сбрасывать карту
to beat / defend	[ tə biːt ] [ dɪˈfend ]	побить / покрыть карты
discard pile	[ dɪˈskɑːd paɪl ]	отбой (карты, вышедшие из игры)
successful defense	[ səkˈsesfəl dɪˈfens ]	отбой (игрок отбился – побил все карты)
defender	[ dɪˈfendə ]	отбивающийся игрок
pass	[ pɑːs ]	переводить (карты)
Your turn!	[ jɜː tɜːn ]	Твой ход!
to abandon the defense	[ tu əˈbændən ðə dɪˈfens ]	принять (забрать карты)
trick	[ trɪk ]	взятка


Read more: http://study-english.info/vocabulary-cards.php#ixzz5kUW0DoKL 
http://study-english.info/ 

"""
import random
from cards import cards, Card, numbers


debertz_cards = cards[20:-2]
# print(debertz_cards)


def my_shuffle(array):
    random.shuffle(array)
    return array


def cards_player_sort(cards_player):
    cards_player_sort_arr = []
    for card in cards_player:
        rank, suit = card.split('_')
        for value, ranc in numbers.items():
            if ranc == rank:
                cards_player_sort_arr.append(Card(rank,
                                             suit, value))

    cards_player_sort_arr = sorted(cards_player_sort_arr,
                                   key=lambda card: (card.suit, card.value))
    return cards_player_sort_arr


def first_step(player_count):
    debertz_cards = cards[20:-2]
    cards_player_one = list()
    cards_player_two = list()
    cards_player_three = list()
    cards_player_fourth = list()
    # карти в колоді
    deck_of_cards = list()

    # кількість гравців
    # player_count = 3

    # козир

    # print(len(debertz_cards))
    debertz_cards = my_shuffle(debertz_cards)

    for k in range(2):
        for i in range(3):
            add_card = debertz_cards.pop()
            cards_player_one.append(add_card)
            if i == 2:
                break
        for i in range(3):
            add_card = debertz_cards.pop()
            cards_player_two.append(add_card)
            if i == 2:
                break
        for i in range(3):
            add_card = debertz_cards.pop()
            cards_player_three.append(add_card)
            if i == 2:
                break
        if player_count == 4:
            for i in range(3):
                add_card = debertz_cards.pop()
                cards_player_fourth.append(add_card)
                if i == 2:
                    break

    deck_of_cards = debertz_cards

    cards_player_one_sort = cards_player_sort(cards_player_one)
    cards_player_two_sort = cards_player_sort(cards_player_two)
    cards_player_three_sort = cards_player_sort(cards_player_three)
    cards_player_fourth_sort = cards_player_sort(cards_player_fourth)

    for card in cards_player_one_sort:
        print(card)
    return {
            'cards_player_one': cards_player_one_sort,
            'cards_player_two': cards_player_two_sort,
            'cards_player_three': cards_player_three_sort,
            'cards_player_fourth': cards_player_fourth_sort,
            'deck_of_cards': debertz_cards,
            'trump': debertz_cards[-1]
            }


def step_two():
    # роздаєм карти з колоди
    if player_count == 3:
        for i in range(4):
            add_card = deck_of_cards.pop()
            cards_player_one.append(add_card)
            if i == 3:
                break
        for i in range(4):
            add_card = deck_of_cards.pop()
            cards_player_two.append(add_card)
            if i == 3:
                break
        for i in range(4):
            add_card = deck_of_cards.pop()
            cards_player_three.append(add_card)
            if i == 3:
                break

        trump = deck_of_cards[-1]
    # роздаєм карти з колоди
    if player_count == 4:
        for i in range(2):
            add_card = deck_of_cards.pop()
            cards_player_one.append(add_card)
            if i == 1:
                break
        for i in range(2):
            add_card = deck_of_cards.pop()
            cards_player_two.append(add_card)
            if i == 1:
                break
        for i in range(2):
            add_card = deck_of_cards.pop()
            cards_player_three.append(add_card)
            if i == 1:
                break
        for i in range(2):
            add_card = deck_of_cards.pop()
            cards_player_fourth.append(add_card)
            if i == 1:
                break
        trump = cards_player_fourth[-1]

    cards_player_one_sort = []
    for card in cards_player_one:
        rank, suit = card.split('_')
        for value, ranc in numbers.items():
            if ranc == rank:
                cards_player_one_sort.append(Card(rank,
                                             suit, value))

    cards_player_one_sort = sorted(cards_player_one_sort,
                                   key=lambda card: (card.suit, card.value))

    for card in cards_player_one_sort:
        print(card)

    print('cards_player_one: ', cards_player_one_sort)
    print('cards_player_two: ', cards_player_two)
    print('cards_player_three: ', cards_player_three)
    if player_count == 4:
        print('cards_player_fourth: ', cards_player_fourth)
    print('deck of cards: ', deck_of_cards, len(deck_of_cards))
    print('trump: ', trump)
    # print(cards_player_two)
    # print(cards_player_three)

    # if __name__ == "__main__":

    #     print(my_shuffle(debertz_cards))


