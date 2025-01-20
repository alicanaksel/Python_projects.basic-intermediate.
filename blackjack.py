# Blackjack
# new version
from random import randint

# Initialize global variables
croupier_cards = []
player_cards = []
player_total = 0
croupier_total = 0
player_lost = False  # Track if the player has lost

# Phase 1 & 2: Croupier's turn and Player's initial cards
def phase_12():
    global croupier_total, player_total
    
    # Croupier's turn
    card1 = randint(1, 11)
    croupier_cards.append(card1)
    croupier_total += card1
    print("Croupier got the card:", card1)
    
    # Player's turn
    pcard1 = randint(1, 11)
    pcard2 = randint(1, 11)
    player_total += pcard1 + pcard2
    player_cards.extend([pcard1, pcard2])
    
    print("Player got the cards:", " and ".join(map(str, player_cards)))
    print("Player's total:", player_total)
    
    # Check if player hits 21 immediately
    if player_total == 21:
        print("Congratulations! You hit 21 with your initial cards and win!")
        exit()  # End the program

# Phase 3: Player's decision to draw cards
def phase_3():
    global player_total, player_lost
    while player_total <= 21:
        ask_player = input("Would you like to have another card? (yes/no): ").strip().lower()
        
        if ask_player in ("y", "yes"):
            card = randint(1, 11)
            player_total += card
            player_cards.append(card)
            print(f"You drew a {card}. Your total is now: {player_total}.")
            
            # Check if player hits 21 during the turn
            if player_total == 21:
                print("Congratulations! You hit 21 and win!")
                exit()  # End the program
        elif ask_player in ("n", "no"):
            print(f"You chose to stop. Your final total is {player_total}.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
        
        # Check if player loses
        if player_total > 21:
            player_lost = True
            print("Your total is over 21. You lose!")
            break

# Phase 4: Croupier's turn
def phase4():
    global croupier_total, player_total
    
    if player_lost:
        print("Croupier wins by default as the player has lost.")
        return
    
    print("\nCroupier's turn starts...")
    while croupier_total < 21:
        if croupier_total < 17:
            card = randint(1, 11)
            croupier_cards.append(card)
            croupier_total += card
            print(f"Croupier drew a {card}. Total is now: {croupier_total}.")
        else:
            break
    
    if croupier_total > 21:
        print("Croupier went over 21. Player wins!")

# Determine the winner
def determine_winner():
    global croupier_total, player_total, player_lost
    if player_lost:
        print("Croupier wins since the player has lost.")
    elif croupier_total > 21:
        print("Player wins since the croupier went over 21.")
    elif player_total > croupier_total:
        print(f"Player wins with {player_total} points vs. Croupier's {croupier_total} points.")
    elif croupier_total > player_total:
        print(f"Croupier wins with {croupier_total} points vs. Player's {player_total} points.")
    else:
        print(f"It's a draw with both scoring {player_total} points.")

# Main Program
print("Welcome to the Blackjack Game!\n")
phase_12()

if not player_lost:
    phase_3()

if not player_lost:
    phase4()

determine_winner()




# Old version
'''
from random import randint

# Initialize global variables
croupier_cards = []
player_cards = []
player_total = 0
croupier_total = 0

# Phase 1 & 2: Croupier's turn and Player's initial cards
def phase_12():
    global croupier_total, player_total  # Declare globals to modify them inside the function
    
    # Croupier's turn
    card1 = randint(1, 11)
    croupier_cards.append(card1)
    croupier_total += card1
    print("Croupier got the card:", card1)
    
    # Player's turn
    pcard1 = randint(1, 11)
    pcard2 = randint(1, 11)
    player_total += pcard1 + pcard2
    player_cards.extend([pcard1, pcard2])  # Append both cards to the list
    
    print("Player got the cards:", " and ".join(map(str, player_cards)))  # Display cards
    print("Player's total:", player_total)  # Display the total for clarity
    return

# Phase 3: Player's decision to draw cards
def phase_3():
    global player_total , condition # Access the global player total
    while player_total <= 21:  # Continue while player hasn't exceeded 21
        ask_player = input("Would you like to have another card? (yes/no): ").strip().lower()
        
        if ask_player in ("y", "yes"):
            # Draw a new card
            card = randint(1, 11)
            player_total += card
            player_cards.append(card)
            print(f"You drew a {card}. Your total is now: {player_total}.")
            if player_total == 21:
                break
        elif ask_player in ("n", "no"):
            print(f"You chose to stop. Your final total is {player_total}.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
        
        # Check if player loses
        if player_total > 21:
            print("Your total is over 21. You lose!")
            print("Cropier won.")
            break
    return

def phase4():
    global croupier_total
    cCard= 0
    while croupier_total< 21:
        if croupier_total < 17:
            cCard= randint(1,11)
            print(f"Croupier got the card: {cCard}.")
            croupier_total+= cCard
            print(f"Cropier total is: {croupier_total}.")
        else:
            break
    if croupier_total> 21:
        print("Cropier loses. Player wins")
    return


# Main Program
phase_12()

# Edge case: Skip Phase 3 if player already has 21
if player_total == 21:
    print("Congratulations! You hit 21 with your initial cards!")
else:
    phase_3()
    phase4()



if player_total> croupier_total and player_total <= 21:
    print("Player won.")
elif croupier_total > player_total and croupier_total <= 21:
    print("Cropier won.")
elif croupier_total == player_total:
    print("It's a draw")
    
'''
