# Empfehlung (auch zum Danebenlegen bei den Übungsaufgaben): Python Cheat Sheet
# https://www.dataquest.io/blog/python-cheat-sheet/

###=== Umgang mit Variablen allgemein ===###

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

# LÜCKENAUFGABEN zu dir()

# Methoden mit __ sind "magic"-Methoden, nicht für direkte Verwendung gedacht

# Neben den klassischen integer, float, string haben wir Listen:
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

# LÜCKENAUFGABE zu Listen

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

# LÜCKENAUFGABEN zu Dictionaries

# Ein set ist eine Menge und kann jedes Element nur ein Mal enthalten:

myset = set()
myset.add(15)
myset.add("blub")
print(myset)
myset.add(14)
myset.add(15)
print(myset)

###=== Umgang mit Strings ===###
# Python wird häufig zur Stringverarbeitung (Tabellenkonversion etc.) verwendet,
# daher ein paar mehr Details zu Strings.

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

# Strings haben eine häufig verwendete, nette Methode, um Tupel und Arrays zu verketten:

toprint = ["Das", "sind", "Woerter"]
print(" ".join(toprint))
print("--!--".join(toprint))

# LÜCKENAUFGABEN zu Strings

# Zum Formatieren von strings existiert eine Spezifikationssprache:
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


###=== Kontrollstrukturen ===###

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
print("Das ist auch toll")

# While tut das, was while halt so tut:
y=10
while y > 5:
    print(y)
    y -= 1

# LÜCKENAUFGABEN zu while, if, else

# for ist zum iterieren da:
letters = ["a", "b", "c"]
for letter in letters:
    if letter == "a":
        print("AAAAAAAAA")
    print(letter)

# Man kann über alles iterieren, was iterable ist (auch strings sind z.B. iterable):
print(range(2,7))
for x in range(2,7):
    print(x)

for x in range(0,10,3):
    print(x)

for key in mydict:
    print(str(key) + ": " + str(mydict[key]))

for item in mydict.items():
    print(item)

# LÜCKENAUFGABEN zu for

# AUFGABEN:
# 1.1) Finden Sie 2 Methoden, um von einem String alle Zeichen
#   zeilenweise auszugeben. Z.B. word = "test", Ergebnis:
# t
# e
# s
# t
# 1.2) Geben Sie von den Buchstaben des Wortes jeden nur ein Mal aus. Z.B.
#   word = "test". Tips: Sie können eine dafür besonders geeigtene Datenstruktur verwenden, oder die .count()-Methode
#   von String. Ergebnis:
# t
# e
# s
# 1.3) Drehen Sie die Zeichen in einem String um, z.B. word = "Zeichenkette", nach
#   Ausführung ist word == "etteknehcieZ"
# 1.4*) Bauen Sie aus einem String (z.B. "test") ein Array aller Rotationen
#   dieses String (-> ["test", "estt", "stte", "estt"])
# 1.5*) Erweitern Sie 1.4 indem aus einem Array von Strings eine dictionary
#   generiert wird, die zu jedem der Strings (key) die Liste aller Rotationen
#   wie in 1.4* beschrieben ablegt (values).
# 1.6*) Erweitern Sie 1.4*, indem Sie eine um den ersten Buchstaben zentrierte
#   Ausgabe erstellen. Z.B. word = "Test", Ausgabe:
#     Test
#    tTes
#   stTe
#  estT

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

# LÜCKENAUFGABEN List Comprehensions

# AUFGABEN:
# 2.1) Lösen Sie 1.1 mittels list comprehension (am besten auch mit 2 Methoden)
# 2.2) Lösen Sie 1.2 nochmals unter Mitverwendung einer list comprehension
# 2.3) Zählen Sie unter Verwendung einer list comprehension, wie häufig in einem
#   String das Zeichen "t" vorkommt.
# 2.4*) Schreiben Sie eine list comprehension, die alle ungeraden Zahlen bis 100 
#   ausgibt
# 2.5*) Schreiben Sie eine list comprehension, die alle Primzahlen bis 100 ausgibt.
#   Tipp: Sie können list comprehensions verschachteln

# Funktionsdefinitionen können überall im Code vorkommen (sollten es aber nicht ;) ):
def add(x, y):
    result = x+y
    return result

print(add(3,7))

# Vorsicht: Funktionen müssen evaluiert worden sein, bevor sie aufgerufen werden (Live-Beispiel)

# Namen in Funktionsdeklaration können auch in Aufruf verwendet werden (named parameters):

print(add(y=10, x=5))

# Default-Parameter sind möglich:
def somefunction(x, y, defaultparam=False):
    result = x - y
    if defaultparam:
        result = abs(result)
    return result

# Was kommt jeweils raus?
print(somefunction(10, 15))
print(somefunction(10, 15, True))

# Besonderheit von Python: Funktionen, die iterierbar sind. yield returnt zwar,
# der Stack der Funktion bleibt aber beim nächsten Aufruf erhalten:

def generatorfunction(maxnum):
    currentnum = 0
    while currentnum < maxnum:
        yield currentnum
        currentnum += 2

# Was wird ausgegeben?
for x in generatorfunction(10):
    print(x)
    
# Eine Funktion, die mittels yield Werte zurückgibt und somit iterierbar ist,
# wird als Generator bezeichnet.

# Generatoren können schrittweise abgefragt werden:

nums = generatorfunction(1000)
print(next(nums))
print(next(nums))

# Das ist extrem nützlich, um z.B. über Werte einer rekursiv definierten Folge
# zu laufen ohne sie komplett im Speicher zu halten oder sehr große Datensätze
# zu verarbeiten. 

# Exkurs: Dateiverarbeitung
# Datei öffnen (2. Argument ist mode, häufig: r, w, a. b ist binary, z.B. "rb"):
infile = open("LICENSE.md", "r")
data = infile.read()
infile.close()

# Ups... willkommen in der Hölle :(
# Keine Ahnung, was das encoding ist? replace oder ignore:
infile = open("LICENSE.md", "r", errors="replace")
data = infile.read()
infile.close()
print(data[:100])

# Bekannt? Angeben mit encoding.
infile = open("LICENSE.md", "r", encoding="UTF-8")
data = infile.read()
infile.close()
print(data[:100])

# Auch eine Text-Datei ist iterierbar:
infile = open("LICENSE.md", "r", encoding="UTF-8")
lines = infile.read().split("\n")
infile.close()
for line in lines:
    print(line)

# Wo könnte hier das Problem sein?
# Alternative:

for line in open("LICENSE.md", "r", encoding="UTF-8"):
    print(line)

# AUFGABEN:
# 3.1) Schreiben Sie einen Generator, der eine Datei nimmt und mittels yield 
#   iterierbar zeilenweise (jede Zeile ohne das "\n" am Ende) zurückgibt. 
# Beipsiel für Verwendung:
# for line in linewise("LICENSE.md"):
#     print(line)
# 3.2*) Schreiben Sie einen Generator, der Primzahlen liefert
# 3.3*) Schreiben Sie einen Generator, der die Fibonacci-Folge liefert

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
Fruit.get_description()

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

class Banana(Fruit):
    def __init__(self, cost, stock):
        super().__init__("banana", cost, stock)
        
    def get_description(self):
        return "I am a banana! I cost " + " ".join(super().get_description().split(" ")[2:])

banana = Banana(10, 50)
print(banana)

# Abfrage, was was ist:

isinstance(apple, Fruit)
isinstance(apple, object)
isinstance(apple, Banana)
isinstance(banana, Fruit)
isinstance(banana, Banana)

# Es geht auch Mehrfachvererbung (im Gegensatz zu Java, wo nur mehrere Interfaces
# implementiert werden können):

class Coloredthing:
    def __init__(self, color):
        self.color = color
    
    def describe_color(self):
        return "it is " + self.color
    
class Coloredfruit(Fruit, Coloredthing):
    def __init__(self, name, price, stock, color):
        # Warum kriegt __init__ hier explizit self?
        Fruit.__init__(self, name, price, stock)
        Coloredthing.__init__(self, color)
        
    def get_description(self):
        # Wieso Fruit.get_description aber self.describe_color?
        return Fruit.get_description(self) + " Also, " + self.describe_color()
    
fruit = Coloredfruit("apple", 5, 300, "red")
print(fruit)

# Sinnvolleres Beispiel: Uhr-Klasse, Kalender-Klasse existieren zum Verwalten von Uhrzeit
# und Datum. Neue Klasse zum Darstellen eines Widgets mit Uhrzeit und Datum erbt von beiden.

# Vanilla-Python kann leider nicht allzu viel. Dafür gibt es aber eine Menge an Module.
# Standard-Library: https://docs.python.org/3/py-modindex.html
# pip: https://pypi.org
# Beispiel: OS

import os
files = os.listdir(".")
print("\n".join([x for x in files if x.endswith(".txt")]))

from os import getcwd
print(getcwd())

# Das ist auch super, um eigene Module zu schreiben. Import evaluiert das gesamte Modul.
import mymodules
mymodules.dostuff("Exercise")

# Vorsicht beim interaktiven Testen: Module werden nur ein Mal geladen. Abhilfe:
from importlib import reload
reload(mymodules)

# AUFGABEN:
# 4.1) Lagern Sie den Generator aus 3.1 in eine eigene Klasse in einem neuen Modul aus. Beispiel für Verwendung:
# from readmodule import Linewisereader
# lr = Linewisereader("README.md", encoding="UTF-8")
# for line in lr.lines():
#     print(line)
# 4.2*) Erweitern Sie Linewisereader um zwei Methoden:
# reopen(): Öffnet die Datei nochmal neu, so dass lines() wieder von Vorne iteriert
# set_encoding(): Setzt das encoding neu und macht ein reopen()
# Tip: Denken Sie an das singleton-Pattern.


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

# ZUSATZAUFGABEN:
# X.1*) Schreiben Sie eine Funktion, die - gegeben eine Zahl von 0 bis
#   999,999,999,999 - diese auf Deutsch oder Englisch (Sprache=Funktionsargument)
#   als Text ausgibt.