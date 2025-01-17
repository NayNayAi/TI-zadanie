imie = input("Wpisz imie: ")
print("Witaj", imie, "w tej przygodzie!")
import random
mylist= ["Twoja przygoda zaczyna sie przyjemnie, slonce oswieca twa droge", "Twoja przygoda zaczyna sie z hukiem, zastala cie burza", "Twoja przygoda zaczyna sie ponuro, dopadla cie ulewa"]
print(random.choice(mylist))
answer = input(
    "Jestes na rozdrozu, mozesz isc w prawo lub lewo. Gdzie chcesz sie udac? (lewo/prawo) ").lower()

if answer == "lewo":
    answer = input(
        "Docierasz do rzeki, mozesz przejsc mostem lub isc dalej bokiem rzeki. Czy przekroczysz most?(tak/nie) ")

    if answer == "nie":
        print("Idziesz wzdluz rzeki i napotykasz bandytow na swojej drodze, zostajesz ograbowany i przegrywasz.")
    elif answer == "tak":
        print("Przechodzac przez most poslizgnales sie i wpadles do rzeki, rzeka byla pelna krokodyli, zostajesz zjedzony, przegrywasz.")
    else:
        print("Rozmyslasz sie i zawracasz do domu nigdy nie realizujac marzen o byciu poszukiwaczem przygod")

elif answer == "prawo":
    answer = input(
        "Docierasz do magicznego zrodelka, mozesz sie w nim zanurzyc lub isc dalej, czy sie zanurzysz? (tak/nie) ")

    if answer == "tak":
        print("Zanurzajac sie czujesz jak twoje cialo staje sie strasznie ociezale, probujesz sie podniesc, ale nie masz sily, nie masz innego wyjscia jak zatonac, przegrywasz.")
    elif answer == "nie":
        answer = input(
            "Idziesz dalej spotykajac na swojej drodze tajemniczego staruszka. Czy z nim porozmawiasz (tak/nie)? ")

        if answer == "tak":
            print("Rozmawiasz ze staruszkiem, okazal sie wielkim czarodziejem, ktory obdarowuje cie magiczna rozdzka!")

        elif answer == "nie":
            print("Ignorujesz staruszka, ktoremu to sie nie spodobalo. Okazal sie wielkim czarodziejem i za pomoca swojej mocy wygnal cie z kraju, przegrywasz.")
        else:
            print("Nagle zasypiasz, po czym budzisz sie w swoim domu nie pamietajac nic ze swojej przygody, czy byla w ogole prawdziwa?")
    else:
        print("Probujesz ominac zrodelko, ale wpadasz prosto do srodka, przegrywasz.")

else:
    print("Wrociles do domu zanim przygoda sie zaczela")

print("Dziekuje za wziecie udzialu w przygodzie", imie)