#######################################
"""
        Who wants to be a millioner
"""
from random import randrange

prize = (100,200,300,500,1000,2000,4000,8000,16000,32000)

class Question(object):
    def __init__(self, description, key, alt1, alt2, alt3, question_level):
        self.__description = description
        self.__key = key
        self.__alt1 = alt1
        self.__alt2 = alt2
        self.__alt3 = alt3
        self.__question_level = question_level
        
    # GETTERS
    def get_description(self):
        return self.__description
    def get_key(self):
        return self.__key
    def get_alt1(self):
        return self.__alt1
    def get_alt2(self):
        return self.__alt2
    def get_alt3(self):
        return self.__alt3
    def get_question_level(self):
        return self.__question_level
    
    # Question content
    def __str__(self):
        return f"Description: {self.__description}\na: {self.__key}\nb: {self.__alt1}\nc: {self.__alt2}\nd: {self.__alt3}\nLevel : {self.__question_level}\n"



def get_question(player_level):
    # Setting up the file
    file_name = str(player_level + 1)
    file_handle = open("Questions/Level " + file_name + ".txt", "r")
    lines = file_handle.readlines()
    file_handle.close()
    
    question_index = randrange(0,11,5)              # END doesn't evaluate
    
    return Question(lines[question_index], lines[question_index + 1], lines[question_index + 2], lines[question_index + 3], lines[question_index + 4], player_level)

def get_alternatives(alternatives_list):
    size = len(alternatives_list)
    shuffled_alternatives = []
    
    while size > 0:
        random_index = randrange(0, size, 1)        # Basically randint(0, len(x))
        shuffled_alternatives.append(alternatives_list[random_index])
        del alternatives_list[random_index]
        size -= 1
    return shuffled_alternatives

def get_input(player_level):
    valid_choices = ["A","B","C","D", "RETREAT"]
    while True:
        choice = input("\nYour final answer is... \t")
        if choice.upper() in valid_choices:
            if choice.upper() == "A":
                return 0
            elif choice.upper() == "B":
                return 1
            elif choice.upper() == "C":
                return 2
            elif choice.upper() == "D":
                return 3
            elif choice.upper() == "RETREAT" and player_level >= 1:
                return 4



def play_game(player_level):
    # Create question object
    player_question = get_question(player_level)
    
    # Prints the question
    print(f"\nQuestion {player_level + 1} for {prize[player_level]}$\n")
    print(player_question.get_description())
    
    # Randomize alternatives
    alternatives = [player_question.get_key().rstrip("\n"), player_question.get_alt1().rstrip("\n"),    
                    player_question.get_alt2().rstrip("\n"), player_question.get_alt3().rstrip("\n")]
    key = "" + alternatives[0]
    alternatives = get_alternatives(alternatives)
    
    # Show for the user
    for i in range(0, len(alternatives)):
        if i == 0:
            letter = "A: "
        elif i == 1:
            letter = "B: "
        elif i == 2:
            letter = "C: "
        else:
            letter = "D: "
        print(letter + alternatives[i])
        i += 1
    
    # Get user input and check
    user_input = get_input(player_level)
    print("\n" + 75*"-" + "\n")
    
    if user_input == 4:
        print("Returning retreat")
        return {"Countinue":-1, "money_index":player_level - 1}
    else:
        if alternatives[user_input] == key:
            return {"Countinue":1, "money_index":player_level} 
        else:
            return {"Countinue":0, "money_index_when_lose":player_level // 5}
        
    


def main():
    print("-"*70 + "\n\tA \"Who wants to be a millioner\" game by Andri Reveli\n" + "-"*70)
    
    level = 0
    while level <= 9:
        continue_to_play = play_game(level)
        if continue_to_play["Countinue"] == 1:
            level += 1
        elif continue_to_play["Countinue"] == 0:
            print(f"\t\tWRONG ANSWER.")
            break
        else:
            print(f"You have retreated")
            break
    try:
        if continue_to_play["money_index_when_lose"] == 0:
            print("0$")
        elif continue_to_play["money_index_when_lose"] == 1:
            print(f"{prize[4]}$")
    except:
        placeholder = continue_to_play["money_index"]
        print(f"{prize[placeholder]}$")
    
    print("Game Over")
main()