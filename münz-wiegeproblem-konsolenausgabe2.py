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
    # 1. Wägung: 1–4 vs. 5–8
    result1 = weigh(coins, [0, 1, 2, 3], [4, 5, 6, 7])

    if result1 == 0:  # Fälschung in 9–12
        result2 = weigh(coins, [8, 9, 10], [0, 1, 2])
        if result2 == 0:
            return 11, coins[11] == 12
        elif result2 == 1:  # eine von 9-11 schwerer
            result3 = weigh(coins, [8], [9])
            if result3 == 0:   return 10, True
            elif result3 == 1: return 8, True
            else:             return 9, True
        else:  # eine von 9-11 leichter
            result3 = weigh(coins, [8], [9])
            if result3 == 0:   return 10, False
            elif result3 == 1: return 9, False
            else:             return 8, False

    elif result1 == 1:  # 1-4 schwerer
        result2 = weigh(coins, [0, 1, 4], [2, 7, 9])
        if result2 == 0:
            result3 = weigh(coins, [5], [6])
            if result3 == 1:   return 6, False
            elif result3 == -1:return 5, False
            else:             return 3, True
        elif result2 == 1:
            result3 = weigh(coins, [0], [1])
            if result3 == 0:   return 7, False
            elif result3 == 1: return 0, True
            else:             return 1, True
        else:
            result3 = weigh(coins, [2], [0])
            if result3 == 1:   return 2, True
            elif result3 == -1:return 0, False
            else:             return 4, False

    else:  # 5-8 schwerer
        result2 = weigh(coins, [4, 5, 0], [3, 7, 9])
        if result2 == 0:
            result3 = weigh(coins, [1], [2])
            if result3 == 0:   return 6, True
            elif result3 == 1: return 2, False
            else:             return 1, False
        elif result2 == 1:
            result3 = weigh(coins, [4], [5])
            if result3 == 0:   return 3, False
            elif result3 == 1: return 4, True
            else:             return 5, True
        else:
            result3 = weigh(coins, [6], [7])
            if result3 == 0:   return 0, False
            elif result3 == 1: return 6, True
            else:             return 7, True


def main():
    simulationen = 100
    korrekt = 0

    print("=== 12-Münzen-Wägeproblem – 100 Simulationen ===\n")
    print("Eine von 12 Münzen ist zufällig zu leicht (8g) oder zu schwer (12g).\n"
          "Der Algorithmus versucht, sie in genau 3 Wägungen zu finden.\n")

    for sim in range(1, simulationen + 1):
        # Münzen vorbereiten
        coins = [10] * 12
        fake_index = random.randint(0, 11)
        is_heavier = random.choice([True, False])
        coins[fake_index] = 12 if is_heavier else 8

        # Algorithmus ausführen
        gefunden_index, gefunden_heavier = find_fake_coin(coins)

        # Ergebnis prüfen
        if gefunden_index == fake_index and gefunden_heavier == is_heavier:
            korrekt += 1
            status = "✓ RICHTIG"
        else:
            status = "✗ FALSCH"

        # Ausgabe jeder Simulation
        print(f"Simulation {sim:3d}: Gefälscht war Münze {fake_index + 1} "
              f"({'schwerer' if is_heavier else 'leichter'} ) → "
              f"Gefunden: Münze {gefunden_index + 1} "
              f"({'schwerer' if gefunden_heavier else 'leichter'} )  {status}")

    # Abschließende Statistik
    print("\n" + "="*60)
    print(f"          Ergebnis nach {simulationen} Simulationen")
    print("="*60)
    print(f"Korrekte Identifikationen: {korrekt} von {simulationen}")
    print(f"Genauigkeit: {100.0 * korrekt / simulationen:.2f} %")
    print("="*60)


if __name__ == "__main__":
    main()