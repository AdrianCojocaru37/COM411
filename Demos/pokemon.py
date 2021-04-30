import csv,random



def save_pokes(pokes =[]):
  with open("pokemon.txt","w") as sv:
    for pokemon in pokes:
      sv.write(pokemon+ "\n")

def save_pokes_csv(pokes =[]):
  with open("pokemon.csv", "w") as sv:
    data_writer =csv.writer(sv,delimiter=",",quotechar='"')
    data_writer.writerow(pokes)

def load_pokemon():
  with open('pokemon.txt') as ld:
    return ld.read().split()


def load_pokemon_csv():
  with open("pokemon.csv") as ld:
    csv_reader =csv.reader(ld,quotechar="'")
    return list(csv_reader)[0]



def random_poke():
  with open("poke_database.csv") as pok:
    csv_reader=csv.reader(pok, quotechar="'")
    new_poke =list(csv_reader)[random.randint(0,1045)]
    return new_poke[2]








def run():
  #poke_list=["Pikach","Abra","Charizard","Bulbazaur", "Sceptile"]
  #save_pokes_csv(poke_list)
  #print(load_pokemon_csv())
  #print("\033[91mWe1come Pokemon Trainer!\033[0m")
  #while True:
    #print("\What would you like to do ?\1-View my pokemon\n2-Add new pokemon\n3-Add random Pokemn\n4-Exit")
    #opt =int(input())
    #if opt==1:
      #print(load_pokemon_csv())
    #elif opt ==2:
      #new_poke =input("enter name: ")
      #poke_list =load_pokemon_csv()
      #poke_list.append(new_poke)
      #save_pokes_csv(poke_list)
    elif opt==3:
      new_poke =random_poke()
      print(f"Well done! You have captured{new_poke}")
      poke_list=load_pokemon_csv()
      poke_list.append(new_poke)
      save_pokes_csv(poke_list)
    elif opt==4:
      break
    
      
  print(random_poke())




run()
