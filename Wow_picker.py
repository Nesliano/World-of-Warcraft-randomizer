import random
import os

########################################################################################################################
# FILE PATHS
########################################################################################################################

# Factions
factions_file_path = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Factions.txt"

# Races
alliance_file_path = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Races/Alliance_Races.txt"
horde_file_path = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Races/Horde_Races.txt"

# Alliance classes
human_file_path = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Alliance/Human.txt"
dwarf_file_path = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Alliance/Dwarf.txt"
nightelf_file_path = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Alliance/Night Elf.txt"
gnome_file_path = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Alliance/Gnome.txt"
draenei_file_path = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Alliance/Draenei.txt"
worgen_file_path = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Alliance/Worgen.txt"
pandaren_file_path = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Alliance/Pandaren.txt"
dracthyr_file_path = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Alliance/Dracthyr.txt"

# Horde classes
orc_file_path = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Horde/Orc.txt"
undead_file_path = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Horde/Undead.txt"
tauren_file_path = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Horde/Tauren.txt"
troll_file_path = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Horde/Troll.txt"
bloodelf_file_path = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Horde/Blood Elf.txt"
goblin_file_path = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Horde/Goblin.txt"
## Pandaren and Dracthyr can be found under "# Alliance classes"

# Specs
Death_spec = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Specs/Death Knight.txt"
Demon_spec = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Specs/Demon Hunter.txt"
Druid_spec = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Specs/Druid.txt"
Evoker_spec = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Specs/Evoker.txt"
Hunter_spec = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Specs/Hunter.txt"
Mage_spec = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Specs/Mage.txt"
Monk_spec = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Specs/Monk.txt"
Paladin_spec = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Specs/Paladin.txt"
Priest_spec = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Specs/Priest.txt"
Rogue_spec = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Specs/Rogue.txt"
Shaman_spec = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Specs/Shaman.txt"
Warlock_spec = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Specs/Warlock.txt"
Warrior_spec = "/Users/esbennielsen/Desktop/Python Projects/Wow/Text documents/Classes/Specs/Warrior.txt"

########################################################################################################################
# CODE
########################################################################################################################

# Picks faction
def faction_picker():
    with open(factions_file_path, "r") as file:
        factions = file.readlines()
        factions = [faction.strip() for faction in factions]
        chosen_faction = random.choice(factions)

        return chosen_faction

# Picks race
def choose_race(chosen_faction):
    if chosen_faction == "Alliance":
        race_file = alliance_file_path
    elif chosen_faction == "Horde":
        race_file = horde_file_path
    else:
        return [] # Returns empty list in case of bug


    with open(race_file, "r") as file:
        races = file.readlines()
        races = [race.strip() for race in races]
        chosen_race = random.choice(races)

    random.shuffle(races)  # Randomize the order of races

    return chosen_race

# Picks class
def choose_class(chosen_race):
    class_file_path = {
        "Human": human_file_path,
        "Dwarf": dwarf_file_path,
        "Night Elf": nightelf_file_path,
        "Gnome": gnome_file_path,
        "Draenei": draenei_file_path,
        "Worgen": worgen_file_path,
        "Pandaren": pandaren_file_path,
        "Dracthyr": dracthyr_file_path,
        "Orc": orc_file_path,
        "Undead": undead_file_path,
        "Tauren": tauren_file_path,
        "Troll": troll_file_path,
        "Blood Elf": bloodelf_file_path,
        "Goblin": goblin_file_path
    }

    class_file = class_file_path.get(chosen_race)

    if class_file is None:
        return []

    with open(class_file, "r") as file:
        classes = file.readlines()
        classes = [cls.strip() for cls in classes]
        chosen_class = random.choice(classes)

    random.shuffle(classes)  # Randomize the order of classes

    return chosen_class

# Picks spec
def choose_spec(chosen_class):
    spec_file_path = {
        "Death Knight": Death_spec,
        "Demon Hunter": Demon_spec,
        "Druid": Druid_spec,
        "Evoker": Evoker_spec,
        "Hunter": Hunter_spec,
        "Mage": Mage_spec,
        "Monk": Monk_spec,
        "Paladin": Paladin_spec,
        "Priest": Priest_spec,
        "Rogue": Rogue_spec,
        "Shaman": Shaman_spec,
        "Warlock": Warlock_spec,
        "Warrior": Warrior_spec
    }
    spec_file = spec_file_path.get(chosen_class)

    if spec_file is None:
        return []

    with open(spec_file, "r") as file:
        specs = file.readlines()
        specs = [spec.strip() for spec in specs]
        chosen_spec = random.choice(specs)

    random.shuffle(specs)

    return chosen_spec

# If they are not satisfied:
while True:
    chosen_faction = faction_picker()
    print("Faction:", chosen_faction)

    fac_sat = input("Are you satisfied with the choice? (Yes/No):\n")
    if fac_sat.lower() == "no":
        continue

    while True:
        races = choose_race(chosen_faction)
        print("Available Races (randomized):", races)

        race_sat = input("Are you satisfied with the race options? (Yes/No)\n")
        if race_sat.lower() == "no":
            continue
        else:
            break

    while True:
        chosen_class = choose_class(races)
        print("Class:", chosen_class)

        class_sat = input("Are you satisfied with the class choice? (Yes/No)\n")
        if class_sat.lower() == "no":
            continue
        else:
            break

    while True:
        chosen_spec = choose_spec(chosen_class)
        print("Specialization:", chosen_spec)

        spec_sat = input("Are you satisfied with the specialization choice? (Yes/No)\n")
        if spec_sat.lower() == "no":
            continue
        else:
            break

    choice_sat = input(f"Are you satisfied with playing the {chosen_faction} faction as a {races}\
 {chosen_spec} {chosen_class}? (Yes/No)\n")
    if choice_sat.lower() == "yes":
        break

# Needs updating when code is updated #
print(f"Congratulations! You'll be playing the {chosen_faction} faction. You are now a {races} {chosen_spec} {chosen_class} \
 Happy leveling!")