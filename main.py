def players_repr(players: list[dict]):
    for player in players:
        print(f"{player['name']=}, {player['age']=}, {player['number']=}")


def players_add(players: list[dict]):
    new_player = {}

    name = input("Enter player name: ")
    age = input("Enter player age: ")
    number = input("Enter player number: ")

    new_player["name"] = name
    new_player["age"] = age
    new_player["number"] = number

    players.append(new_player)


def players_del(players: list[dict]):
    name = input("Enter player name to delete: ")
    i = 0
    for player in players:
        if player["name"] == name:
            players.pop(i)
        i += 1


def players_find(players: list[dict]):
    field = input("Enter player field to find: ")
    value = input("Enter player value to find: ")
    for player in players:
        if player[field] == value:
            print(player)
            return 0


def players_get_by_name(players: list[dict]):
    name = input("Enter player name to find: ")
    for player in players:
        if player["name"] == name:
            print(player)


def main():
    team = [
        {"name": "John", "age": "20", "number": "1"},
        {"name": "Marry", "age": "33", "number": "3"},
        {"name": "Cavin", "age": "33", "number": "12"},
    ]

    options = ["repr", "add", "del", "find", "get", "exit"]

    while True:
        user_choice = input(f"Enter your choice {options}:")

        if not user_choice:
            break

        if user_choice == "repr":
            players_repr(team)

        elif user_choice == "add":
            players_add(team)

        elif user_choice == "del":
            players_del(team)

        elif user_choice == "find":
            players_find(team)

        elif user_choice == "get":
            players_get_by_name(team)

        elif user_choice == "exit":
            break


if __name__ == "__main__":
    main()
