[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/0XtS1uQO)
# Domácí úkol č. 3
> **Upravujte pouze soubor `assignment_3_1.py` a v něm pouze nahraďte `...` podle zadání!**

Vašim úkolem je vytvořit oblíbenou hru Kámen, nůžky, papír (rock, paper, scissors).

Tato hra je pro dva hráče, ale v tomto případě hrajete Vy proti počítači. Hra je založena na zvolení jednoho ze tří
symbolů každým hráčem. Hráči ukáží ve stejný okamžik na prstech svou volbu. Vy zadáváte volbu z klávesnice, počítači
se generuje náhodně číslo, resp. index `0`, `1` nebo `2`, který reprezentuje jeden z povolených symbolů uložených 
v konstantě `GAME_SYMBOLS`. 

Před odehráním hry je ještě nutné vstupy z klávesnice předzpracovat. Nejprve je nutné změnit první písmeno ve jménu
hráče na velké písmeno a u tahu hráče změnit všechna písmena na malá. V neposlední řadě je potřeb ověřit, že vstup
zadaný uživatelem je mezi povolenými herními symboly.

Pak už přichází na řadu samotná hra. Vítězem hry se stává hráč, který zvolil symbol s vyšší hodnotou. 
Je přesně definováno, který symbol má větší hodnotu:

 * Kámen tupí nůžky – vyhrává kámen (kámen > nůžky).
 * Papír balí kámen – vyhrává papír (papír > kámen).
 * Nůžky stříhají papír – vyhrávají nůžky (nůžky > papír).
 * Remíza (oba symboly jsou stejné) – nikdo nevyhrává.

Doplňte algoritmus tak, aby určil vítěze podle těchto pravidel. V souboru `assignment_3_1.py` jsou nachystané dvojice
řádků kódu, které je nutné vložit do jednotlivých větví programu, aby algoritmus správně fungoval a bylo ho možné ověřit
pomocí automatických testů.
