# PROJEKT: Transformacje współrzędnych
Program oferuje funkcje transformacji współrzędnych między różnymi układami.
### Z jakich transformacji możesz skorzystać?
- XYZ (geocentryczne) --> BLH (elipsoidalne)
- BLH (elipsoidalne) --> XYZ (geocentryczne)
- XYZ (geocentryczne) --> NEUp (topocentryczne)
- BL (elipsoidalne) --> PL2000 (prostokątne lokalne)
- BL (elipsoidalne) --> PL1992 (prostokątne lokalne)
### Jakie elipsoidy sądostępne w programie?
- WGS84
- GRS80
- Elipsoida Krasowskiego
### Jakie wymagania musi spełniać twój komputer?
- Oprogramowanie Windows 10
- Program Python 3.9 lub 3.10
- Biblioteki konieczne do instalacji: Math, Numpy, Argparse
### Jak korzystać z programu?
W Wierszu poleceń należy wykonywać polecania programu.
- -> plik ->
Należy podać nazwę pliku wraz z rozszerzeniem, jeśli znajduje się w tym samym folderze, lub ścieżkę do pliku, jeśli jest ulokowany poza folderem.
- -> transformacja -> 
Należy podać nazwę transformacji współrzędnych na której chcesz pracować.
- -> odniesienie -> 
Należy wybrać model elipsoidy do którego zostaną odniesione transformacje.
### Przykład wywołania programu:
Na konsoli należy wpisać:
```sh
script_git.py
-plik testXYZ2BLH.txt
-transformacja XYZ2BLH
-odniesienie GRS80
```
Program odpowiada:
```sh
Raport został zapisany w folderze.
Aby zakończyć wpisz STOP. Aby korzystać dalej napisz inne słowo.
```
Po wpisaniu 'stop' program zakończy pracę.
```sh
Program zakończył pracę.
```
Aby kontynuować pracę z programem należy wpisać dowolne inne słowo.
### Tranformacja XYZ2BLH
Plik z danymi:
```sh
3853110.000 11425020.000 4863030.000
```
Raport:
```sh
   B[°]       L[°]       H[m] 
 49.99923   20.29622    388.846
```
Program odpowiada:
```sh
Podaj lokalizację pliku txt: C:\Users\Dell\Documents\GitHub\informatyka\wyniki_XYZ2BLH.txt
Nazwa transformacji:XYZ2BLH
Model elipsoidy:grs80
Raport został zapisany w folderze.
Aby zakończyć wpisz STOP. Aby korzystać dalej napisz inne słowo.: stop
Program zakończył pracę.
```
### Informacje o błędach.
Program miewa trudności z transformacją obszernych danych. Zaleca się transformowanie zestawów danych z osobna tj. po jedenj linijce.
