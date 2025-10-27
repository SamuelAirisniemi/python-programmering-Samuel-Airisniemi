morse_dict = {}
path = "Exercises/Week3/dictionary exercises/morse.txt"

with open(path, encoding="utf-8") as file:
    for line in file:
        if ":" in line:
            letter, kod = line.split(": ")
            morse_dict[letter.strip().upper()] = kod.strip()

def morse(message: str) -> str:
    return " ".join(morse_dict.get(ch.upper(), "") for ch in message if ch.strip())

print(morse("SOS"))
print(morse("POKEMON"))