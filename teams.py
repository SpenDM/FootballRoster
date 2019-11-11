import re

roster_file = "wr_ranks.txt"
position = "WR"


def main():
    with open(roster_file, "r") as file:
        lines = file.readlines()

    format_file(lines)

    # roster = parse_roster(lines)


def parse_roster(lines):
    roster = {}
    return roster


def format_file(lines):
    players = []
    rank = 1
    for line in lines:
        if line[0].isalpha():

            chunks = line.split()
            player = str(rank) + " " + chunks[0] + " " + re.sub(position, "", chunks[1])
            players.append(player+"\n")

            rank += 1

    filename = position + ".tsv"
    with open(filename, "w") as file:
        file.writelines(players)


if __name__ == '__main__':
    main()
