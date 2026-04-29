
import java.io.*;
import java.util.Random;

public class CoinWeighingProblem_mit_Statistik_mit_Ausgabe {
    public static void main(String[] args) {
        try (PrintWriter writer = new PrintWriter(new FileWriter("output.txt"))) {
            writer.println("Ziel ist es, eine gefälschte Münze zu finden.");
            writer.println("Eine von 12 Münzen ist entweder zu leicht oder zu schwer. Man darf nur dreimal wiegen.\n");

            int simulationen = 1200; // Anzahl der Simulationen
            int richtigeIdentifikationen = 0;

            for (int sim = 0; sim < simulationen; sim++) {
                int[] coins = new int[12];
                for (int i = 0; i < 12; i++) {
                    coins[i] = 10;
                }

                Random rand = new Random();
                int fakeCoin = rand.nextInt(12);
                boolean isHeavier = rand.nextBoolean();
                coins[fakeCoin] = isHeavier ? 12 : 8;
                writer.println("\nSimulation gestartet. Eine Münze ist gefälscht.");
                writer.println("\t(Für Testzwecke: Münze " + (fakeCoin + 1) + " ist " + 
                              (isHeavier ? "schwerer (12g)" : "leichter (8g)") + ")");

                // Führe die Wägungen durch
                if (findFakeCoin(coins, fakeCoin, writer)) {
                    richtigeIdentifikationen++;
                }
            }

            writer.println("Korrekte Identifikationen: " + richtigeIdentifikationen);
            writer.println("Genauigkeit: " + (100.0 * richtigeIdentifikationen / simulationen) + "%");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
      public static int weigh(int[] coins, int[] left, int[] right) {
        int leftSum = 0, rightSum = 0;
        for (int i : left) leftSum += coins[i];
        for (int i : right) rightSum += coins[i];
        if (leftSum < rightSum) return -1;
        if (leftSum > rightSum) return 1;
        return 0;
    }
    
    public static boolean findFakeCoin(int[] coins, int fakeCoin,PrintWriter writer) {
    int identifiedCoin = -1; // Index der identifizierten Münze
    boolean identifiedHeavier = false; // Ist die identifizierte Münze schwerer?

    int[] left1 = {0, 1, 2, 3};
    int[] right1 = {4, 5, 6, 7};
    int result1 = weigh(coins, left1, right1);
    writer.println("Wägung 1: Münzen 1-4 vs. 5-8: " + 
                      (result1 == 0 ? "gleich" : (result1 == 1 ? "1-4 schwerer" : "5-8 schwerer")));

    if (result1 == 0) {
        int[] left2 = {8, 9, 10};
        int[] right2 = {0, 1, 2};
        int result2 = weigh(coins, left2, right2);
        writer.println("Wägung 2: Münzen 9-11 vs. 1-3: " + 
                          (result2 == 0 ? "gleich" : (result2 == 1 ? "9-11 schwerer" : "9-11 leichter")));

        if (result2 == 0) {
            identifiedCoin = 11; // Münze 12
            identifiedHeavier = coins[11] == 12;
            writer.println("Wägung 3: Münze 1 vs. 12: " + (coins[11] == 12 ? "12 schwerer" : "1 schwerer"));
            writer.println("Ergebnis: Münze 12 ist " + (coins[11] == 12 ? "schwerer" : "leichter"));
        } else if (result2 == 1) {
            int result3 = weigh(coins, new int[]{8}, new int[]{9});
            writer.println("Wägung 3: Münze 9 vs. 10: " + 
                              (result3 == 0 ? "gleich" : (result3 == 1 ? "9 schwerer" : "10 schwerer")));
            if (result3 == 0) { identifiedCoin = 10; identifiedHeavier = true; writer.println("Ergebnis: Münze 11 ist schwerer"); }
            else if (result3 == 1) { identifiedCoin = 8; identifiedHeavier = true; writer.println("Ergebnis: Münze 9 ist schwerer"); }
            else { identifiedCoin = 9; identifiedHeavier = true; writer.println("Ergebnis: Münze 10 ist schwerer"); }
        } else {
            int result3 = weigh(coins, new int[]{8}, new int[]{9});
            writer.println("Wägung 3: Münze 9 vs. 10: " + 
                              (result3 == 0 ? "gleich" : (result3 == 1 ? "9 schwerer" : "10 schwerer")));
            if (result3 == 0) { identifiedCoin = 10; identifiedHeavier = false; writer.println("Ergebnis: Münze 11 ist leichter"); }
            else if (result3 == 1) { identifiedCoin = 9; identifiedHeavier = false; writer.println("Ergebnis: Münze 10 ist leichter"); }
            else { identifiedCoin = 8; identifiedHeavier = false; writer.println("Ergebnis: Münze 9 ist leichter"); }
        }
    } else if (result1 == 1) {
        int[] left2 = {0, 1, 4};
        int[] right2 = {2, 7, 9};
        int result2 = weigh(coins, left2, right2);
        writer.println("Wägung 2: Münzen 1,2,5 vs. 3,8,10: " + 
                          (result2 == 0 ? "gleich" : (result2 == 1 ? "1,2,5 schwerer" : "1,2,5 leichter")));

        if (result2 == 0) {
            int result3 = weigh(coins, new int[]{5}, new int[]{6});
            writer.println("Wägung 3: Münze 6 vs. 7: " + 
                              (result3 == 0 ? "gleich" : (result3 == 1 ? "6 schwerer" : "7 schwerer")));
            if (result3 == 1) { identifiedCoin = 6; identifiedHeavier = false; writer.println("Ergebnis: Münze 7 ist leichter"); }
            else if (result3 == -1) { identifiedCoin = 5; identifiedHeavier = false; writer.println("Ergebnis: Münze 6 ist leichter"); }
            else { identifiedCoin = 3; identifiedHeavier = true; writer.println("Ergebnis: Münze 4 ist schwerer"); }
        } else if (result2 == 1) {
            int result3 = weigh(coins, new int[]{0}, new int[]{1});
            writer.println("Wägung 3: Münze 1 vs. 2: " + 
                              (result3 == 0 ? "gleich" : (result3 == 1 ? "1 schwerer" : "2 schwerer")));
            if (result3 == 0) { identifiedCoin = 7; identifiedHeavier = false; writer.println("Ergebnis: Münze 8 ist leichter"); }
            else if (result3 == 1) { identifiedCoin = 0; identifiedHeavier = true; writer.println("Ergebnis: Münze 1 ist schwerer"); }
            else { identifiedCoin = 1; identifiedHeavier = true; writer.println("Ergebnis: Münze 2 ist schwerer"); }
        } else {
            int result3 = weigh(coins, new int[]{2}, new int[]{0});
            writer.println("Wägung 3: Münze 3 vs. 1: " + 
                              (result3 == 0 ? "gleich" : (result3 == 1 ? "3 schwerer" : "1 schwerer")));
            if (result3 == 1) { identifiedCoin = 2; identifiedHeavier = true; writer.println("Ergebnis: Münze 3 ist schwerer"); }
            else if (result3 == -1) { identifiedCoin = 0; identifiedHeavier = false; writer.println("Ergebnis: Münze 1 ist leichter"); }
            else { identifiedCoin = 4; identifiedHeavier = false; writer.println("Ergebnis: Münze 5 ist leichter"); }
        }
    } else {
        int[] left2 = {4, 5, 0};
        int[] right2 = {3, 7, 9};
        int result2 = weigh(coins, left2, right2);
        writer.println("Wägung 2: Münzen 5,6,1 vs. 4,8,10: " + 
                          (result2 == 0 ? "gleich" : (result2 == 1 ? "5,6,1 schwerer" : "5,6,1 leichter")));

        if (result2 == 0) {
            int result3 = weigh(coins, new int[]{1}, new int[]{2});
            writer.println("Wägung 3: Münze 2 vs. 3: " + 
                              (result3 == 0 ? "gleich" : (result3 == 1 ? "2 schwerer" : "3 schwerer")));
            if (result3 == 0) { identifiedCoin = 6; identifiedHeavier = true; writer.println("Ergebnis: Münze 7 ist schwerer"); }
            else if (result3 == 1) { identifiedCoin = 2; identifiedHeavier = false; writer.println("Ergebnis: Münze 3 ist leichter"); }
            else { identifiedCoin = 1; identifiedHeavier = false; writer.println("Ergebnis: Münze 2 ist leichter"); }
        } else if (result2 == 1) {
            int result3 = weigh(coins, new int[]{4}, new int[]{5});
            writer.println("Wägung 3: Münze 5 vs. 6: " + 
                              (result3 == 0 ? "gleich" : (result3 == 1 ? "5 schwerer" : "6 schwerer")));
            if (result3 == 0) { identifiedCoin = 3; identifiedHeavier = false; writer.println("Ergebnis: Münze 4 ist leichter"); }
            else if (result3 == 1) { identifiedCoin = 4; identifiedHeavier = true; writer.println("Ergebnis: Münze 5 ist schwerer"); }
            else { identifiedCoin = 5; identifiedHeavier = true; writer.println("Ergebnis: Münze 6 ist schwerer"); }
        } else {
            int result3 = weigh(coins, new int[]{6}, new int[]{7});
            writer.println("Wägung 3: Münze 7 vs. 8: " + 
                              (result3 == 0 ? "gleich" : (result3 == 1 ? "7 schwerer" : "8 schwerer")));
            if (result3 == 0) { identifiedCoin = 0; identifiedHeavier = false; writer.println("Ergebnis: Münze 1 ist leichter"); }
            else if (result3 == 1) { identifiedCoin = 6; identifiedHeavier = true; writer.println("Ergebnis: Münze 7 ist schwerer"); }
            else { identifiedCoin = 7; identifiedHeavier = true; writer.println("Ergebnis: Münze 8 ist schwerer"); }
        }
    }

    // Vergleich mit der tatsächlichen gefälschten Münze
    boolean isHeavier = coins[fakeCoin] == 12;
    return identifiedCoin == fakeCoin && identifiedHeavier == isHeavier;
    
}

}
