import re

team_file = "browns.txt"

OFFENSE = "OFFENSE"
DEFENSE = "DEFENSE"
ST = "SPECIAL"


class Player:
    def __init__(self, name, string, rank, max_rank):
        self.name = name
        self.string = string
        self.rank = rank
        self.max_rank = max_rank


def main():
    with open(team_file, "r") as file:
        lines = file.readlines()

    team = {OFFENSE: {}, DEFENSE: {}, ST: {}}
    mode = OFFENSE
    for line in lines:
        chunks = line.rstrip().split()

        if chunks[0] == OFFENSE:
            mode = OFFENSE
            continue
        elif chunks[0] == DEFENSE:
            mode = DEFENSE
            continue
        elif chunks[0] == ST:
            mode = ST
            continue

        position, player_ranks, max_rank = read_position_players(chunks[0], team, mode)

        get_players(chunks, team, mode, position, player_ranks, max_rank)

    print("do something here")


def read_position_players(raw_position, team, mode):
    position = raw_position.lstrip("LR")
    if position not in team[mode]:
        team[mode][position] = []

    if position == "DE" or position == "DT" or position == "NT" or position == "RUSH":
        player_file = "DL.tsv"
    elif "LB" in position or position == "B":
        player_file = "LB.tsv"
    elif position == "CB" or position == "FS" or position == "SS" or position == "SAM":
        player_file = "DB.tsv"
    elif position == "FB":
        player_file = "RB.tsv"
    elif position == "PK":
        player_file = "K.tsv"
    else:
        player_file = position + ".tsv"

    with open(player_file) as file:
        raw_lines = file.readlines()
    lines = [l for l in raw_lines if re.search("\S", l)]
    max_rank = len(lines)

    player_ranks = {}
    for line in lines:
        chunks = line.split()
        if len(chunks) > 2:
            rank = chunks[0]
            name = " ".join(chunks[1:])

            player_ranks[name] = rank

    return position, player_ranks, max_rank


def get_players(chunks, team, mode, position, player_ranks, max_rank):
    position_done = False
    i = 2
    string = 1

    while not position_done:

        surname = ""
        surname_done = False
        while not surname_done:
            name = chunks[i]
            if name[-1] == ",":
                surname_done = True
                name = name.rstrip(",")
            surname += name + " "
            i += 1

        full_name = chunks[i] + " " + surname
        full_name = full_name.rstrip()

        rank = "UNRANKED"
        if full_name in player_ranks:
            rank = player_ranks[full_name]

        player = Player(full_name, string, rank, max_rank)
        team[mode][position].append(player)

        i += 3
        string += 1
        if i >= len(chunks):
            position_done = True


if __name__ == '__main__':
    main()
