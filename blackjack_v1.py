import random

# random.choice('123456789JQKA')
# 定义卡池和两个空list
Jack = 10
Queen = 10
King = 10
Ace = 1
card_pool = [2,3,4,5,6,7,8,9,Jack,Queen,King,Ace,2,3,4,5,6,7,8,9,Jack,Queen,King,Ace,2,3,4,5,6,7,8,9,Jack,Queen,King,Ace,2,3,4,5,6,7,8,9,Jack,Queen,King,Ace]
player_card = []
computer_card = []

# 洗牌
random.shuffle(card_pool)

# 每人先发两张牌
card1 = card_pool.pop(0)
player_card.append(card1)
card2 = card_pool.pop(0)
computer_card.append(card2)

card3 = card_pool.pop(0)
player_card.append(card3)
card4 = card_pool.pop(0)
computer_card.append(card4)
#######################################################################

# 发牌——替换Ace
def hit():
    number = card_pool.pop(0)
    return number
# 不发牌
def stand():
    return 0

# 判定hit/stand函数
def hit_or_stand(h_o_s):
    if h_o_s == "hit":
        return hit()
    elif h_o_s == "stand":
        return stand()
    else:
        print("wrong word, please insert again:")
        return hit_or_stand(input())

# 分数
def point(whos_card):
    if whos_card == player_card:
        point = sum(player_card)
        return point
    else:
        point = sum(computer_card)
        return point

# 判断是否blackjack
def blackjack():
    if point(player_card) == point(computer_card) == 21:
        print("Draw, double BlackJack")
        return end_game()
    if point(player_card) == 21:
        print("Congratulations, BlackJack you win")
        return end_game()
    if point(computer_card) == 21:
        print("Sorry, computer BlackJack you lost")
        return end_game()

# 停止游戏
def end_game():
    print("That was a good game, bye!")

#游戏流程
def game_goes_on():
    print("Do you want to hit or stand?")
    h_o_s = input()
    player_card.append(hit_or_stand(h_o_s))
# computer_player判定
    if point(computer_card) < 18:
        h_o_s = hit()
    else:
        h_o_s = stand()
    computer_card.append(h_o_s)

    print("Now your card is: ",player_card , " , Total point is: ", point(player_card))
    print("Now computer card is: ", computer_card , " , Total point is: ", point(computer_card))

# 判定游戏是否继续
    blackjack()
    if point(player_card) > 21 and point(computer_card) < 21:
        print("Blast, you Lose")
        return end_game()
    elif point(computer_card) > 21 and point(player_card) < 21:
        print("You win")
        return end_game()
    if player_card[-1] == computer_card[-1] == 0:
        if point(player_card) > point(computer_card):
            print("You Lose")
            return end_game()
        elif point(player_card) == point(computer_card):
            print("Draw")
            return end_game()
        else:
            print("You win")
            return end_game()
    else:
        return game_goes_on()

################################################################################
# 初始化每人发两张牌牌
print("Welcome to play BlackJack - 21 point!\nPlease insert your name challenger: ")
name = input()
print("Welcome " + name + " , here is your card: ", player_card," Total point is:", point(player_card))
print("computer card is: ", computer_card," Total point is: ", point(computer_card))
blackjack()
game_goes_on()

# # 询问
# print("Do you want to hit or stand?")
# h_o_s = input()
# player_card.append(hit_or_stand(h_o_s))
# # computer_player判定
# if point(computer_card) < 18:
#     h_o_s = hit()
# else:
#     h_o_s = stand()
# computer_card.append(h_o_s)

# print("Now your card is: ",player_card , " , Total point is: ", point(player_card))
# print("Now computer card is: ", computer_card , " , Total point is: ", point(computer_card))
# # 判断输赢
# blackjack()
# if point(player_card) > 21 and point(computer_card) < 21:
#     print("Blast, you Lose")
# elif point(computer_card) > 21 and point(player_card) < 21:
#     print("You win")

# # 都stand
# if player_card[-1] == computer_card[-1] == 0:
#     if point(player_card) > point(computer_card):
#         print("You Lose")
#     else:
#         print("You win")







# 后续工作： ace情况 循环 用类的方法实现