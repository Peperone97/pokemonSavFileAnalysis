#!/usr/bin/python3

import sys

def main():
    if(len(sys.argv) != 2):
        print("must be 1 argument")
        exit(1)
    else:
        savFile = open(sys.argv[1], 'rb')
        content = savFile.read()

        numberOfPokemon = content[int(0x1A65)]
        print("Number of pokémon in the team: " + str(numberOfPokemon))
        i = 0
        while(i < numberOfPokemon):
            #print("Pokémon " + str(i) + ", national dex id: " + str(content[int(0x1A66)+i]))
            print("Pokémon " + str(i+1) + ", national dex id: " + str(content[int(0x1A6D)+(48*i)]))
            print("\tlivello: " + str(content[int(0x1A8c)+(48*i)]))
            i+=1

        savFile.close()

if __name__ == "__main__":
    main()