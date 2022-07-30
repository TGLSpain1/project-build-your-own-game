from funciones import selecting_gun, load_gun, choose_bullet_number

player_alive = True
guns = {"Revolver": 6, "Glock": 10, "Beretta": 12}
choose_gun_dict = {"a": "Revolver", "b": "Glock", "c": "Beretta"}
player = str(input("¿Cuál es tu nombre?: "))
print("")
player_accounts = {"Anahi-Ironhack": 0, "Gaby-Ironhack": 0, "Diego-Ironhack": 0, "Valv-Ironhack": 0, "Tito-Ironhack": 0, "Bryan-Ironhack": 0, "Ángel-Ironhack": 0}
player_accounts[player] = 0

choose_gun = selecting_gun(choose_gun_dict, guns)
print("")

chosen_gun = choose_gun_dict[choose_gun]
gun = guns[chosen_gun]

bullets = choose_bullet_number(guns, chosen_gun)
print("")

loaded_gun = load_gun(gun, bullets)

prize = int((bullets/gun)*10000)


