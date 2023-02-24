## Python / PyTest gyakorló feladat
2023-02-24

**Cél:** Az eddig megismert Python programozási lehetőségek gyakorlása egy konkrét alkalmazás, és a hozzá tartozó
tesztek elkészítése közben.

**Elkészítendő alkalmazás:** Command Line Shop

A gyakorló óra során a vásárlói funkciókat szeretnénk megvalósítani.  
A Tulajdonosi funkciókat szorgalmiként, akár egyénileg, akár közös munka során tudnátok majd megcsinálni.

---

### Alkalmazás specifikáció

Az alkalmazás parancssorból üzemeltethető, választható menüpontok ill. az azokhoz tartozó funkciók segítségével. 
Lehetőséget biztosít a bolti áruk kezelésére ill. vásárlásra szerepkör szerint.

Szerepkörök: Tulajdonos, Vásárló  
Kapcsolódó igény: menüpont segítségével lehessen váltani a szerepkörök között.

Tervezett funkciók:

1. Tulajdonos
   1. Meglévő termékek listázása
   2. Termék törlése
   3. Új termék felvétele
   4. Termék adatainak módosítása
   5. Szerepkör váltás
   6. Kilépés
   ```text
    Egy termék a következő tulajdonságokkal rendelkezik: 
      - Azonosító   (int, egyedi, növekményes)
      - Név         (str)
      - Ár          (float)
   ```
   
2. Vásárlói funkciók
   1. Meglévő termékek listázása ( = Tulajdonos 1. funkció)
   2. Termék keresése szövegrészlet alapján (név mező tartalmazza-e)
   3. Termékek kosárba helyezése ID alapján - darabszám is legyen megadható!
   4. Kosár listázása
   5. Fizetés: számla lekérése
   6. Szerepkör váltás
   7. Kilépés

---

### Automatizált teszt specifikáció

PyTest segítségével ellenőrizzük a következő eseteket:

1. Vásárlói funkciók
   1. Termék keresésekor minden keresési találat megjelenik
   2. A számla végösszege helyesen kerül kiszámításra