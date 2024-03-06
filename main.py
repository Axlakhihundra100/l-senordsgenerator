import secrets
import string


def titel():
    print("----------------------------")
    print("-----lösenordsgenerator-----")
    print("-a--x--e--l-----------------")
    print("Skriv start för att starta generatorn")
    print("Skriv avsluta för att avsluta generatorn")


# lösenordsskapare (secure) (hacker)
titel()
while True:
    user_input = input(": ")

    if user_input == "avsluta":
        break

    elif user_input == "start":
        print("Vilket sorts lösenord vill du skapa?")
        print("Alfabet och nummer, Skriv an.")
        print("Alfabet, nummer och specialtecken, skriv ans")

        val = input(": ")
        if val == "an":
            print("Hur långt vill du att ditt lösenord ska vara?")
            antal = int(input(": "))
            alphabet_numbers = string.ascii_letters + string.digits
            lösenord = ''.join(secrets.choice(alphabet_numbers) for i in range(antal))
            print(lösenord)
            titel()
        elif val == "ans":
            print("Hur långt vill du att ditt lösenord ska vara?")
            antal = int(input(": "))
            alphabet_numbers_spec = string.ascii_letters + string.digits + string.punctuation
            lösenord = ''.join(secrets.choice(alphabet_numbers_spec) for i in range(antal))
            print(lösenord)
            titel()
        else:
            print("Du skrev fel mannen betee dig o skriv rätt.")
            break
