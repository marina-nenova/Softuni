def cast_spell(hero, mp_needed, spell_name):
    if heroes[hero]["mp"] >= mp_needed:
        heroes[hero]["mp"] -= mp_needed
        print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['mp']} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {spell_name}!")


def take_damage(hero, damage, attacker):
    heroes[hero]['hp'] -= damage
    if heroes[hero]['hp'] > 0:
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['hp']} HP left!")
    else:
        print(f"{hero} has been killed by {attacker}!")
        del heroes[hero]


def recharge(hero, mp_amount):
    amount_recovered = mp_amount
    if heroes[hero]['mp'] + mp_amount > max_mp:
        amount_recovered = max_mp - heroes[hero]['mp']
    heroes[hero]['mp'] += amount_recovered
    print(f"{hero} recharged for {amount_recovered} MP!")


def heal(hero, hp_amount):
    amount_recovered = hp_amount
    if heroes[hero]['hp'] + hp_amount > max_hp:
        amount_recovered = max_hp - heroes[hero]['hp']
    heroes[hero]['hp'] += amount_recovered
    print(f"{hero} healed for {amount_recovered} HP!")


n = int(input())
max_mp = 200
max_hp = 100

heroes = {}
for _ in range(n):
    name, hp, mp = input().split()
    heroes[name] = {'hp': int(hp), 'mp': int(mp)}

command = input()

while not command == "End":
    data = command.split(" - ")
    action = data[0]
    hero_name = data[1]

    if action == "CastSpell":
        mp_needed = int(data[2])
        spell = data[3]
        cast_spell(hero_name, mp_needed, spell)

    elif action == "TakeDamage":
        damage = int(data[2])
        attacker = data[3]
        take_damage(hero_name, damage, attacker)

    elif action == "Recharge":
        mp_amount = int(data[2])
        recharge(hero_name, mp_amount)

    elif action == "Heal":
        hp_amount = int(data[2])
        heal(hero_name, hp_amount)
    command = input()

for hero_name, info in heroes.items():
    print(hero_name)
    print(f'  HP: {info["hp"]}')
    print(f'  MP: {info["mp"]}')
