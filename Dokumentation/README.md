Inhaltsverzeichnis
2	Was ist GNSS?	
3	Vorstellung der zu vergleichenden Empfänger	
4	Vorbereitungen für den Vergleich der Empfänger	
4.1	Aufbau des NMEA Protokolls	
4.2	Dilution of Precision DOP	
4.3	Differential Global Positioning System DGPS	
4.4	Durchzuführende Messungen	
4.4.1	Langzeitmessung	
4.4.2	Geschwindigkeitsmessung	
4.5	Messaufbau	
5	Durchführung, Auswertung und Interpretation der Messungen	
5.1	Durchführung	
5.1.1	Langzeitmessung	
5.1.2	Geschwindigkeitsmessung	
5.2	Annahmen die wir für die Auswertung treffen werden	
5.2.1	Langzeitmessung	
5.2.2	Geschwindigkeitsmessung	
5.3	Auswertung	
5.3.1	Auswertung Langzeitmessung	
5.3.2	Interpretation Langzeitmessung	
5.3.3	Auswertung Geschwindigkeitsmessung	
5.3.4	Interpretation Geschwindigkeitsmessung	
6	Fazit	
7	Literaturverzeichnis	
8	Abbildungsverzeichnis	

# Was ist GNSS?
GNSS steht für Globales Navigationssatellitensystem (engl. Global Navigation Satellite System); durch den Empfang von Signalen verschiedener Navigationssatelliten dient es zur Positionsbestimmung und Navigation auf der Erde.

GNSS ist ein Sammelbegriff für die verschiedenen globalen Satellitensysteme:


* NAVSTAR GPS (Global Positioning System) von den Vereinigten Staaten von Amerika
* GLONASS (Globales Satellitennavigationssystem) von der Russischen Föderation
* Galileo von der Europäischen Union
* Beidou von der Volksrepublik China
		
Das GNSS System besteht aus drei Segmenten:

* **Satelliten im Weltraum**
 Die Satelliten umkreisen in regelmäßigen Intervallen die Erde und senden Signale. Jeder Satellit ist mit einer Uhr, einem Mikroprozessor, einem Sender und einer      Antenne ausgestattet.

* **Kontrollstationen** 
 Die Bahnkoordinaten der Satelliten werden von der Erde aus bestimmt.

* **Nutzer / Empfänger**
 Empfängt Signale von Satelliten und verarbeitet diese.

Ein GNSS Empfänger ist ein Gerät, dass aus den Satellitensignalen die eigene Position ermittelt.
Zur Positionsbestimmung muss der Empfänger die Signale von mindestens vier Satelliten gleichzeitig empfangen. Die Satelliten teilen über Funk ihre genaue Position und Uhrzeit mit. Im Empfänger werden dann die vier Signallaufzeiten (von den Satelliten zum Empfänger) errechnet. Aus diesen Daten wird dann die aktuelle Position inklusive der Höhe und der Uhrzeit des Empfängers ermittelt. 
Es werden also mindestens vier Laufzeiten von den Satelliten zur Empfangsantenne gemessen.
Jede dieser Empfangslaufzeiten steht für eine Pseudoentfernung und definiert eine Kugelfläche um den dazugehörigen Satelliten. Drei der vier Kugelflächen bilden einen Schnittpunkt am Standort des Empfängers, die anderen Schnittpunkte der Kugelflächen sind zu vernachlässigen.
Der vierte Satellit ermittelt die Abweichung zwischen den Uhren der Satelliten und der des Empfängers, um die Pseudoentfernungen in die tatsächlichen Entfernungen umzurechnen. 




Abbildung 1

# Vorstellung der zu vergleichenden Empfänger
Folgend die wesentlichen Unterschiede/Gemeinsamkeiten der zu vergleichenden Empfänger auf Grundlage der Datenblätter.

|Merkmal|uBlox Max-M8-FW31|Zhongkewei ATGM336H-5N31| 
|---|:---:|:---:|
|Preis|	                                                      9,06 $|	                             2,94 $|
|Gleichzeitiger Empfang von GNSS Systemen (max.)|	              3|	                                    2|
|Untestützte GNSS Systeme|	                         GPS/BEIDOU/GLONASS/GALILEO|	GPS/BEIDOU/GLONASS/Galileo|
|Qualitätsindex|	                                      Differential GPS fix|	                      GPS fix|
|Höhe (max.)|	                                                50.000m|	                              18.000m|
|Geschwindigkeit (max.)|	                                    500 m/s|	                              515 m/s|
|Beschleunigung (max.)|	                                        4 g|	                                  4 g|
|Positionsgenauigkeit|	                                     2,5 - 4 m|	                              2,5 m|

# Vorbereitungen für den Vergleich der Empfänger
## Aufbau des NMEA Protokolls
NMEA 0183 ist ein Kommunikationsprotokoll welches für die Kommunikation zwischen GNSS-Empfängern und Endgeräten dient. Dieses Protokoll beinhaltet 70 unterschiedliche 
NMEA-Datensätze.
Die erste Version, die allerdings nicht öffentlich war sondern Militärzwecken diente, wurde im März 1983 freigegeben. Die aktuellste Version ist die 2012 erschienene Version 4.10.  
Die Übertragung des NMEA Protokolls beginnt mit dem Start-Bit (logische Null) darauf folgen acht Daten-Bits, zum Schluss folgt ein Stopp-Bit (logische Null).
 
Abbildung 2







Das NMEA Protokoll besteht aus drei Hauptbestandteilen, der Präambel, der Nachricht und der Checksumme. Folgendes Beispiel zeigt einen GGA-Datensatz im NMEA Protokoll.

 
Abbildung 3
Die Präambel enthält Informationen über den Start der Nachricht, das verwendete Satellitensystem und den empfangenen Datensatz.
	GP steht für GPS 
	GL steht für GLONASS
	GA steht für GALILEO
	BD steht für Beidou
	GN steht für einen Verbund aus unterschiedlichen Systemen

Die Datensätze geben an wie die darauffolgende Nachricht zu interpretieren ist; hierbei sind fünf häufig verwendeten Protokolle:
	GGA (Global Positioning System Fix Data)
	VTG (Track made good and Ground speed)
	GSA (GPS, DOP and active Satellites)
	GSV (Satellites in view)
	RMC (Recorded Minimum Navigation Information)

Die Nachricht selbst enthält je nach Datensatz unterschiedliche Informationen, auf diese werden wir später im Bezug auf unsere Messungen genauer eingehen.
Die Checksumme am Ende der Nachricht wird mit einem „*“ als Begrenzung begonnen. 

## Dilution of Precision DOP
Satellitennavigationssysteme bestimmen ihre Position über die Entfernung zu mehreren Satelliten durch eine Signallaufzeitmessung. Die Ungenauigkeit dieser Positionsbestimmung gibt der DOP-Wert an, dieser ist abhängig von den Positionen der genutzten Satelliten zueinander. 
Günstige Winkel zwischen Satellit A, Satellit B und dem Standort des Empfängers liegen bei             90°. Sind diese Winkel sehr klein oder um 180°, schneiden sich die Entfernungskreise bzw. -Kugeln unter flachen Winkeln und verringern somit die Messgenauigkeit. Der Kehrwert der Fläche bzw. des Volumens, das die Einheitsvektoren in Richtung der Satelliten aufspannen, bestimmt die Größe des DOP-Wertes. 
DOP ist folglich ein Maß dafür, wie gut die Konstellation der Satelliten überhaupt für eine Messung geeignet ist.
|	| |
|---|---|
|0-2,5|	Bestmögliche Anordnung| 
|2,5-8|	Noch akzeptabel|
|>8|	Keine Auswertung mehr möglich| 

## Differential Global Positioning System DGPS
DGPS bezeichnet ein Verfahren, dass durch ausstrahlen von Korrekturdaten über Bodenstationen die Genauigkeit der GNSS-Systeme steigern soll.

## Durchzuführende Messungen
Für den Vergleich der GNSS-Empfänger sollen zwei maßgebliche Messungen durchgeführt werden; zum einen eine stationäre Langzeitmessung am GPS-Referenzpunkt in Köln und zum anderen eine Geschwindigkeitsmessung unter möglichst konstanten Rahmenbedingungen (Geschwindigkeit, Höhendifferenz, Störeinflüsse). 

### Langzeitmessung
Um die Genauigkeit der beiden Empfänger hinsichtlich ihrer Positionsbestimmung und Höhe zu ermitteln soll eine ca. dreistündige Messung am GPS-Referenzpunkt in Köln durchgeführt werden. Hierbei zeichnen wir die Datensätze „GGA“, „GSA“ und „GSV“ auf. Die Koordinaten des Referenzpunktes wurden mit einem hochpräzisen GPS-Empfänger bestimmt und beziehen sich auf die Mitte der Bronzeplatte.
 
Abbildung 4

Der GGA-Datensatz (GPS Fix Data) enthält Werte um einen guten Gesamtvergleich zwischen den beiden Empfängern treffen zu können. Er umfasst Informationen bezüglich Zeit, geographischer Länge und Breite, Qualität des Systems, Anzahl der genutzten Satelliten, Höhe und weitere. Der GGA Datensatz ist wie folgt aufgebaut:
$--GGA,hhmmss.ss,llll.ll,a,yyyyy.yy,a,x,xx,x.x,x.x,M,x.x,M,x.x,xxxx*hh

| | |
|-|-|
|hhmmss.ss|	Universeller Time Code (UTC)|
|llll.ll|	Breitengrad|
|a|	Breitenrichtung (N=Nord, S=Süd)|
|yyyyy.yy|	Längengrad|
|a|	Längsrichtung (E=Ost, W=West)|
|x|	GPS-Qualität (0= kein GPS, 1=GPS, 2=DGPS)|
|xx|	Anzahl der empfangenen Satelliten| 
|x.x|	Horizontal Dilution of Precision (HDOP)|
|x.x|	Höhenangabe der Antenne (Geoid-Höhe)|
|M|	Einheit der Höhenangabe (M=Meter)|
|x.x|	Höhendifferenz zwischen Ellipsoid und Geoid|
|M|	Einheit der Höhendifferenz (M=Meter)|
|x.x|	Alter der DGPS-Daten|
|xxxx|	Identifizierung der DGPS Referenzmessstelle|
|hh|	Checksumme|

Ein eventueller Zusammenhang mit der HDOP soll untersucht werden. Des Weiteren soll die Menge der empfangenen Satelliten verglichen werden.

### Geschwindigkeitsmessung
Bei der Geschwindigkeitsmessung sollen Messungen unter konstanter Geschwindigkeit durchgeführt werden und mit einer Strecke-Zeitmessung verglichen werden. Dazu werden die Datensätze „VTG“, „GGA“, „GSA“ und „GSV“ aufgezeichnet. Der VTG-Datensatz gibt Aufschluss über die Geschwindigkeit, diese wird im Protokoll direkt in Kilometer pro Stunden ausgegeben.  Für die Strecke-Zeitmessung werden die Kilometertafeln am Rande der Autobahn gezählt und die Zeit mit einer Stoppuhr gemessen. Anhand der gemessenen Zeit und zurückgelegten Strecke kann eine Durchschnittsgeschwindigkeit zzgl. einem Fehler berechnet werden.


## Messaufbau
Zum Einlesen des NMEA Protokolls haben wir ein Python Programm geschrieben und uns dafür an bereits verfügbaren Bibliotheken bedient.

Für einen einheitlichen Vergleich der beiden Empfänger wurde eine Platine mit den beiden Empfängern bestückt; somit nutzten sie beide die gleiche Antenne und andere für den Betrieb notwendige Bauteile. Über serielle Schnittstellen konnten die Daten der Empfänger ausgelesen werden. Die Stromversorgung der Platine ist zum einen extern, über einen separaten Anschluss möglich, zum anderen kann die Stromversorgung der Platine auch über eine der seriellen Schnittstelen erfolgen.
 
Abbildung 5


Messaufbau:
 
Abbildung 6
Messaufbau am Rhein:
 
Abbildung 7
# Durchführung, Auswertung und Interpretation der Messungen
## Durchführung
### Langzeitmessung
Für die Langzeitmessung wurde die Antenne der beiden Empfänger mittig auf der Bronze Platte des Kölner GPS-Referenzpunktes platziert. Über eine Zeit von ca. drei Stunden wurden die dafür ausgewählten Datensätze geloggt.



### Geschwindigkeitsmessung
Bei der Geschwindigkeitsmessung wurde die Antenne der beiden Empfänger auf dem Autodach montiert. Über eine Strecke von ca. 5 Kilometern wurden auf einem möglichst geraden und ebenen Autobahnabschnitt die dafür ausgewählten Datensätze geloggt. Bei der Geschwindigkeitsmessung wurden Messungen mit ca. 80km/h und ca. 110km/h durchgeführt.

## Annahmen die wir für die Auswertung treffen werden
### Langzeitmessung
Ziel der Langzeitmessung ist es festzustellen, ob beide GNSS-Empfänger gravierende/ sichtbare Abweichungen bei der Positionsbestimmung in Längen- und/oder Breitengraden, sowie der Höhe, haben.
Die Erde ist ein Ellipsoid und kommt damit einer Kugel sehr nahe. Also können beliebige Punkte auf der Erde durch geografische Koordinaten beschrieben werden. Dafür wird die Erde wie folgt aufgeteilt:

Längengrade 180° West bis 180° Ost, verlaufend zwischen Nord- und Südpol und
Breitengrade 90° Nord bis 90° Süd verlaufend um den Äquator.
 
Abbildung 8
Die einzelnen Längen- und Breitengrade werden noch einmal unterteilt dargestellt, ein Grad wird in 60 Minuten und eine Minute wird weiter in 60 Sekunden unterteilt.
Es gibt unterschiedliche Möglichkeiten Koordinaten darzustellen:
 
Abbildung 9
Der Abstand zwischen den Breitengraden ist konstant bei 111,3 km, der Abstand zwischen den Längengraden variiert jedoch und ist abhängig davon, auf welchem Breitengrad man sich befindet.

Nach folgender Formel lässt sich der Abstand zweier Längengrade berechnen:
dL=111,3 km*cos⁡(Breitengrad)

Um nun die Entfernung zwischen zwei Punkten zu berechnen nutzt man den Satz des Pythagoras. Da der kürzeste Weg zwischen zwei Punkten allerdings durch den Erdball und nicht um ihn herum verläuft muss man zusätzlich die Erdkrümmung berücksichtigen. Für diesen Fall (über weite Entfernungen) muss man die Loxodrome (in der Grafik rot) umrechnen um die sogenannten Orthodrome (in Grafik blau) zu erhalten; die Loxodrome sind immer ein Teilstück des Großkreises (Orthodrome).

 
Abbildung 10
Bei der Langzeitmessung am Kölner GPS-Referenzpunkt sollten sich aufgrund der geringen Abweichungen, max. 2,5 - 4m laut Datenblättern im Vergleich zum Erdradius (6.371.000m),   keine signifikanten Abweichungen aufgrund der Erdkrümmung ergeben, daher wird die Erdkrümmung im Folgenden vernachlässigt.
Das NMEA-Protokoll gibt die Koordinaten in Grad-Dezimalminuten aus, da aber die folgenden Rechnungen auf Dezimalgrad basieren ist eine vorherige Umrechnung in dieses Format nötig .
Hier ein Beispiel aus einer Messung:
$GNGGA,142102.00,5056.46904,N,00658.11390,E,1,08,1.34,67.7,M,46.7,M,,*73
Dieser Auszug wird wie folgt interpretiert:
5056.46904 N	Ddmm.mmmmm	N 50° 56,46904
00658.11390 E	Dddmm.mmmmm	E 06° 58,11390
Die Umrechnung von Grad-Dezimalminuten in Dezimalgrad erfolgt folgendermaßen:
50° 56,46904=(56,46904/60)+50°=50,94115067°
06° 58,11390=(58,11390/60)+06°=6,968565°



Der Abstand entlang der Längengrade lässt sich mit folgender Formel berechnen:
dL=111,3*cos⁡((Breite 1+Breite 2)/2*π/180)*(Länge1-Länge2)
Der Abstand entlang der Breitengrade lässt sich mit folgender Formel berechnen:
dB=111,3*(Breite 1-Breite 2)
Die Distanz zwischen den beiden Punkten lässt sich mit folgender Formel berechnen:
Distanz= √(〖dL〗^2+〖dB〗^2 )

### Geschwindigkeitsmessung
Für den Vergleich der Geschwindigkeitsmessungen der beiden Empfänger wird eine Strecke-Zeitmessung durchgeführt. Dafür wird folgende Formeln verwendet:
v=∆x/∆t
Eine Näherung für den Fehler wird wie folgt angenommen:
∆v=v*(∆x/x+∆t/t)
Daraus ergibt sich die Geschwindigkeit: (v±∆v) wobei gilt:
 v_max=v+∆v 
 v_min=v-∆v













## Auswertung
### Auswertung Langzeitmessung
In den nachfolgenden Abbildungen ist die Abweichung der Messdaten in Länge und Breite aufgetragen. Abbildung 11 zeigt die gemessenen Abweichungen der beiden Empfänger bezogen auf den Referenzpunkt. 
 
Abbildung 11











In Abbildung 12 ist der Schwerpunkt (blaues „X“) der ausgewerteten Daten des uBlox Empfängers inklusive der Standardabweichung (kleiner Kreis um „X“) dargestellt.
 
Abbildung 12
In Abbildung 13 ist das Histogramm der ausgewerteten Abweichungen des uBlox Empfängers zum Referenzpunkt in dx und dy Richtung mit entsprechenden Häufigkeiten aufgetragen.
 
Abbildung 13
In Abbildung 14 ist der Schwerpunkt (rotes „X“) der ausgewerteten Daten des Zhongkewei Empfängers inklusive der Standardabweichung (kleiner Kreis um „X“) zu sehen.
 
Abbildung 14
In Abbildung 15 ist das Histogramm der ausgewerteten Abweichungen des Zhongkewei Empfängers zum Referenzpunkt in dx und dy Richtung mit entsprechenden Häufigkeiten aufgetragen.
 
Abbildung 15
Beim uBlox Empfänger lässt sich beobachten, dass es zwar Abweichungen zum Referenzpunkt gibt, diese jedoch nicht signifikant von den Vorgaben aus dem Datenblatt abweichen (2,5 - 4m). Zusätzlich lässt sich anhand des Schwerpunktes (Abbildung 12) eine leichte Abweichung in nördliche Richtung feststellen. Der Referenzpunkt liegt beim uBlox Empfänger außerhalb der Standardabweichung vom Schwerpunkt.
Der Zhongkewei Empfänger weist ein wesentlich größeres Streubild der Messwerte auf, hierbei ist kein eindeutiger Trend zu erkennen. Der Referenzpunkt liegt innerhalb der Standardabweichung vom Schwerpunkt des Zhongkewei Empfängers.
In den nachfolgenden Abbildungen ist der aus x- und y-Abweichungen kombinierte Abstand der Messwerte zum GPS-Referenzpunkt aufgetragen. Abbildung 16 zeigt die gesamte Abweichung der beiden Empfänger bezogen auf den Referenzpunkt.
 
Abbildung 16









In der nachfolgende Abbildung 17 ist der kombinierte Abstand der Messwerte des uBlox Empfängers zum GPS-Referenzpunkt, inklusive des Mittelwertes (blau) der Standardabweichung (rot) aufgetragen.
 
Abbildung 17
In der nachfolgende Abbildung 18 ist der kombinierte Abstand der Messwerte des Zhongkewei Empfängers zum GPS-Referenzpunkt, inklusive des Mittelwertes (gelb) der Standardabweichung (rot) aufgetragen
 
Abbildung 18
In den Abbildungen 17 und 18 wird deutlich, dass die Standardabweichung des uBlox Empfängers (1,55m) wesentlich geringer ist als die des Zhongkewei Empfängers (3,97m). Es lässt sich feststellen, dass der Zhongkewei Empfänger im Schnitt einen größeren Abstand zum Referenzpunkt besitzt.
In Abbildung 19 sind die Höhen der beiden Empfänger, sowie deren Mittelwerte, im Verhältnis zur Höhe des Kölner Referenzpunkt zu sehen.
 
Abbildung 19
In der nachfolgende Abbildung 20 ist die Höhe des uBlox Empfängers zum GPS-Referenzpunkt (rot), inklusive des Mittelwertes (blau) und der Standardabweichung (schwarz) aufgetragen. 

 
Abbildung 20


In der nachfolgende Abbildung 21 ist die Höhe des Zhongkewei Empfängers zum GPS-Referenzpunkt (rot), inklusive des Mittelwertes (gelb) und der Standardabweichung (schwarz) aufgetragen.
 
Abbildung 21
Hierbei lässt sich feststellen, dass die vom uBlox gemessene Höhe im Mittel etwa 1,52m über der Referenzhöhe 55,38m liegt. Die Standardabweichung des uBlox Empfängers ist 3,10m.
Auffällig ist das der Zhongkewei Empfänger im Mittel etwa 54,61m über der Referenzhöhe liegt und die Standardabweichung 14,49m ist.
Des Weiteren wurde die Anzahl der empfangen Satelliten verglichen, es waren bei beiden Empfängern keine Auffälligkeiten festzustellen. Die Betrachtung der HDOP (Qualitätsmerkmal) ergab ebenfalls keine Auffälligkeiten, da die Werte sich konstant um 1 bewegt haben und somit im optimalen Bereich lagen. Daher konnte kein Zusammenhang zwischen HDOP und den Abweichungen der Positionsbestimmung festgestellt werden.

### Interpretation Langzeitmessung
Folgend wird darauf eingegangen, wie sich entsprechende Differenzen zwischen den beiden Empfängern ergeben könnten. Dabei handelt es sich lediglich um Vermutungen die aufgrund der Komplexität des gesamten Themas, der immensen Masse an auszuwertenden Daten und der sehr kurzen Projektdauer nicht weiter belegt werden konnten.
Die deutlich größere Streuung in der Positionsbestimmung zwischen Zhongkewei und uBlox Empfänger könnte zum einen daran liegen, dass der Zhongkewei Empfänger nur 2 GNSS-Systeme gleichzeitig verarbeiten kann und zum anderen kein DGPS empfängt.
Eine weitere Auffälligkeit bei der Positionsbestimmung sind die linienartigen, zeitlich aufeinander auftretenden Ausreißer beim Zhongkewei Empfänger. 
Diese aufeinanderfolgenden Ausreißer können ein Hinweis darauf sein, dass der Zhongkewei Empfänger mit Mittelwerten der letzten Messwerte arbeitet. Die dichte Wolke des uBlox Empfängers weist keine solcher zusammenhängenden Ausreißer auf also ist anzunehmen, dass der uBlox Empfänger jeden einzelnen Messwert auswertet.
Die deutliche Abweichung in der Höhe des Zhongkewei Empfängers könnte durch eine Fehlinterpretation seinerseits im GGA Protokoll entstehen; der uBlox Empfänger stellt die Geodiale- und Ellipsoidiale Höhe an den entsprechenden Stellen im GGA Protokoll separat voneinander dar, so ist es im Protokoll auch vorgesehen.
Im direkten Vergleich stellt der Zhongkewei Empfänger den geodialen Wert deutlich größer dar, der ellipsoidiale Wert ist dauerhaft „0“. Auffällig ist, dass die Summe aus geodialer und ellipsoidialer Höhen des uBlox Empfängers annähernd dem geodialen Wert des Zhongkewei Empfängers entspricht.
 
Abbildung 22
Der maximale Messbereich der Höhe beträgt beim uBlox Empfänger 50.000m und beim Zhongkewei 18.000m, da wir unsere Empfänger nicht im Grenzbereich betreiben sollte sich dieser Unterschied nicht auf unsere Messung auswirken.
Anhand der Histogramme lässt sich erkennen, dass beim uBlox Empfänger die Häufigkeit einer Abweichung breiter um „0“ gestreut ist als beim Zhongkewei Empfänger. 
Anhand der Histogramme lässt sich erkennen, dass die ausgewerteten Daten des uBlox Empfängers annähernd der Erwartung der Normalverteilung entspricht, der Erwartungswert für dy jedoch nicht bei „0“ zentriert ist. Auffällig ist, dass der Zhongkewei-Empfänger deutlich mehr Werte über der erwarteten Normalverteilung nahe „0“ liefert. Daher lässt sich kaum feststellen welcher der beiden Empfänger tatsächlich eine genauere Positionsbestimmung zulässt.


### Auswertung Geschwindigkeitsmessung
Im Folgenden Diagrammen ist die aus den Empfängern berechnete Geschwindigkeit und die von uns über die Strecke und die Zeit ermittelte Geschwindigkeit zu sehen. Hier mit 80 km/h laut Tempomat.
 
Abbildung 23
Eine zweite Messung mit 110 km/h laut Tempomat:
 
Abbildung 24
Hier lässt sich beobachten, dass sowohl der Zhongkewei als auch der uBlox Empfänger nicht wesentlich von der Strecke-Zeitmessung abweichen und sogar im Toleranzbereich des geschätzten Fehlers liegen. Lediglich beim uBlox Empfänger gibt es einige wenige Ausreißer.



### Interpretation Geschwindigkeitsmessung
Folgend wird darauf eingegangen, wie sich entsprechende Differenzen zwischen den beiden Empfängern ergeben könnten. Dabei handelt es sich lediglich um Vermutungen die aufgrund der Komplexität des gesamten Themas und der immensen Masse an auszuwertenden Daten nicht weiter belegt werden konnten.
Die Abweichung beider Empfänger am Beginn der 110km/h Messung könnte am nachregeln des Tempomaten liegen.
Es lässt sich eine Korrelation zwischen den Ausreißern der beiden Empfänger beobachten, diese sind beim uBlox Empfänger deutlich ausgeprägter als beim Zhongkewei. Hierbei lässt sich unsere Vermutung, dass der Zhongkewei Empfänger mit Mittelwerten der letzten Messungen arbeitet bestärken. Die wesentlich größeren Ausreißer des uBlox Empfängers deuten darauf hin, dass dieser jeden Messwert für sich interpretiert.
Um unsere Behauptung über die konstante Höhenabweichung von ca. 45m noch einmal zu stützen, sind im Folgenden die Höhenverläufe der beiden Empfänger während der Geschwindigkeitsmessungen zu sehen.
 
Abbildung 25
Auch hier lässt sich die konstante Höhenabweichung zwischen den beiden Empfängern feststellen und unterstützt unsere Behauptung mit dem falsch interpretierten GGA-Datensatz des Zhongkewei Empfänger (siehe Interpretation Langzeitmessung).
Interessant ist, dass sich über diesen kurzen Zeitverlauf die Empfänger bis auf das „Höhen-Offset“ ein sehr ähnliches Verhalten aufweisen und keine Ausreißer auftreten.




# Fazit
Ein direkter Vergleich der beiden Empfänger ist sehr schwierig, da beide Empfänger sich in ihren technischen Eigenschaften unterscheiden; der Zhongkewei Empfänger unterstützt lediglich normales GPS und der uBlox Empfänger korrigiertes GPS (DGPS). In Abmessungen und Gewicht unterscheiden sich die beiden Empfänger nicht signifikant voneinander. Ein weiterer Unterschied ist die maximale Höhe welche die Empfänger unterstützen; uBlox 50.000m und Zhongkewei 18.000m.
In der Langzeitmessung hat sich gezeigt, dass die Positionsbestimmung beider Empfänger funktioniert; unter Berücksichtigung der Standardabweichung kommen beide Empfänger zu einem ähnlichen Ergebnis.
In der Geschwindigkeitsmessung hat sich gezeigt, dass die Fehler der beiden Empfänger korrelieren und der uBlox Empfänger trotz seiner größeren Ausreißer sehr ähnliche Messungen liefert.

Im gesamten lässt sich keine Aussage darüber treffen, ob einer der beiden Empfänger besser ist als der andere da sie sich beide sehr ähnlich sind. Es ist wichtig festzuhalten, dass die Auswahl eines Empfängers vom entsprechenden Einsatzbereich sehr stark abhängig ist und somit individuell entschieden werden muss, welche Eigenschaften für die entsprechende Anwendung gefordert ist.
Aufgrund der enormen Datenmengen und der Komplexität des Themas ist dieses Projekt nur ein Anriss dessen, was zu den Empfängern in Erfahrung gebracht werden könnte. Vor allem die interne Übersetzung der Rohdaten in NMEA-Datensätze müsste weiter untersucht werden; dafür wären weitere, umfangreiche Messreihen unter Einbezug der Rohdaten erforderlich.










# Literaturverzeichnis

Globales Navigationssatellitensystem (2020),https://de.wikipedia.org/wiki/Globales_
Navigationssatellitensystem, Abruf am 09.06.2020
Prof. Dr. techn. Alfred Mischke: Skript Teil 8: GNSS, https://www.ruhr-uni-bochum.de/geodaesie/download/Skript%20Teil%208%20-%20GNSS.pdf, Abruf am 11.06.2020
uBlox Datenblatt: MAX-M8 series, https://www.u-blox.com/sites/default/files/MAX-M8-FW3_DataSheet_(UBX-15031506).pdf, Abruf am 03.06.2020
Zhongkewei Datenblatt: ATGM336H-5N,https://datasheet.lcsc.com/szlcsc/ 1810261521_ZHONGKEWEI-ATGM336H-5N31_C90770.pdf, Abruf am 03.06.2020
NMEA 0183 (2019), https://de.wikipedia.org/wiki/NMEA_0183, Abruf am 15.06.2020
Aufbau des NMEA-Protokolls, http://www.zogg-jm.ch/Dateien/aufbau_des_nmea.pdf, Abruf am 17.06.2020
Dilution of Precision (2019), https://de.wikipedia.org/wiki/Dilution_of_Precision, Abruf am 25.06.2020
NMEA 0183 Datensätze, http://www.nmea.de/nmea0183datensaetze.html, Abruf am 10.07.2020
Martin Kompf: Entfernungsberechnung, https://www.kompf.de/gps/distcalc.html, Abruf am 10.07.2020 
# Abbildungsverzeichnis
Abbildung 1	https://www.dlg.org/fileadmin/_processed_/1/6/csm_1_Laufzeitmessung_a19590f9d1.jpg
Abbildung 2	http://www.zogg-jm.ch/Dateien/aufbau_des_nmea.pdf
Abbildung 3	Eigene Darstellung
Abbildung 4	https://www.geocaching.com/geocache/GC7B70Q_gps-referenzpunkt-koln?guid=a2ac0301-4926-4594-9925-fcecac8e164c
Abbildung 5	Eigene Darstellung
Abbildung 6	Eigene Darstellung
Abbildung 7	Eigene Darstellung
Abbildung 8	https://de.wikipedia.org/wiki/Geographische_Koordinaten#/media/Datei:FedStats_Lat_long.png
Abbildung 9	https://de.wikipedia.org/wiki/Geographische_Koordinaten
Abbildung 10	https://de.wikipedia.org/wiki/Orthodrome#/media/Datei:Rhumbs_and_great_circles_on_Mercator.svg
Abbildung 11	Eigene Darstellung
Abbildung 12	Eigene Darstellung
Abbildung 13	Eigene Darstellung
Abbildung 14	Eigene Darstellung
Abbildung 15	Eigene Darstellung
Abbildung 16	Eigene Darstellung
Abbildung 17	Eigene Darstellung
Abbildung 18	Eigene Darstellung
Abbildung 19	Eigene Darstellung
Abbildung 20	Eigene Darstellung
Abbildung 21	Eigene Darstellung
Abbildung 22	Eigene Darstellung
Abbildung 23	Eigene Darstellung
Abbildung 24	Eigene Darstellung
Abbildung 25	Eigene Darstellung


