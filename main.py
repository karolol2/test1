from classes.game import Person, bcolors
from classes.magic import Spell

fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Fire", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
quake = Spell("Quake", 10, 100, "black")
meteor = Spell("Meteor", 10, 100, "black")

cure = Spell("Cure", 10, 100, "white")

magic = [{"name": "fire", "cost": 10, "dmg": 60},
         {"name": "thunder", "cost": 10, "dmg": 80},
         {"name": "blizzard", "cost": 10, "dmg": 60}]

player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure])
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors. BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    print("======================")
    player.choose_action()
    choice = input("Choose action")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of dmg")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input ("Choose magic")) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough mp\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)
        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals" + str(magic_dmg), "points of damage" + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("enemy attacks for", enemy_dmg)

    print("------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("your points: ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC + "\n")

    print("Your MP:" + bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You loose!" + bcolors.ENDC)
        running = False

