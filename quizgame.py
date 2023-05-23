print("Welkom op mijn computer quize!")

playing = input("Wil je spelen? type ja of nee: ")

if playing.lower() != "ja":
    quit()

print("Okey! Laten we spelen :)")
score = 0

answer = input("1. Wanneer is de programmeertaal HTML ontwikkeld?: ")
if answer.lower() == "1991":
    print('Juist!')
    score += 1
else:
    print("Fout, Begin opnieuw!")

answer = input("2. Wanneer is de programmeertaal Python ontwikkeld?: ")
if answer.lower() == "1989":
    print('Klopt!')
    score += 1
else:
    print("Fout, Begin opnieuw!")

answer = input("3. Wanneer is het World Wide Web (WWW) uitgevonden?: ")
if answer.lower() == "1989":
    print('Goed bezig!')
    score += 1
else:
    print("Fout, Begin opnieuw!")
    
answer = input("4. Wanneer is de programmeertaal Java ontwikkeld?: ")
if answer.lower() == "1995":
    print('Juist')
    score += 1
else:
    print("Fout, Begin opnieuw!")

answer = input("5. Wanneer is de eerste versie van Windows gelanceerd?: ")
if answer.lower() == "1985":
    print('Je gaat lekker')
    score += 1
else:
    print("Fout, Begin opnieuw!")

answer = input("6. Wanneer werd het eerste e-mailbericht verzonden?: ")
if answer.lower() == "1971":
    print('Goed bezig!')
    score += 1
else:
    print("Fout, Begin opnieuw!")

print("Je hebt " + str(score) + " vragen goed!")
print("Je hebt " + str((score / 6) * 100) + "%.")