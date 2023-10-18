import game_data
import random
def main():
    get_choice()

def get_data(data):
    temp = []
    first = random.randint(0,len(data))
    temp.append(data[first])
    print(f"Compare A:", data[first]["name"], data[first]["description"]," from ", data[first]["country"])
    del data[first]
    second = random.randint(0,len(data))
    temp.append(data[second])
    print(f"Against B:", data[second]["name"], data[second]["description"], " from ", data[second]["country"])
    del data[second]
    return temp

def get_choice():
    while True:
        try:
            compare_list = get_data(game_data.data)
            user_choice = str(input("Who has more followers? Type 'A' or 'B' "))
            if user_choice != 'A' and user_choice != 'B':
                print("Type only 'A' or 'B': ")
            elif user_choice == 'A' or user_choice == 'B':
                compare(user_choice, compare_list)
        except ValueError:
            print("Only 'A' or 'B' allowed: ")
            pass

def compare(user_choice,compare_list):
    if user_choice == 'A':
        choice = int((compare_list[0]["follower_count"]))
        choice_versus = int((compare_list[0]["follower_count"]))
        if choice > choice_versus:
            print("You Win! ", choice, "followers versus", choice_versus)
            get_choice()
        elif choice < choice_versus:
            print("You Lost! ", choice, "followers versus", choice_versus)

    if user_choice == 'B':
        choice = int((compare_list[1]["follower_count"]))
        choice_versus = int((compare_list[0]["follower_count"]))
        if choice > choice_versus:
            print("You Win! ", choice, "followers versus", choice_versus)
            get_choice()
        elif choice < choice_versus:
            print("You Lost! ", choice, "followers versus", choice_versus)




if __name__ == '__main__':
    main()
