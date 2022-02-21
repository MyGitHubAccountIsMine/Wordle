import csv
import matplotlib.pyplot as plt
import pandas as pd


def edit_csv(player, won, lost, amn_tries_per_win, word):
    games = len(pd.read_csv("WordleSheet.csv"))+1
    list_data = [str(games), player, won, lost, amn_tries_per_win, word]
    with open('WordleSheet.csv', 'a') as file:
        writer_object = csv.writer(file)
        writer_object.writerow(list_data)
        file.close()
    stats(player)


def stats(player):
    overall_wordle_sheet = pd.read_csv('WordleSheet.csv', index_col=0)
    wordle_sheet = overall_wordle_sheet.query(f"Player == '{player}'")
    games = len(wordle_sheet)
    won_column = wordle_sheet['Won']
    won_times = 0
    for i in won_column:
        if i:
            won_times += 1
    lost_column = wordle_sheet['Lost']
    lost_times = 0
    for i in lost_column:
        if i:
            lost_times += 1
    win_percentage = (won_times / games) * 100
    if lost_times != 0:
        win_loss_ratio = f"{won_times}/{lost_times}"
    else:
        win_loss_ratio = f"{won_times}/0"
    print(f"Player: {player}\nWin Percentage: {win_percentage}%\nWin Loss Ratio: {win_loss_ratio}")


def more_stats(player):
    overall_wordle_sheet = pd.read_csv('WordleSheet.csv', index_col=0)
    wordle_sheet = overall_wordle_sheet.query(f"Player == '{player}'")
    try_per_win_column = wordle_sheet['Amount Of Tries/Win']
    try_per_win = ""
    for i in try_per_win_column:
        try_per_win += str(i)
    x_axis = [1, 2, 3, 4, 5, 6]
    y_axis = [try_per_win.count('1'), try_per_win.count('2'), try_per_win.count('3'), try_per_win.count('4'), try_per_win.count('5'), try_per_win.count('6')]
    plotdata = pd.DataFrame({
        "Amount": y_axis},
        index=x_axis)
    plotdata.plot(kind='bar', figsize=(15, 8))
    plt.title(f"Amount Of Tries Per Win. Player: {player}")
    plt.xlabel("Number")
    plt.ylabel("Amount")
    plt.show()

