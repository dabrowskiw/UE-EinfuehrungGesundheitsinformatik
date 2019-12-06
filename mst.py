# * Klasse SequenceType erstellen, die einen Namen und eine Liste von Alleltypen
#   im Constructor nimmt
# * interesting_profiles einlesen und in eine dictionary von SequenceTypes einlesen
#   (Schlüssel: Name des Sequenztyps, Value: SequenceType)
# * Klasse Bacterium erstellen, die die Accession und den Sequenztyp hält
# * ausbruchsdaten.txt einlesen, aus jeder Zeile die Accession und den ST parsen
#   und ein entsprechendes Array von Bacterium erstellen
# * Methode count_differences(self, other) implementieren, die die Anzahl an
#   Alleltypen ausgibt, in denen sich self.alleletypes von other.alleletypes
#   unterscheidet
# * Distanzmatrix erstellen (diverse Optionen, z.B. die SequenceType selber die
#   Distanzen zu allen anderen SequenceTypes merken lassen). Vorsicht: Geschwindikeit
#   beachten! Wie lässt es sich beschleunigen? Können z.B. bestimmte Berechnungen
#   weggelassen werden?
