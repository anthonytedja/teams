import csv, random

# RETURN DICTIONARY OF TEAMS FROM RAW DATA
def get_teams(data, num_teams, size):
    dic = {}
    i = 0
    for i in range(num_teams):
        dic[COLORS[i]] = LEADERS[COLORS[i]] + DATA[i * size: (i + 1) * size]
    end = (i + 1) * size
    for j in range(len(data[end:])):
        dic[COLORS[j]] = dic.get(COLORS[j]) + [DATA[j + end]]
    return dic

# RETURN AVERAGE ABILITY OF TEAMS IN CATEGORIES
def team_value(teams):
    values = []
    i = 0
    for team in teams.values():
        offense = support = defense = total = 0
        players = len(team)
        for player in team:
            offense += player[1]
            support += player[2]
            defense += player[3]
            total += player[4]
        values.append((COLORS[i], int(offense / players * 100), int(support / players * 100),
                        int(defense / players * 100), int(total / players * 100)))
        i += 1
    return values

# RETURN VARIANCE OF DATA
def variance(data, n):
    # n = number of teams
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / n

# CALCULATE TEAM VARIANCES FROM TEAM DATA
def calculate(data):
    teams = team_value(data)

    o = []
    s = []
    d = []

    for team in teams:
        o.append(team[1])
        s.append(team[2])
        d.append(team[3])

    var = [variance(o, TEAMS), variance(s, TEAMS), variance(d, TEAMS)]
    return teams, var

# PRINT TEAM AND STATS
def print_team(teams, score):
    print('')
    i = 0
    for k, v in teams.items():
        team = []
        for player in v:
            team.append(player[0])
        print(k, ':', team, score[i][1:])
        i += 1
    print('')

DATA = []
TEAMS = 0
INITIAL = {}
COLORS = ['GREEN', 'RED', 'BLACK', 'WHITE', 'BLUE', 'YELLOW', 'PURPLE', 'PINK', 'ORANGE']
LEADERS = {}
HEADER = []
PATH = 'sample.csv'

# CSV INSTRUCTIONS
# 
# A NEW LINE SIGIFIES THE START OF A NEW TEAM
# THE FIRST PLAYER IN A TEAM IS ASSUMED TEAM CAPTAIN SO TEAMS WILL ONLY HAVE ONE TEAM CAPTAIN
# EACH ROW IS PLAYERNAME, PLAYER OFFENSE (0-10), PLAYER SUPPORT (0-10), PLAYER DEFENSE (0-10)
with open(PATH, 'r') as file:
    reader = csv.reader(file)
    HEADER = next(reader)
    new = True
    for row in reader:
        if row == []:
            new = True
        else:
            TEAMS += new
            offense, support, defense = int(row[1]), int(row[2]), int(row[3])
            player = [row[0], offense, support, defense, offense + support + defense]
            color = COLORS[TEAMS - 1]
            INITIAL[color] = INITIAL.get(color, []) + [player]
            if new:
                LEADERS[color] = [player]
            else:
                DATA.append(player)
            new = False

NUMBER = len(DATA)
SIZE = NUMBER // TEAMS
BEST = [float('inf')] * 3
CURR = INITIAL
BEST_TEAM = INITIAL

# ITERATE THROUGH RANDOM TEAMS TO FIND TEAM COMBINATION WITH MINIMUM VARIANCE
LOOP = 500000
FULL = LOOP * 10
for x in range(FULL + 1):
    SCORE, VALUE = calculate(CURR)

    # if VALUE[0] <= BEST[0] and VALUE[1] <= BEST[1] and VALUE[2] <= BEST[2]:   DIFFERENT ALGO
    if sum(VALUE) <= sum(BEST):
        BEST = VALUE
        BEST_TEAM = CURR

        print_team(CURR, SCORE)
        print('VARIANCE:', VALUE, '\n')

    if x % LOOP == 0:
        print('\n', x * 100 // FULL, '% COMPLETE\n')

    random.shuffle(DATA)
    CURR = get_teams(DATA, TEAMS, SIZE)

# WRITE BEST TEAM BACK TO FILE
with open(PATH, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(HEADER)
    writer.writerow([])
    for team in BEST_TEAM.values():
        for player in team:
            writer.writerow(player)
        writer.writerow([])
