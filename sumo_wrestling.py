########## DEFINITION OF TERMS ############
'''

    - The definition of terms will be used for shortening variables,
      so that writing code shall become more efficient and not all
      variables need to be typed in full. If the variable wont be used
      frequently anyway, it will be typed with its full name.

    - Typically, the letter P would signify "Player",
      for example: P1 and P2 stand for Player 1 and Player 2 respectively,
      and p_move stands for player's move. 
      
    - FS is short for Fighting Spirit, practically the hitpoints
    - MP is short for Momentum Points, practically energy

'''
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

def will_play():
    question = '''[1] Start Game 
[2] Exit

'''
    user_input = input(f"{question}Enter: ")
    if user_input == '1':
        return True
    elif user_input == '2':
        return False
    else:
        print("Invalid option. Please select only [1] or [2]")
        return will_play()

def continue_game():
    question = '''Play Again?
[Y] Yes
[N] No

'''
    user_input = input(f"{question}Enter: ")
    if user_input == 'Y':
        return True
    elif user_input == 'N':
        return False
    else:
        print("Invalid option. Please select only [Y] or [N]")
        return continue_game()

###########################################

def get_name(player_number):
    name = input(f"- Enter P{player_number} Name (Default is \"P{player_number}\"): ")
    if len(name) > 0:
        return name
    else:
        return "P" + player_number

###########################################
# Fix formatting later
def display_statistics(p1,p2,p1_fs,p2_fs,p1_mp,p2_mp):
    print(f"{p1}\t\t{p2}")
    print(f"FS:{p1_fs}\t\tFS:{p2_fs}")
    print(f"MP:{p2_mp}\t\tMP:{p2_mp}")
    return

###########################################

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

def print_move(player,move):
    print(player,end=' ')
    if move < 3 or move > 5:
        print(f"used {move_id(move)}",end=' ')
        if move == 1:
            print("and restores 1 MP")
        else:
            print()
        return
    
    if move == 3:
        momentum = 1
    elif move == 4:
        momentum = 2
    else:
        momentum = 3
    print(f"consumes {momentum} Momentum to use {move_id(move)}")

def receive_action(action, actor, recepient):
    print(f"{actor}'s ")

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
    elif p2_move > p1_move:
        print(f"{p2}'s {move_id(p2_move)} WINS against {p1}'s {move_id(p1_move)}")
    else:
        print(f"Both {p1} and {p2} used {p1_move}")


    return next_round(p1, p2, p1_hp, p1_mp, p2_hp, p2_mp, round_number + 1)

##########################################

def main_game(game_played):
    if not game_played:
        if not will_play():
            return
        # Match Registration
        print('=' * 45,"\nMatch Registration")
        player_one = get_name('1')
        player_two = get_name('2')
        print('=' * 45)
        # print(f"Player One: {player_one}\nPlayer Two: {player_two}")
    
    print("\n\t=== GET READY FOR THE NEXT BATTLE! ===")
    winner = next_round(player_one, player_two, 100, 0, 100, 0, 1)

##########################################

# Main start to the game
main_game(False)
