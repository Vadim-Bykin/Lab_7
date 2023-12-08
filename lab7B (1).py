# Лабораторная работа № 7, ООП
from itertools import combinations
from random import randint

# любители
class Prof:
    def __init__(self, name, score):
        self.name = name
        self.score = score

# профессионалы
class Jun:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Team:
    def __init__(self, people):
        self.COUNT = 4
        self.juns = []
        self.profs = []
        self.JUN_MAX_SCORE = 1000
        self.PROF_MIN_SCORE = 2400
        self.commands = []
        self.selected_commands = []
        self.distribution(people)
        self.form()

    def distribution(self, a):  # распределение любителей и профессионалов
        for i in a:
            if i[1] <= self.JUN_MAX_SCORE:
                self.juns.append(Jun(i[0], i[1]))
            elif i[1] >= self.PROF_MIN_SCORE:
                self.profs.append(Prof(i[0], i[1]))

    def form(self):  # формирование команды
        for i in range(self.COUNT + 1):
            for prof in combinations(self.profs, i):
                for jun in combinations(self.juns, self.COUNT - i):
                    cur_command = prof + jun
                    cur_score = 0
                    for item in cur_command:
                        cur_score += int(item.score)
                    self.commands.append([cur_command, cur_score, i, self.COUNT - i])

    def return_commands(self):  # все возможные команды
        count = 0
        print("Все возможные наборы команд")
        for command in self.commands:
            count += 1
            print(
                f"№ {count}: {command[0][0].name} ({command[0][0].score}) {command[0][1].name} ({command[0][1].score}) "
                f"{command[0][2].name} ({command[0][2].score}) {command[0][3].name} ({command[0][3].score}) - {command[1]}")

    def select_commands(self, count_juns, count_profs):  # вывод команды согласно условию
        for command in self.commands:
            if command[2] < count_profs:
                continue
            elif command[3] < count_juns:
                continue

            self.selected_commands.append(command)

        return self.selected_commands

    def select_best_commands(self):  # целевая функция
        max_score = 0
        best_commands = []
        for cur_command in self.selected_commands:
            if cur_command[1] > max_score:
                max_score = cur_command[1]

        for cur_command in self.selected_commands:
            if cur_command[1] == max_score:
                best_commands.append(cur_command)

        return best_commands

# список профессионалов (имена для удобства начинаются на П) и любителей (имена для удобства начинаются на Л)
team = Team([['Петр', randint(2400, 2900)], ['Павел', randint(2400, 2900)], ['Полина', randint(2400, 2900)],
            ['Пелагея', randint(2400, 2900)], ['Прохор', randint(2400, 2900)], ['Лёня', randint(0, 1000)],
            ['Люба', randint(0, 1000)], ['Людмила', randint(0, 1000)], ['Лев', randint(0, 1000)],
            ['Лаврентий', randint(0, 1000)]])

team.return_commands()
print('-----------------')
prof_count = int(input('Введите кол-во профессионалов: '))
jun_count = int(input('Введите кол-во любителей: '))

print(f'Все команды, удовлетворяющие условиям (не менее {prof_count} профессионалов и не менее {jun_count} любителя):')
print('Состав игроков, общий рейтинг команды')
select_teams = team.select_commands(jun_count, prof_count)
if len(select_teams) == 0:
    print("Команд, удовлетворяющих условиям не найдено")
else:
    for i in select_teams:
        for j in i[0]:
            print(j.name, end=' ')
        print(end='')
        print(' -', i[1])
    print('-----------------')
    print('Самые лучшие команды:')
    print('Состав игроков, общий рейтинг команды')
    for i in team.select_best_commands():
        for j in i[0]:
            print(j.name, end=' ')
        print(' -', i[1])
