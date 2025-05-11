# 🏺 Grabmal – Algorithmische Wegfindung durch ein Fallenlabyrinth

## Projektbeschreibung

Dieses Projekt beschäftigt sich mit einem algorithmischen Problem, das an Szenarien aus Computerspielen oder Abenteuerfilmen erinnert: Eine Spielfigur, Petra, muss ein Grabmal erreichen, das nur über einen langen Gang zugänglich ist. Der Gang besteht aus Abschnitten, die jeweils von periodisch bewegten Steinquadern blockiert werden. Ziel ist es, einen Algorithmus zu entwickeln, der den schnellstmöglichen Pfad durch dieses gefährliche Labyrinth berechnet – unter Berücksichtigung der Öffnungs- und Schließzeiten der Quader.

## Aufgabenstellung

Viele Computerspiele, Abenteuer- und Science-Fiction-Filme enthalten gefährliche Fallen, durch welche die Heldin oder der Held durch geschicktes Hin- und Herlaufen hindurchkommen können. Petra steht vor einem solchen Szenario: Ein Grabmal kann nur durch einen langen Gang erreicht werden. Dieser Gang besteht aus Abschnitten, die lückenlos aufeinander folgen. In jedem Abschnitt ist in der Decke ein Steinquader eingelassen, der ihn blockieren kann. Am Anfang ist jeder Abschnitt durch seinen Quader blockiert.

Beim Erreichen des Ganges löst Petra einen Mechanismus aus, der die Quader bewegt. Petra beobachtet, dass sich jeder Quader periodisch bewegt mit einer ganzzahligen Anzahl von Minuten als Periodenlänge. Ein Quader mit Periode 5 Minuten blockiert seinen Abschnitt zunächst 5 Minuten, um ihn dann für 5 Minuten freizugeben und nach 5 Minuten erneut zu blockieren.

Petra kann sich nur in Abschnitten aufhalten, die nicht blockiert sind. Steht sie in einem Abschnitt, kann sie in einen benachbarten Abschnitt nur dann laufen, wenn **beide Abschnitte gleichzeitig nicht blockiert** sind.

Beispiel: Drei Quader mit den Perioden 5, 8 und 12 Minuten. Petra kann den Gang passieren, indem sie nach 8 Minuten in den zweiten Abschnitt läuft, dort 4 Minuten wartet und dann durch den dritten Abschnitt zum Grabmal läuft.

**Ziel:** Schreibe ein Programm, das Instruktionen für ein schnellstmögliches Erreichen des Grabmals ausgibt.

## Aufbau & Funktionsweise

### 🔍 Eingabe
Die Datei `Eingabe.txt` enthält die Anzahl der Abschnitte (erste Zeile) und darauf folgend die Perioden der Quader.

### ⚙️ Kernkomponenten

- `grabmal.py`: Enthält die Logik zur Lösung des Problems:
  - Periodenanalyse mit `_isopen`
  - Traversierung basierend auf einem Regelwerk (rechte Bewegung, Zeitfortschritt, Rücksprung, Startsprung)
  - Suche nach dem optimalen Pfad durch BFS-ähnliche Strategie mit einer `deque`
  
- Mehrpfadlogik: Berücksichtigt alternative Wege durch Speicherung potenzieller Pfade, falls eine direkte Fortsetzung blockiert ist.

### 🧠 Algorithmische Ideen

- **Zeit-Abschnitt-Kombinationen** werden als Zustände behandelt.
- **Zustände werden nur einmal besucht**, um Wiederholungen zu vermeiden.
- **Zeitsprünge** optimieren die Simulation, indem unnötige Prüfungen übersprungen werden.
- **Pfadverzweigungen** werden berücksichtigt, um alle möglichen Pfade zu durchlaufen.

## 📁 Dateien

| Datei                | Beschreibung                                      |
|---------------------|---------------------------------------------------|
| `grabmal.py`        | Hauptprogramm zur Berechnung der Lösung           |
| `Eingabe.txt`       | Beispielhafte Periodenliste                       |
| `loesung_grabmalX.txt` | Ausgaben mit verschiedenen Beispielperioden     |
| `Dokumentation_Grabmal.docx`          | Dokumentation und theoretische Herleitung         |

## ▶️ Nutzung

Für eine deutlich bessere Performance sollte das Skript mit **[PyPy3](https://www.pypy.org/)** ausgeführt werden:

```bash
pypy3 grabmal.py
