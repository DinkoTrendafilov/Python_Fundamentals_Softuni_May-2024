number_of_teams = int(input())

teams = {}

for _ in range(number_of_teams):
    command = input().split()
    team_name = command[0]
    team_points = int(command[1])
    team_goals_scored = int(command[2])

    teams[team_name] = {"points": team_points, "goals": team_goals_scored}

for key, values in teams.items():
    print(f"{key} : {values['points']} points, {values['goals']} goals")

print()

sorted_teams = dict(sorted(teams.items(), key=lambda items: (-items[1]['points'], -items[1]['goals'])))

for team, values in sorted_teams.items():
    print(f"{team} : {values['points']} points, {values['goals']} goals")

