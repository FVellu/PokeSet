def getPokemons(log, whatPlayer):
    p1 = []
    p2 = []
    for x in str(log).split("\n"):
        if x.startswith("|switch|p1") or x.startswith("|drag|p1"):
            if "," in x.split("|")[3]:
                p1.append(x.split("|")[3].split(",")[0])
            else:
                p1.append(x.split("|")[3])
        if x.startswith("|switch|p2") or x.startswith("|drag|p2"):
            if "," in x.split("|")[3]:
                p2.append(x.split("|")[3].split(",")[0])
            else:
                p2.append(x.split("|")[3])
    if whatPlayer == 1:
        return list(dict.fromkeys(p1))
    elif whatPlayer == 2:
        return list(dict.fromkeys(p2))
    else:
        return list(dict.fromkeys(p1)), list(dict.fromkeys(p2))
def getPokemonMovesP1(log, pokemon):
    currentMon = "no pokemon"
    moves = []
    for x in str(log).split("\n"):
        if x.startswith("|switch|p1") or x.startswith("|drag|p1"):
            if "," in x.split("|")[3]:
                currentMon = x.split("|")[3].split(",")[0]
            else:
                currentMon = x.split("|")[3]
        if x.startswith("|move|p1"):
            if str(currentMon) == str(pokemon):
                if "," in x.split("|")[3]:
                    moves.append(x.split("|")[3].split(",")[0])
                else:
                    moves.append(x.split("|")[3])
    return list(dict.fromkeys(moves))

def getPokemonMovesP2(log, pokemon):
    currentMon = "no pokemon"
    moves = []
    for x in str(log).split("\n"):
        if x.startswith("|switch|p2") or x.startswith("|drag|p2"):
            if "," in x.split("|")[3]:
                currentMon = x.split("|")[3].split(",")[0]
            else:
                currentMon = x.split("|")[3]
        if x.startswith("|move|p2"):
            if str(currentMon) == str(pokemon):
                if "," in x.split("|")[3]:
                    moves.append(x.split("|")[3].split(",")[0])
                else:
                    moves.append(x.split("|")[3])
    return list(dict.fromkeys(moves))



#for x in str(replayJson['log']).split("\n"):
#    print(x)

#print(getPokemonMovesP1(replayJson['log'], "Skarmory"))
#print(getPokemons(replayJson['log']))

# 0 = player 1, 1 = player 2

#for pokemon in getPokemons(replayJson['log'], 1):
#    if len(getPokemonMovesP1(replayJson['log'] ,pokemon)) == 4:
#for pokemon in getPokemons(replayJson['log'], 2):
#    if len(getPokemonMovesP2(replayJson['log'] ,pokemon)) == 4:
#        writeFile(pokemon, 2, replayJson['log'])