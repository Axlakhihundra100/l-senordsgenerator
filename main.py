import secrets
import string


def titel():
    print("----------------------------")
    print("-----lösenordsgenerator-----")
    print("-a--x--e--l-----------------")
    print("Skriv start för att starta generatorn")
    print("Skriv avsluta för att avsluta generatorn")
    # definierar titeln och skriver ut instruktioner

# (lösenordsskapare (secure) (hacker))
titel()
while True:
    user_input = input(": ")
    # skriver ut titeln och anger user_input
    if user_input == "avsluta":
        break
    # om användaren skriver "avsluta" stänger programmet
    elif user_input == "start":
        print("Vilket sorts lösenord vill du skapa?")
        print("Alfabet och nummer, Skriv an.")
        print("Alfabet, nummer och specialtecken, skriv ans")
        # om användaren skriver "start" visas fler instruktioner
        val = input(": ")
        if val == "an":
            print("Hur långt vill du att ditt lösenord ska vara?")
            antal = int(input(": "))
            alphabet_numbers = string.ascii_letters + string.digits
            # alphabet_numbers är tecken och nummer^
            lösenord = ''.join(secrets.choice(alphabet_numbers) for i in range(antal))
            # lösenordet består av random alphabet_numbers och är antal långt
            print(lösenord)
            titel()
            # skriver lösenordet och visar titeln
        elif val == "ans":
            print("Hur långt vill du att ditt lösenord ska vara?")
            antal = int(input(": "))
            alphabet_numbers_spec = string.ascii_letters + string.digits + string.punctuation
            # alphabet_numbers_spec är bokstäver nummer och tecken
            lösenord = ''.join(secrets.choice(alphabet_numbers_spec) for i in range(antal))
            # samma som tidigare
            print(lösenord)
            titel()
        else:
            print("Du skrev fel mannen betee dig o skriv rätt.")
            break
            # om du skrev någonting annat än an/ans i tidigare "val" får du ett felmedelande
