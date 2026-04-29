import random

def weigh(coins, left, right):
    left_sum = sum(coins[i] for i in left)
    right_sum = sum(coins[i] for i in right)
    if left_sum < right_sum:
        return -1
    elif left_sum > right_sum:
        return 1
    return 0


def find_fake_coin(coins, fake_coin_index):
    # Erste Wägung: Münzen 1-4 (0-3) vs. 5-8 (4-7)
    result1 = weigh(coins, [0,1,2,3], [4,5,6,7])
    print("Wägung 1: Münzen 1-4 vs. 5-8: " +
          ("gleich" if result1 == 0 else ("1-4 schwerer" if result1 == 1 else "5-8 schwerer")))

    if result1 == 0:  # Fall: Erste Wägung ausgeglichen → Fälschung in 9-12
        result2 = weigh(coins, [8,9,10], [0,1,2])
        print("Wägung 2: Münzen 9-11 vs. 1-3: " +
              ("gleich" if result2 == 0 else ("9-11 schwerer" if result2 == 1 else "9-11 leichter")))

        if result2 == 0:  # Münze 12 ist falsch
            print("Wägung 3: Münze 1 vs. 12: " + ("12 schwerer" if coins[11] == coins[0] else "1 schwerer"))
            print(f"Ergebnis: Münze 12 ist {'schwerer' if coins[11] == coins[0] else 'leichter'}")
            return 11, coins[11] == 12

        else:  # result2 == 1 oder -1 → eine von 9-11 falsch
            result3 = weigh(coins, [8], [9])
            print("Wägung 3: Münze 9 vs. 10: " +
                  ("gleich" if result3 == 0 else ("9 schwerer" if result3 == 1 else "10 schwerer")))

            if result2 == 1:  # eine von 9-11 schwerer
                if result3 == 0:
                    print("Ergebnis: Münze 11 ist schwerer")
                    return 10, True
                elif result3 == 1:
                    print("Ergebnis: Münze 9 ist schwerer")
                    return 8, True
                else:
                    print("Ergebnis: Münze 10 ist schwerer")
                    return 9, True
            else:  # eine von 9-11 leichter
                if result3 == 0:
                    print("Ergebnis: Münze 11 ist leichter")
                    return 10, False
                elif result3 == 1:
                    print("Ergebnis: Münze 10 ist leichter")
                    return 9, False
                else:
                    print("Ergebnis: Münze 9 ist leichter")
                    return 8, False

    elif result1 == 1:  # 1-4 schwerer als 5-8
        result2 = weigh(coins, [0,1,4], [2,7,9])
        print("Wägung 2: Münzen 1,2,5 vs. 3,8,10: " +
              ("gleich" if result2 == 0 else ("1,2,5 schwerer" if result2 == 1 else "1,2,5 leichter")))

        if result2 == 0:
            result3 = weigh(coins, [5], [6])
            print("Wägung 3: Münze 6 vs. 7: " +
                  ("gleich" if result3 == 0 else ("6 schwerer" if result3 == 1 else "7 schwerer")))
            if result3 == 1:
                print("Ergebnis: Münze 7 ist leichter")
                return 6, False
            elif result3 == -1:
                print("Ergebnis: Münze 6 ist leichter")
                return 5, False
            else:
                print("Ergebnis: Münze 4 ist schwerer")
                return 3, True

        elif result2 == 1:
            result3 = weigh(coins, [0], [1])
            print("Wägung 3: Münze 1 vs. 2: " +
                  ("gleich" if result3 == 0 else ("1 schwerer" if result3 == 1 else "2 schwerer")))
            if result3 == 0:
                print("Ergebnis: Münze 8 ist leichter")
                return 7, False
            elif result3 == 1:
                print("Ergebnis: Münze 1 ist schwerer")
                return 0, True
            else:
                print("Ergebnis: Münze 2 ist schwerer")
                return 1, True

        else:  # result2 == -1
            result3 = weigh(coins, [2], [0])
            print("Wägung 3: Münze 3 vs. 1: " +
                  ("gleich" if result3 == 0 else ("3 schwerer" if result3 == 1 else "1 schwerer")))
            if result3 == 1:
                print("Ergebnis: Münze 3 ist schwerer")
                return 2, True
            elif result3 == -1:
                print("Ergebnis: Münze 1 ist leichter")
                return 0, False
            else:
                print("Ergebnis: Münze 5 ist leichter")
                return 4, False

    else:  # result1 == -1 → 5-8 schwerer als 1-4
        result2 = weigh(coins, [4,5,0], [3,7,9])
        print("Wägung 2: Münzen 5,6,1 vs. 4,8,10: " +
              ("gleich" if result2 == 0 else ("5,6,1 schwerer" if result2 == 1 else "5,6,1 leichter")))

        if result2 == 0:
            result3 = weigh(coins, [1], [2])
            print("Wägung 3: Münze 2 vs. 3: " +
                  ("gleich" if result3 == 0 else ("2 schwerer" if result3 == 1 else "3 schwerer")))
            if result3 == 0:
                print("Ergebnis: Münze 7 ist schwerer")
                return 6, True
            elif result3 == 1:
                print("Ergebnis: Münze 3 ist leichter")
                return 2, False
            else:
                print("Ergebnis: Münze 2 ist leichter")
                return 1, False

        elif result2 == 1:
            result3 = weigh(coins, [4], [5])
            print("Wägung 3: Münze 5 vs. 6: " +
                  ("gleich" if result3 == 0 else ("5 schwerer" if result3 == 1 else "6 schwerer")))
            if result3 == 0:
                print("Ergebnis: Münze 4 ist leichter")
                return 3, False
            elif result3 == 1:
                print("Ergebnis: Münze 5 ist schwerer")
                return 4, True
            else:
                print("Ergebnis: Münze 6 ist schwerer")
                return 5, True

        else:  # result2 == -1
            result3 = weigh(coins, [6], [7])
            print("Wägung 3: Münze 7 vs. 8: " +
                  ("gleich" if result3 == 0 else ("7 schwerer" if result3 == 1 else "8 schwerer")))
            if result3 == 0:
                print("Ergebnis: Münze 1 ist leichter")
                return 0, False
            elif result3 == 1:
                print("Ergebnis: Münze 7 ist schwerer")
                return 6, True
            else:
                print("Ergebnis: Münze 8 ist schwerer")
                return 7, True


def main():
    simulationen = 100
    korrekt = 0

    print("Ziel ist es, eine gefälschte Münze zu finden.")
    print("Eine von 12 Münzen ist entweder zu leicht oder zu schwer. Man darf nur dreimal wiegen.\n")

    for sim in range(simulationen):
        coins = [10] * 12
        fake_coin = random.randint(0, 11)
        is_heavier = random.choice([True, False])
        coins[fake_coin] = 12 if is_heavier else 8

        print(f"\nSimulation gestartet. Eine Münze ist gefälscht.")
        print(f"\t(Für Testzwecke: Münze {fake_coin + 1} ist "
              f"{'schwerer (12g)' if is_heavier else 'leichter (8g)'})")

        # Algorithmus ausführen und Ergebnis prüfen
        gefunden_index, gefunden_heavier = find_fake_coin(coins, fake_coin)

        if gefunden_index == fake_coin and gefunden_heavier == is_heavier:
            korrekt += 1

        print()  # Leerzeile zwischen Simulationen

    print(f"Korrekte Identifikationen: {korrekt}")
    print(f"Genauigkeit: {100.0 * korrekt / simulationen:.2f}%")

if __name__ == "__main__":
    main()