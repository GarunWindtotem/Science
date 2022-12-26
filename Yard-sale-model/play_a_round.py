import numpy as np
from matplotlib import pyplot as plt

# context: simulating Yard-Sale-model
# input: money of two players
# output: money after one round of play of two players
# output: count the numbers who won

def play_a_round(A, B):

    # 1) berechne den Einsatz für Spieler A und B
    Einsatz_A = A * 0.2
    Einsatz_B = B * 0.2

    # 2) der Spieler mit dem geringeren Einsatz bestimmt den Spieleinsatz
    if Einsatz_A <= Einsatz_B:
          Spieleinsatz = Einsatz_A
    else:
          Spieleinsatz = Einsatz_B
    # print(f'Spieleinsatz= {Spieleinsatz}')

    CountWinner_A = 0
    CountWinnner_B = 0

    # 3) Kopf oder Zahl (Zufallszahl 0 oder 1) um Gewinner zu bestimmen
    # 0: Spieler A gewinnt, 1: Spieler B gewinnt
    head_or_tail = int(np.random.randint(0, 2, size=1))
    if head_or_tail == 1:
          A = A - Spieleinsatz
          B = B + Spieleinsatz
          CountWinnner_B = 1
         # print('player B wins')
    else:
          A = A + Spieleinsatz
          B = B - Spieleinsatz
          CountWinner_A = 1
         # print('player A wins')
    return A, B, CountWinner_A, CountWinnner_B


for i in range(0, 101):

    # Anzahl Spiele
    N = 1_000

    # Kontostände der Spieler bei Spielstart
    A = 100
    B = 1_000

    # Kontostände in Liste
    Kontostand_A_list = []
    Kontostand_B_list = []
    Kontostand_A_list.append(A)
    Kontostand_B_list.append(B)

    CountWinner_A_list = []
    CountWinner_B_list = []


    for item in range(1, N):

        # call function
        values = play_a_round(A, B)
        l = [*values]
        A = l[0]
        B = l[1]
        CountWinner_A = l[2]
        CountWinner_B = l[3]
        # Spielergebnisse speichern
        Kontostand_A_list.append(A)
        Kontostand_B_list.append(B)
        # Zähle Gewinner
        CountWinner_A_list.append(CountWinner_A)
        CountWinner_B_list.append(CountWinner_B)

    # Bestimme den Gewinner
    Ergebnis_A = Kontostand_A_list[-1]
    Ergebnis_B = Kontostand_B_list[-1]

    if Ergebnis_A > Ergebnis_B:
        winner = "A"
    elif Ergebnis_A < Ergebnis_B:
        winner = "B"
    else:
        winner ="draw"

    AmoutWonGamesA = sum(CountWinner_A_list)
    AmoutWonGamesB = sum(CountWinner_B_list)

    # print(AmoutWonGamesA, AmoutWonGamesB)
    # create index list for plot
    x = []
    for item in range(0, N):
        x.append(item)

    # print(len(x))
    # visualize
    # fix, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
    # ax1.plot(x, Kontostand_A_list)
    # ax2.plot(x, Kontostand_B_list)
    # plt.show()

    plt.figure(figsize=(16, 9))
    plt.style.use('seaborn-v0_8')
    plt.grid(True)

    plt.plot(x, Kontostand_A_list, color='red', marker='', markerfacecolor='grey', label="player A")
    plt.plot(x, Kontostand_B_list, color='blue', marker='', markerfacecolor='grey', label="player B")
    plt.title("Yard-sale-model simulation", fontsize=40)
    plt.suptitle(f'Player A won: {AmoutWonGamesA}, Player B won: {AmoutWonGamesB}, Ergebnis A:{round(Ergebnis_A,1)} B: {round(Ergebnis_B,1)}')
    plt.xlabel('Anzahl Spiele', fontsize=25)
    plt.ylabel('Kontostand', fontsize=25) 
    plt.legend(loc='upper center',
        bbox_to_anchor=(0.5, -0.1),
        fancybox=True,
        shadow=True,
        ncol=4,
        fontsize=25)
       
    plt.savefig(f'{int(sum(Kontostand_A_list))} game_series_{i}, winner {winner}.png', dpi=300, bbox_inches='tight')
    # plt.show()
    plt.close()
