visuel = ""
mot = "bonjour"
caracteres_trouves= ['o', 'n']

for char in mot:
    if char in caracteres_trouves:
        visuel += char
    else:
        visuel += "_"

print(visuel)

dict = {"win":0, "loss": 0}
dict["win"] += 1
for k, v in dict.items():
    print(f"{k}: {v}")