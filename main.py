#!/usr/bin/python3

import sys

def trainerId(content):
    #in pokemon crystal the id is in the memory index 0x1A73-0x1A74
    a = content[int(0x1A73)]*16**2
    b = content[int(0x1A74)]
    return a+b

def totalPkmXp(content, stage):
    xp = content[int(0x1A75) +(48*stage)]*16**4
    xp += content[int(0x1A76) +(48*stage)]*16**2
    xp += content[int(0x1A77) +(48*stage)]
    return xp

def main():
    if(len(sys.argv) != 2):
        print("must be 1 argument")
        exit(1)
    else:
        savFile = open(sys.argv[1], 'rb')
        content = savFile.read()

        numberOfPokemon = content[int(0x1A65)]
        if(numberOfPokemon != 0):
            print("Trainer id: " + str(trainerId(content)))
            print("Number of pokémon in the team: " + str(numberOfPokemon))
            for i in range(0, numberOfPokemon):
                #print("Pokémon " + str(i) + ", national dex id: " + str(content[int(0x1A66)+i]))
                print("Pokémon " + str(i+1) + ", national dex id: " + str(content[int(0x1A6D)+(48*i)]))
                print("\tlivello: " + str(content[int(0x1A8C)+(48*i)]))
                print("\ttotal xp: " + str(totalPkmXp(content, i)))
                print("\tstats: ")
                print("\t\tatk: " + str(content[int(0x1A94)+(48*i)]) + " def: " + str(content[int(0x1A96)+(48*i)]))
                print("\t\tsatk: " + str(content[int(0x1A9A)+(48*i)]) + " sdef: " + str(content[int(0x1A9C)+(48*i)]))
                print("\t\tspeed: " + str(content[int(0x1A98)+(48*i)]))
        else:
            print("No pokémon in this save")

        savFile.close()

if __name__ == "__main__":
    main()