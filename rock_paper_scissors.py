import random

draw=0
win=0
lose=0

status_counter_w = 0
status_counter_d = 0
status_counter_l = 0

ans_win_round = "Wygrałeś!!! :)"
ans_lose_round = "przegrałeś :("
ans_draw_round = "jest remis -_-"

ans_win_game = "Wygrałeś!!! :) Brawo spróbuj jeszcze raz wygrać z komputerem"
ans_lose_game = "przegrałeś spróbuj jeszcze raz :("
ans_draw_game = "zremisowałeś z komputerem -_- spróbuj jeszcze raz"

print("W grze papier, kamień, nożyce kto pierwszy zwycięży 3 razy wygrywa.")


def get_player_move():
    answer = input("podaj literę (P,K,N): ").upper()
    return answer
     

def get_comuter_move():
    computer_choice = random.choice(["P","K","N"])
    return computer_choice


def check_the_round_result():
    global draw, win, lose, answer, computer_choice

    if answer not in ["P", "K", "N"]:
        print("Podałeś złą literkę")
        print("")
        return

    win_with ={"P":"K","K":"N","N":"P"}
    lose_with ={"K":"P","N":"K","P":"N"}

    if answer == computer_choice:
        print(ans_draw_round)
        draw+=1

    elif win_with[answer] == computer_choice:
        print(ans_win_round)
        win+=1

    elif lose_with[answer] == computer_choice:
        print(ans_lose_round)
        lose+=1

    print("twój status to: ", win, "wygranych,", draw, "remisów,", lose, "przegranych")
    print("")


def check_the_status_of_played_games():
    global status_counter_w, status_counter_d, status_counter_l, win, draw, lose

    if win == 3:
        status_counter_w +=1
        print(ans_win_game) 
    elif draw == 3:
        status_counter_d+=1
        print(ans_draw_game)
    elif lose == 3:
        status_counter_l+=1
        print(ans_lose_game)
    if win == 3 or draw == 3 or lose == 3:
        print("Twój status rozegranych gier:", status_counter_w, "wygranych,", status_counter_d, "remisów", status_counter_l, "przegranych")
        print("")


def ask_continue():
    global win, lose, draw
    if win == 3 or lose == 3 or draw == 3:
        while True:
            l = input("Jeśli chcesz kontynuować grę wpisz 'dalej' jeśli nie wpisz 'koniec': ").lower()
            if l == 'dalej':
                print("")
                print("Gra jest kontynuowana ponownie wygrany musi wygrać 3 razy by zwyciężyć.")
                win = 0
                lose = 0
                draw = 0
                break
            elif l == 'koniec':
                print("koniec gry")
                exit()
            else : 
                print("zła informacja")
                continue
            

while True:
    answer = get_player_move()
    computer_choice = get_comuter_move()

    print(answer)
    print("Odpowiedź komputera:", computer_choice)

    check_the_round_result()
    check_the_status_of_played_games()
    ask_continue()
