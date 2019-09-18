# Python-Skripte werden einfach von oben nach unten ausgefuehrt, es ist keine explizite main notwendig (aber moeglich, sehen wir spaeter)
# Variablen kriegen keine Typendeklaration:
x = 5
x += 3
y = 2*x
print(y)

# Grundlegende Operatoren funktionieren wie erwartet:
# Modulo:
print(y%3)

# Ganzzahl-Division (floor):
print(y//3)

# Potenzierung:
print(y**4)

# Alle Operationen lassen sich mit Direktzuweisung kombinieren:
y %= 3
print(y)

# Vorsicht: strong typing -> Java-artige Verkettung geht nicht!
print("y="+y)

# Stattdessen muss man explizit konvertieren:
print("y="+str(y))
