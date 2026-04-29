import random

def weigh(coins, left, right):
    """Vergleicht zwei Gruppen von Münzen.
    Rückgabe: -1 (links leichter), 0 (gleich), 1 (links schwerer)"""
    left_sum = sum(coins[i] for i in left)
    right_sum = sum(coins[i] for i in right)
    if left_sum < right_sum:
        return -1
    elif left_sum > right_sum:
        return 1
    return 0


def find_fake_coin(coins):
    """Führt die drei Wägungen durch und gibt (index, ist_schwerer) der falschen Münze zurück."""
    # 1. Wägung: Münzen 1–4 (0-3) vs. 5–8 (4-7)
    result1 = weigh(coins, [0, 1, 2, 3], [4, 5, 6, 7])

    if result1 == 0:  # ausgeglichen → Fälschung in 9–12
        result2 = weigh(coins, [8, 9, 10], [0, 1, 2])  # 9-11 vs. 1-3

        if result2 == 0:  # ausgeglichen → Münze 12
            return 11, coins[11] == 12
        elif result2 == 1:  # 9-11 schwerer
            result3 = weigh(coins, [8], [9])
            if result3 == 0:
                return 10, True   # Münze 11 schwerer
            elif result3 == 1:
                return 8, True    # Münze 9 schwerer
            else:
                return 9, True    # Münze 10 schwerer
        else:  # 9-11 leichter
            result3 = weigh(coins, [8], [9])
            if result3 == 0:
                return 10, False
            elif result3 == 1:
                return 9, False
            else:
                return 8, False

    elif result1 == 1:  # 1-4 schwerer
        result2 = weigh(coins, [0, 1, 4], [2, 7, 9])  # 1,2,5 vs. 3,8,10

        if result2 == 0:
            result3 = weigh(coins, [5], [6])
            if result3 == 1:
                return 6, False   # Münze 7 leichter
            elif result3 == -1:
                return 5, False   # Münze 6 leichter
            else:
                return 3, True    # Münze 4 schwerer
        elif result2 == 1:
            result3 = weigh(coins, [0], [1])
            if result3 == 0:
                return 7, False   # Münze 8 leichter
            elif result3 == 1:
                return 0, True
            else:
                return 1, True
        else:
            result3 = weigh(coins, [2], [0])
            if result3 == 1:
                return 2, True
            elif result3 == -1:
                return 0, False
            else:
                return 4, False

    else:  # 5-8 schwerer
        result2 = weigh(coins, [4, 5, 0], [3, 7, 9])  # 5,6,1 vs. 4,8,10

        if result2 == 0:
            result3 = weigh(coins, [1], [2])
            if result3 == 0:
                return 6, True
            elif result3 == 1:
                return 2, False
            else:
                return 1, False
        elif result2 == 1:
            result3 = weigh(coins, [4], [5])
            if result3 == 0:
                return 3, False
            elif result3 == 1:
                return 4, True
            else:
                return 5, True
        else:
            result3 = weigh(coins, [6], [7])
            if result3 == 0:
                return 0, False
            elif result3 == 1:
                return 6, True
            else:
                return 7, True


def main():
    simulationen = 100
    korrekt = 0

    print("12-Münzen-Wägeproblem: Finde die gefälschte Münze (leicht oder schwer) in 3 Wägungen.")
    print(f"Anzahl Simulationen: {simulationen}\n")

    for sim in range(1, simulationen + 1):
        # Münzen initialisieren (alle 10g)
        coins = [10] * 12

        # Zufällige Fälschung
        fake_index = random.randint(0, 11)
        is_heavier = random.choice([True, False])
        coins[fake_index] = 12 if is_heavier else 8

        # Algorithmus ausführen
        gefunden_index, gefunden_heavier = find_fake_coin(coins)

        if gefunden_index == fake_index and gefunden_heavier == is_heavier:
            korrekt += 1
        else:
            # Optional: Bei Fehler anzeigen (zum Debuggen)
            print(f"FEHLER in Simulation {sim}: Erwartet Münze {fake_index+1} "
                  f"{'schwerer' if is_heavier else 'leichter'}, "
                  f"gefunden Münze {gefunden_index+1} {'schwerer' if gefunden_heavier else 'leichter'}")

    genauigkeit = 100.0 * korrekt / simulationen
    print("\n" + "="*50)
    print(f"Ergebnis nach {simulationen} Simulationen:")
    print(f"Korrekte Identifikationen: {korrekt} von {simulationen}")
    print(f"Genauigkeit: {genauigkeit:.2f}%")
    print("="*50)


if __name__ == "__main__":
    main()