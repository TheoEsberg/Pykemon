from pytmx import load_pygame
import pytmx, os, json
import Pokemons
path = os.path.dirname(__file__)
os.chdir(path)

class GameHandler:
    def __init__(self):
        self.pygame = None
        self.display = None
        self.player = None
        self.camera = None
        self.displayWidth = 0
        self.displayHeight = 0
        self.recentSteps = []
        self.pokemonFight = False
        self.battle = None

        #   Maps
        self.pallet_town = pytmx.load_pygame("maps/pallet-town.tmx", pixelalpha=True)
        self.home_downstairs = pytmx.load_pygame("maps/home-downstairs.tmx", pixelalpha=True)
        self.home_upstairs = pytmx.load_pygame("maps/home-upstairs.tmx", pixelalpha=True)
        self.professor_oak_home = pytmx.load_pygame("maps/professor-oak.tmx", pixelalpha=True)
        self.arkala_town = pytmx.load_pygame("maps/arkala-town.tmx", pixelalpha=True)

        self.currentMap = self.home_upstairs
        
        #   Pokemon list
        self.pokemons = []
        self.caughtPokemons = []
        self.activePokemon = None

        #   Active Menu's
        self.getStarterActive = False
        self.gotStarterPokemon = False

    def writeJSON(self, data, filename):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def LoadPokemons(self):
        with open("pokemons.json", "r") as f:
            data = json.load(f)
            for pokemon in data["pokemons"].values():
                name = pokemon["name"]
                type = pokemon["type"]
                hp = pokemon["hp"]
                attack = pokemon["attack"]
                defence = pokemon["defence"]
                speed = pokemon["speed"]
                moves = pokemon["moves"]
                level = pokemon["level"]
                xp = pokemon["xp"]
                self.pokemons.append(Pokemons.Pokemons(self, name, type, hp, attack, defence, speed, moves, level, xp))
                print(name, type, hp, attack, defence, speed, moves, level, xp)
                

        with open("caughtPokemons.json", "r") as f:
            data = json.load(f)
            if (data != {}):
                for pokemon in data["pokemons"].values():
                    name = pokemon["name"]
                    type = pokemon["type"]
                    hp = pokemon["hp"]
                    attack = pokemon["attack"]
                    defence = pokemon["defence"]
                    speed = pokemon["speed"]
                    moves = pokemon["moves"]
                    level = pokemon["level"]
                    xp = pokemon["xp"]
                    self.caughtPokemons.append(Pokemons.Pokemons(self, name, type, hp, attack, defence, speed, moves, level, xp))
                    self.activePokemon = self.caughtPokemons[0]
                    print("FÅNGADE PÅKÄMÅNS", self.caughtPokemons)



    def SaveToJson(self, jsonFile, listToSave):
        with open(jsonFile, "r") as f:
            data = json.load(f)
            data = {}
            temp = {}
            data["pokemons"] = temp 
            for i in range(len(listToSave)):
                y = {"name" : listToSave[i].name,
                     "type" : listToSave[i].type,
                     "hp" : listToSave[i].hp, 
                     "attack" : listToSave[i].attack,
                     "defence" : listToSave[i].defence,
                     "speed" : listToSave[i].speed,
                     "moves" : listToSave[i].moves,
                     "level" : listToSave[i].level,
                     "xp" : listToSave[i].xp
                     }
                temp[i] = y
        self.writeJSON(data, jsonFile)


    def GetNewPokemon(self, id, caughtID):
        with open("pokemons.json", "r") as f:
            readData = json.load(f)
            for pid, pokemon in readData["pokemons"].items():
                if (pid == str(id)):
                    print("This is running")
                    name = pokemon["name"]
                    type = pokemon["type"]
                    hp = pokemon["hp"]
                    attack = pokemon["attack"]
                    defence = pokemon["defence"]
                    speed = pokemon["speed"]
                    moves = pokemon["moves"]
                    level = pokemon["level"]
                    xp = pokemon["xp"]
                    self.caughtPokemons.append(Pokemons.Pokemons(self, name, type, hp, attack, defence, speed, moves, level, xp))
                    print("Caught Pokemons", self.caughtPokemons)





