import LogDataExtractor as lde
import requests
import yaml
import json
import time


while True:
    try:
        replayList = requests.get("https://replay.pokemonshowdown.com/search.json?format=gen8ou").text
        replayList = json.loads(replayList)
        for gameData in replayList:
            matchesFileR = open("matches", "r")
            if gameData['id'] in matchesFileR.read():
                pass
            else:
                print("Found new game ID: " + gameData['id'])
                matchesFileW = open("matches", "a")
                replay = requests.get("https://replay.pokemonshowdown.com/" + gameData['id'] + ".json").text
                replayJson = json.loads(replay)
                r = open("dataset.json", "r")
                data = json.loads(r.read())
                r.close()

                for pokemon in lde.getPokemons(replayJson['log'], 1):
                    if(len(lde.getPokemonMovesP1(replayJson['log'], pokemon)) == 4):
                        print(pokemon)
                        if pokemon not in data:
                            data[pokemon] = {}
                        for move in lde.getPokemonMovesP1(replayJson['log'], pokemon):
                            if move not in data[pokemon]:
                                data[pokemon].update({move: 1})
                            else:
                                data[pokemon].update({move: data[pokemon][move] + 1})

                for pokemon in lde.getPokemons(replayJson['log'], 2):
                    if(len(lde.getPokemonMovesP2(replayJson['log'], pokemon)) == 4):
                        print(pokemon)
                        if pokemon not in data:
                            data[pokemon] = {}
                        for move in lde.getPokemonMovesP2(replayJson['log'], pokemon):
                            if move not in data[pokemon]:
                                data[pokemon].update({move: 1})
                            else:
                                data[pokemon].update({move: data[pokemon][move] + 1})

                w = open("dataset.json", "w")
                w.write(json.dumps(data))
                w.close()
                matchesFileW.write(gameData['id'] + "\n")
                matchesFileW.close()
            matchesFileR.close()
    except:
        print("JSONDecodeError, continuing")
    time.sleep(10)
