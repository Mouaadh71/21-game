import random
def card():
    card = int(random.randint(1,13))
    return card
delar_cards = [card(),card()]
player_cards = [card(),card()]
def updet():
    global sdc
    global spc
    sdc = sum(delar_cards)
    spc = sum(player_cards)
updet()
def print_states():
    print(f"player_cards :{player_cards} total : {spc}")

def print_both_states() :
    print(f"delar_cards :{delar_cards} total : {sdc}")
    print(f"player_cards :{player_cards} total : {spc}")

def delar_ai():
    if sdc <21 and sdc < spc:
        if (sdc - 21) <= 5 and sdc < spc and spc <= 21 :
            delar_cards.append(card())
        elif spc > sdc and spc <= 21 :
            delar_cards.append(card())

while True :
    print_states()
    choice = input('What do you want? ["play" to request another card, "stop" to stop]: ')
    if choice == "play" :
        player_cards.append(card())
        updet()
        delar_ai()
    if choice == "stop" :
        delar_ai()
        break
def check_winer() :
    updet()
    while True :
        if sdc < spc and spc <=21 :
            print_both_states()
            print("you won")
            break
        elif sdc == spc:
             delar_cards.append(card())
             player_cards.append(card())
        elif sdc > spc and sdc <=21 :
            print_both_states()
            print("you lose")
            break
        elif sdc > 21 and spc >21 :
            if sdc > spc:
                print_both_states()
                print("you won")
                break
            elif sdc < spc :
                print_both_states()
                print("you lose")
                break
        elif sdc > 21 and spc <21:
            print_both_states()
            print("you win")
            break  
        else :
            print_both_states()
            print("you lose")
            break
check_winer()
