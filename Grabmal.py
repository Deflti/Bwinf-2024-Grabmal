class Solution:
    def loesung(self, pPath):
        # Öffnet die Datei im Lesemodus und speichert alle Zeilen in einer Liste
        with open(pPath, "r") as file:
            lines = file.readlines()

        # Liest die erste Zeile und konvertiert sie in einen Integer, welcher angibt wie viele Quader folgen
        n = int(lines[0])

        # Initialisiert die Variable 'summe_zeit' mit 1, um die Zeit später zu berechnen
        summe_zeit = 1

        # For schleife, die über die nächsten n Zeilen der Datei iteriert und diese mal rechnet
        for i in range(n):
            scalar = int(lines[i + 1])  # Liest und konvertiert die aktuelle Zeile in einen Integer
            if scalar > 0:  # Überprüft, ob die Zahl groeßer als 0 ist
                summe_zeit *= scalar  # Multipliziert summe_zeit mit scalar, falls groeßer 0

        # Gibt die berechnete Wartezeit mal 2 und Minus 1 aus in Minuten
        # Dadurch wird sicher gestellt, dass alle Quader zur selben Zeit geöffnet sind
        print(f"Warte {summe_zeit * 2 - 1} Minuten")
        
        # Gibt die Anzahl der Schritte aus, die gelaufen werden (was immer n sein wird)
        print(f"Gehe {n} nach vorne")

# Startpunkt des Programms
if __name__ == "__main__":
    Solution().loesung("Eingabe.txt")