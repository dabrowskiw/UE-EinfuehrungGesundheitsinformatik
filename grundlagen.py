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

# Jede Variable in Python ist ein Objekt:
print(x.bit_length())

# Nützliche Funktion: dir() zeigt alle Methoden und Attribute eines Objektes an:
dir(x)
dir("   test")
print("   test".upper())
print("   test".strip())

# Methoden mit __ sind "magic"-Methoden, nicht für direkte Verwendung gedacht

# Zum formatieren von strings existiert eine Spezifikationssprache:
# {} sind placeholder für Variablen
print("Der Wert von y: {} minus den Wert von x: {} ist: {}".format(x, y, x-y))

# Mit {} können auch Positionen in der Argumentenliste angegeben werden:
print("y: {1}, x: {0}".format(x, y)) 

# Positionen können wiederholt werden:
print("{0}{1}{0}".format("abra", "cad")) 

# Zahlenformate können definiert werden:
print("723 in binary: {0:b} and hex: {0:X}".format(723)) 

# Damit kann man übrigens schön die Ergebnisse binärer Operationen anschauen:
print("1: {:b}, 1<<2: {:b}, 60: {:b}, ~60: {:b} (dezimal: {}), 13: {:b}, 60&13: {:b}, 60|13: {:b} etc...".format(1, 1<<2, 60, ~60, ~60, 13, 60&13, 60|13)) 
# Frage: Kann jemand erklären, wieso ~60==-61

# Man kann links, rechts oder mittig alignen und sich das Fuellzeichen aussuchen:
print("y 10-stellig rechtsbündig: {0:>10}, linksbündig: {0:<10}, zentriert: {0:^10} und rechtsbündig mit 0: {0:0>10}".format(y))


# String-delimiter können ", ', oder (für multiline) """ sein:
print('Das ist z.B. nuetzlich um " nicht escapen zu muessen')

dat="""Oder um
mehrere Zeilen Text
einfach einzugeben"""
print(dat)

# Es existieren viele convenience-Funktionen für strings, z.B.:

dat2 = dat.replace("\n", " ")
print(dat2)
print(dat2.split(" "))

# (das geht alles auch mit regexp, Modul re, aber das führt zu weit)

# Split führt uns zu Datentypen. Neben den klassischen integer, float, string haben wir Listen:
x = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
print(x)

# Vorsicht: Durch die dynamische Typisierung geht das x=[1,2,3] oben: x ist jetzt kein integer mehr, sondern eine Liste!
# Adressierung von Listen wie gewohnt:
print(x[0])
print(dat2.split(" ")[3])

# Man kann mit Listen viele lustige Dinge tun, z.B.:
# slicen
print(x[2:5])
print(x[5:]) 
print(x[:5])

# von hinten adressieren
print(x[-3])

# Verketten, verschachteln und Datentypen darin mischen
print(x + ["a", 2, ["b", "blub"]])

# Elemente entfernen
x.pop(3) # Das ist der Index
print(x)
x.remove(5) # Das ist der Wert des Elements (es wird das erste Vorkommen gelöscht)
print(x)

# Performance-Hinweis: Listen sind als voralloziierte pointer-Arrays implementiert, die bei Erreichen
# der Kapazität wachsen (-> volle Kopie). 
# pop last, get sind O(1), append ist amortisiert O(1), aber pop nach Index, remove sind O(n)!

# Als abgespeckte Version existieren noch Tupel:
tup = (1, 3, 4)
print(tup)

# Viel mehr als Zugriff geht damit nicht, tuples sind immutable (erlauben 
# aber Optimierungen, sollten also wenn möglich statt Listen eingesetzt werden)

# Dann gibt es noch Dictionaries (aus Java bekannt z.B. als HashMap):
mydict = {"key": "value", "a": 5, "Zeugs": "sehr sinnvoll", 7: "sieben"}
print(mydict)
print(mydict["Zeugs"])
mydict["Zeugs"] = "weniger sinnvoll"
print(mydict["Zeugs"])

# Ueberpruefung, ob ein key drin ist:
print("Zeugs" in mydict)
print("neuerkey" in mydict)
mydict["neuerkey"] = "neuerwert"
print("neuerkey" in mydict)
print(mydict["neuerkey"])

# Übrigens auch aus einem Tupel von Tupeln initialisierbar:
mydict2 = dict((("7", "sieben"), ("acht", 8)))
print(mydict2)

# Kontrollstrukturen verhalten sich wie gewohnt.
# Ungewohnt:
#  * Beginn eines Blocks wird mit : am Ende der Kontrollstuktur gekennzeichnet
#  * Einrückung muss stimmen (und in gesamten Code konsistent sein, mal 3 Leerzeichen und mal 4 geht nicht).
y = 12
if y > 10:
    y -= 3
elif y <= 10:
    y += 10
else:
    print("Geht nicht.")
print(y)

# Funktioniert nicht wegen fehlender Einrückung:
if y > 10:
print("y immer noch groesser 10")

# While tut das, was while halt so tut:
while y > 5:
    print(y)
    y -= 1

# for ist zum iterieren da:
letters = ["a", "b", "c"]
for letter in letters:
    print(letter)

# Man kann über alles iterieren, was iterable ist:
print(range(2,7))
for x in range(0,10,3):
    print(x)

for key in mydict:
    print(str(key) + ": " + str(mydict[key]))

for item in mydict.items():
    print(item)

# Direktes Entpacken der Tupel:
for key, value in mydict.items():
    print(str(key) + ": " + str(value))

# Geht übrigens mit >2 Elementen und überall wo Tupel/Listen zurückkommen:
a, b, c = (1, 2, 5)
print("{}, {}, {}".format(a, b, c))

# Eine Python-spezifische Form von Schleifen ist die list comprehension. Sie
# definiert Operationen, die auf definierte Elemente einer iterable angewendet werden
values = range(0, 20)
even = [x for x in values if x%2 == 0]
print(even)
stringdict = dict([(str(x), x) for x in values])
print(stringdict["12"])

# Funktionsdefinitionen können überall im Code vorkommen (sollten es aber nicht ;) ):
def add(x, y):
    result = x+y
    return result

print(add(3,7))

# Vorsicht: Funktionen müssen evaluiert worden sein, bevor sie aufgerufen werden (Live-Beispiel)

# Namen in Funktionsdeklaration können auch in Aufruf verwendet werden:

print(add(y=10, x=5))

# Default-Parameter sind möglich:
def sub(x, y, makepositive=False):
    result = x - y
    if makepositive:
        result = abs(result)
    return result

print(sub(10, 15))
print(sub(10, 15, True))

# Funktionen sind first-class citizens:
def dostuff(what, x, y):
    print(what(x, y))

function = sub
dostuff(function, 10, 5)
dostuff(add, 10, 5)

# Tatsächliche Anwendung findet das z.B. beim Sortieren:

tosort = [("apples", 5, 280), ("oranges", 12, 100), ("bananas", 5.9, 1200)]

def getprice(fruit):
    return fruit[1]

def getstock(fruit):
    return fruit[2]

tosort.sort(key=getprice)
print(tosort)
tosort.sort(key=getstock)
print(tosort)

# Lambda-Expressions erlauben die anonyme Deklaration einfacher Funktionen:

# Sort descending by price
tosort.sort(key=lambda x: -1*getprice(x)) # Alternativ tosort.sort(key=getprice, reverse=True)
print(tosort)

# tosort ist hier aber blöd aufgebaut, schöner wäre das mit einer Klasse.
# Besonderheiten in Python:
#  * Constructor heißt immer __init__
#  * Erstes Argument einer Methode ist immer self (in Java wäre das this),
#    außer bei statischen Methoden.
#  * Keine protected-Attribute (per Konvention _attribut), keine private-Attribute
#    (per Konvention __attribut, aber immer noch als _klasse__attribut zugreifbar)
class Fruit:
    def __init__(self, name, price, stock):
        self.price = price
        self.stock = stock
        self.name = name
        self._krams = "Krams"
        self.__privatkrams = "Meins!"
        
    def get_description(self):
        return self.name + " costs " + str(self.price) + ", we have "+ str(self.stock) + " in stock."
        
    def print_fruit():
        print("Fruit!")
        
#    def __str__(self):
#        return self.get_description()
#
#    def __repr__(self):
#        return str(self)
  
# Methodenaufrufe:      
Fruit.print_fruit()
# Geht natürlich nicht: 
Fruit.print_description()

tosort = [Fruit("apple", 5, 280), Fruit("orange", 12, 100), Fruit("banana", 5.9, 1200)]
tosort.sort(key=lambda x: x.price)
print(tosort)
# Das sieht blöd aus. Magic-Methode __str__ wird zur Konversion in String verwendet,
# __repr__ für Repräsentation in automatischen Ausgaben. 
# Oben __str__ und __repr__ einkommentieren, nochmal evaluieren, dann sieht man den Unterschied.


# "Private" Attribute:
apple = Fruit("apples", 5, 280)
print(apple._krams)
apple._krams = "Anderer Krams!"
print(apple._krams)

# Private ist "ein bisschen mehr private":
print(apple.__privatekrams)
# Aber:
print(apple._Fruit__privatkrams)
apple._Fruit__privatkrams = "Nix meins."
print(apple._Fruit__privatkrams)

# Vererbung geht mit Klammern:

# Randnotiz zu Performance jetzt wo wir ein paar Grundlagen kennn: strings sind immutable!
# Entsprechend ist das hier extrem langsam:
values = range(0, 1000000)
from datetime import datetime
starttime = datetime.utcnow()
toprint = ""
for value in values:
    toprint += str(value) # O(m+n)!
    toprint += ", "
timediff = (datetime.utcnow() - starttime)
print(1000000*timediff.seconds + timediff.microseconds)

# Aber Listen sind O(1) erweiterbar, also:
starttime = datetime.utcnow()
toprint_arr = []
for value in values:
    toprint_arr += [str(value)] # O(1)
    toprint_arr += [", "]
toprint = "".join(toprint_arr)
timediff = (datetime.utcnow() - starttime)
print(1000000*timediff.seconds + timediff.microseconds)

