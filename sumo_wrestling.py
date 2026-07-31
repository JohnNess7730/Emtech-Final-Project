###########################################

# Simply the introduction to the game, no need to 
# call this over and over, only once in the beginning
# is enough.

introduction = '''!! SUMO WRESTLING !!
-------------------------------------------------------------------------------------
This is a 2 player game where you take turns with your opponent taking actions. 

- Objective: Knockout your opponent's Fighting Spirit [FS] through different Techniques
- Techniques: Powerful techniques that require Momentum Points [MP]
- Momentum Points: A resource that can be gained when using [Build Momentum]

[Note # 1] Matches only lasts 10 Rounds. 
[Note # 2] The player with the highest Fighting Spirit [FS] wins
-------------------------------------------------------------------------------------
'''
print(introduction)

###########################################

# Easier to read code if listing moves is a separate function, 
# especially considering the size of the text.

def list_moves():
    techniques_list = '''
Techniques List:
═════════════════════════════════════════════
[1] Build Momentum      	  Restores 1 MP
[2] Thrust Attack       	  Deal 12 damage
[3] Stake Technique     	  Deal 36 damage; Cost: 1 MP
[4] Pushing Attack      	  Deal 50 damage; Cost: 2 MP
[5] Vajra Toss          	  KO the opponent; Cost: 3 MP
[6] Block               	  Blocks all attacks except for Vajra Toss
[7] Vajra Block         	  Blocks Vajra Toss only
═════════════════════════════════════════════
'''
    print(techniques_list)

############################################

# Though will_play() and continue_game() serve the same purpose, 
# they take in different inputs, and it's easier to just write 
# different functions for each.
'''
def will_play():
    question = ''\'[1] Start Game 
[2] Exit

''\'
    user_input = input(f"{question}Enter: ")
    if user_input == '1':
        return True
    elif user_input == '2':
        return False
    else:
        print("Invalid option. Please select only [1] or [2]")
        return will_play()

def continue_game():
    question = ''\'Play Again?
[Y] Yes
[N] No

''\'
    user_input = input(f"{question}Enter: ")
    if user_input == 'Y':
        return True
    elif user_input == 'N':
        return False
    else:
        print("Invalid option. Please select only [Y] or [N]")
        return continue_game()
'''

###########################################
# ABOVE FUNCTION REWRITTEN TO FIT THE "no recursion" STANDARD

def will_play(game_played):
    
    valid_input = False

    if game_played:
        question = '''Play Again?
[Y] Yes
[N] No

'''
        while not valid_input:
            user_input = input(f"{question}Enter: ")
            if user_input == 'Y':
                return True
            elif user_input == 'N':
                return False
            print("Invalid option. Please select only [Y] or [N]")

    question = '''[1] Start Game 
[2] Exit

'''
    while not valid_input:
        user_input = input(f"{question}Enter: ")
        if user_input == '1':
            return True
        elif user_input == '2':
            return False
        print("Invalid option. Please select only [1] or [2]")


###########################################

def get_name(player_number):
    name = input(f"- Enter P{player_number} Name (Default is \"P{player_number}\"): ")
    if len(name) > 0:
        return name
    else:
        return "P" + player_number

###########################################
'''
def move(player,mp):
    # Currently does NOT account for type errors.
    p_move = input(f"Enter {player}'s Move: ")
    if not p_move.isdigit():
        print("[Error: Invalid Input] Enter Only [1] to [7]")
        return move(player,mp)
    p_move = int(p_move)

    if (p_move == 5 and mp <3) or (p_move == 4 and mp < 2) or (p_move == 3 and mp < 1):
        print("[Error: Move Invalid] Not Enough Momentum [MP]\n")
    elif p_move > 0 and p_move < 8:
        return p_move
    else:
        print("[Error: Invalid Input] Enter Only [1] to [7]")
    return move(player,mp)
'''
def move_id(id):
    if id == 1:
        return "[Build Momentum]"
    if id == 2:
        return "[Thrust Attack]"
    if id == 3:
        return "[Stake Technique]"
    if id == 4:
        return "[Pushing Attack]"
    if id == 5:
        return "[Vajra Toss]"
    if id == 6:
        return "[Block]"
    if id == 7:
        return "[Vajra Block]"

#########################################

'''
def next_round(p1, p2, p1_hp, p1_mp, p2_hp, p2_mp, round_number):
    if round_number > 10:
        print("\t\t!! Time's Up !!")
        if p1_hp > p2_hp:
            return p1
        elif p2_hp > p1_hp:
            return p2
        else:
            return
    print("\n\t    ","=" * 10, "ROUND", round_number, "=" * 10, end="\n\n")

    display_statistics(p1,p2,p1_hp,p2_hp,p1_mp,p2_mp)
    list_moves()

    p1_move = move(p1,p1_mp)
    p2_move = move(p2,p2_mp)
    # print(type(p2_move), type(p2_move))

    print_move(p1,p1_move)
    print_move(p2,p2_move)

    if p1_move > p2_move:
        print(f"{p1}'s {move_id(p1_move)} WINS against {p2}'s {move_id(p2_move)}")

        if p1_move == 6 and (p2_move == 3 or p2_move == 4):
            print(f"{p2}'s {move_id(p2_move)} was blocked")

    elif p2_move > p1_move:
        print(f"{p2}'s {move_id(p2_move)} WINS against {p1}'s {move_id(p1_move)}")
        if p2_move == 6 and (p1_move == 3 or p2_move == 4):
            print()
    else:
        print(f"Both {p1} and {p2} used {move_id(p1_move)}")


    return next_round(p1, p2, p1_hp, p1_mp, p2_hp, p2_mp, round_number + 1)
'''

##########################################

def get_move(player,mp):

    input_valid = False
    
    while not input_valid:
    
        move = input(f"Enter {player}'s Move: ")
        if not move.isdigit():
            print("[Error: Invalid Input] Enter Only [1] to [7]\n")
        else:
            move = int(move)
            if (move == 5 and mp <3) or (move == 4 and mp < 2) or (move == 3 and mp < 1):
                print("[Error: Move Invalid] Not Enough Momentum [MP]\n")
            elif move == 1 and mp > 4:
                print("[Error: Move Invalid] Momentum [MP] Capped at 5.")
            elif move > 0 and move < 8:
                return move
            else:
                print("[Error: Invalid Input] Enter Only [1] to [7]\n")


##########################################

def use_momentum(player,move):
    momentum = 0
    if move == 1:
        momentum = -1
    if move == 3:
        momentum = 1
    if move == 4:
        momentum = 2
    if move == 5:
        momentum = 3
    
    if momentum < 0:
        print(f"{player} used [Build Momentum] and restores 1 Momentum [MP].")
    elif momentum > 0:
        print(f"{player} consumes {momentum} Momentum [MP] to use {move_id(move)}")
    else:
        print(f"{player} used {move_id(move)}")
    return momentum

######################################

def reduce_fs(move):
    if move == 2:
        return 12
    if move == 3:
        return 36
    if move == 4:
        return 50
    return 0

######################################

def display_stats(p1,p2,p1_hp,p2_hp,p1_mp,p2_mp):
    print(f"\t║ \t{p1}\t║\t║ \t{p2}\t║")
    print(f"\t║ FS: [{p1_hp}/100]\t║\t║ FS: [{p2_hp}/100]\t║")
    print(f"\t║ MP: [{p1_mp}/5]\t║\t║ MP: [{p2_mp}/5]\t║")

###########################################
def main_game(p1,p2):    
    print("\n\t=== GET READY FOR THE NEXT BATTLE! ===")

    round = 0
    players_alive = True

    p1_hp = 100
    p2_hp = 100
    p1_mp = 0
    p2_mp = 0

    while round < 10 and players_alive:
        round += 1
        print("\n\t    ","=" * 10, "ROUND", round, "=" * 10, end="\n\n")
        
        display_stats(p1,p2,p1_hp,p2_hp,p1_mp,p2_mp)
        list_moves()
        
        if round % 2 == 1:
            p1_move = get_move(p1,p1_mp)
            p2_move = get_move(p2,p2_mp)
        else:
            p2_move = get_move(p2,p2_mp)
            p1_move = get_move(p1,p1_mp)

        print("═════════════════════════════════════════════") 
        p1_mp -= use_momentum(p1,p1_move)
        p2_mp -= use_momentum(p1,p2_move)
        print("═════════════════════════════════════════════") 
        if p1_move == p2_move:
            print(f"Both players used {move_id(p1_move)}")
        
        elif (p1_move > p2_move and p1_move < 6) or (p1_move == 6 and p2_move > 1 and p2_move < 5) or (p1_move == 7 and p2_move == 5):
            print(f"{p1}'s {move_id(p1_move)} WINS against {p2}'s {move_id(p2_move)}")
        else:
            print(f"{p2}'s {move_id(p2_move)} WINS against {p1}'s {move_id(p1_move)}")

        '''
        elif p1_move > p2_move or (p1_move == 5 and p2_move != 7) or (p1_move > 1 and p1_move < 5 and p2_move !=6):
            print(f"{p1}'s {move_id(p1_move)} WINS against {p2}'s {move_id(p2_move)}")
        elif p2_move > p1_move or (p2_move == 5 and p1_move != 7) or (p2_move > 1 and p2_move < 5 and p1_move !=6):
            print(f"{p2}'s {move_id(p2_move)} WINS against {p1}'s {move_id(p1_move)}")
        '''

        if p1_move == p2_move:
            print("DRAW! Nothing else happens")
        elif (p1_move == 6 and (p2_move > 1 and p2_move < 5)) or (p1_move == 7 and p2_move == 5):
            print(f"{p2}'s {move_id(p2_move)} was blocked")
        elif (p2_move == 6 and (p1_move > 1 and p1_move < 5)) or (p2_move == 7 and p1_move == 5):
            print(f"{p1}'s {move_id(p1_move)} was blocked")
        elif p1_move == 5:
            print(f"{p2} loses all Fighting Spirit and gets KO'd")
            p2_hp = 0
        elif p2_move == 5:
            print(f"{p1} loses all Fighting Spirit and gets KO'd")
            p1_hp = 0
        else:
            if p1_move > p2_move and p1_move > 1 and p1_move < 5:
                print(f"{p2} loses {reduce_fs(p1_move)} Fighting Spirit")
                p2_hp -= reduce_fs(p1_move)
            elif p2_move > 1 and p2_move < 5:
                print(f"{p1} loses {reduce_fs(p2_move)} Fighting Spirit")
                p1_hp -= reduce_fs(p2_move)
        
        if p1_hp <= 0:
            p1_hp = 0
            players_alive = False
        if p2_hp <= 0:
            players_alive = False
            p2_hp = 0
    
    print("\n")
    display_stats(p1,p2,p1_hp,p2_hp,p1_mp,p2_mp)
    if round == 10 and players_alive:
        print("\n\t\t\t!! TIME'S UP !!")
    if p1_hp > p2_hp:
        print(f"\n\t\t\t!! {p1} WINS !!\n")
    elif p2_hp > p1_hp:
        print(f"\n\t\t\t!! {p2} WINS !!\n")
    else:
        print("\n\t\t\t !! DRAW !!\n")

##########################################

# Main start to the game
game_played = False

while will_play(game_played):
    if not game_played:
        print('=' * 45,"\nMatch Registration")
        p1 = get_name('1')
        p2 = get_name('2')
        print('=' * 45)
        
    main_game(p1,p2)
    game_played = True

# I ALMOST FORGOT TO REMOVE MY TRY EXCEPT HAHAHAHAH
'''
try:
    game_played = False
    while will_play(game_played):
        if not game_played:
            print('=' * 45,"\nMatch Registration")
            p1 = get_name('1')
            p2 = get_name('2')
            print('=' * 45)
        
        main_game(p1,p2)
        game_played = True

except KeyboardInterrupt:
    print("\nKeyboardInterrupt")
'''
