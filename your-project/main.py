def russian_roulette():
	import funciones

	# Ver si puedo cambiar texto de color para por ejemplo destacar el nombre del jugador.
	# Pensar tests y ejecutarlos para cada posible outcome
	# Ejecutar desde línea de comando
	funciones.print_like_typing("Bienvenido a la Ruleta Rusa de Ironhack, un juego de Tito Guitard Lejarreta\n")
	funciones.print_like_typing("Cualquier parecido con la realidad es pura coincidencia.\n") 
	funciones.print_like_typing("O no...\n")
	funciones.print_like_typing("Espero que disfrutes :p\n")

	import variables

	players = funciones.generate_player_list(variables.player_accounts)
	players = funciones.shuffle_order(players)
	loaded_gun = variables.loaded_gun
	ready_gun = funciones.shuffle_order(loaded_gun)
	survival = int((ready_gun.count("blank")/len(ready_gun))*100)

	play_intro = "" 
	while play_intro.lower() not in ["n", "s"]:
		play_intro = input("¿Quieres saltarte la introducción? Pulsa 's' para SÍ o 'n' para NO: ")
		print("")
	else:
		if play_intro.lower() == "n":
			funciones.intro(variables.player, variables.chosen_gun, variables.bullets, variables.prize, players)

	print("")
	funciones.print_like_typing("########################################################")
	funciones.print_like_typing("Comienza el juego...")
	funciones.print_like_typing("########################################################")
	print("")

	funciones.print_like_typing(f"Este es el dinero que ha ganado cada jugador hasta el momento: {variables.player_accounts}")
	print("")
	funciones.print_like_typing(f"Este el el orden en el que dispararán los jugadores: {players}")
	print("")
	funciones.print_like_typing(f"El premio que recibirá un jugador por cada disparo que sobreviva  será de ${variables.prize} dólares.")
	print("")
	funciones.print_like_typing(f"La probabilidad de sobrevivir al siguiente disparo es del {survival}%")
	print("")

	input("Pulsa una tecla para ejecutar el siguiente disparo")
	print("")

	variables.player_alive = funciones.shoot_gun(ready_gun, loaded_gun, players, variables.player, variables.player_accounts, variables.prize)
	if variables.player_alive is False:
		funciones.print_like_typing("Game over")

	else:
		while variables.player_alive and len(players) > 1 and loaded_gun.count("bala") > 0:
			keep_playing = ""
			while keep_playing.lower() not in ["s", "n"]:		
				keep_playing = input("¿Quieres seguir jugando? Pulsa 's' para SÍ o 'n' para NO: ")
				print("")
			else:
				if keep_playing.lower() == "s":			
					ready_gun = funciones.shuffle_order(loaded_gun)
					variables.player_alive = funciones.shoot_gun(ready_gun, loaded_gun, players, variables.player, variables.player_accounts, variables.prize)
					if len(players) < 1:
						variables.player_alive = False
				else:
					print(f"Ponz dice: 'De acuerdo cobarde. Puedes irte. Has ganado ${variables.player_accounts[variables.player]}. Disfruta del resto de tu vida...")
					variables.player_alive = False

		else:
			if loaded_gun.count("bala") < 1:
				funciones.print_like_typing("Ponz dice: 'Ya no quedan más balas en la pistola. Se acabó el juego. Enhorabuena a los supervivientes...'")
			elif len(players) < 2:
				funciones.print_like_typing(f"Ponz dice: 'Enhorabuena {variables.player}. Has ganado. Disfruta el dinero y vuelve cuando quieras...'")
			funciones.print_like_typing("Game over")

if __name__ == '__main__':
	russian_roulette()


			











	

