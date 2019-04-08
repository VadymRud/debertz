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
from cards import cards

debertz_cards = cards[20:-2]
#print(debertz_cards)

def my_shuffle(array):
        random.shuffle(array)
        return array

if __name__ == "__main__":
    
    print(my_shuffle(debertz_cards))

