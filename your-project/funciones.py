import random
import time
from itertools import cycle

def generate_player_list(player_accounts):
	return list(player_accounts.keys())

def load_gun(gun, bullets):
	gun = ["blank" for i in range(gun-bullets)] + ["bala" for i in range(bullets)]
	return gun

def shuffle_order(element):
	new_element = element.copy()
	random.shuffle(new_element)
	return new_element

def prepare_player_shots(gun, players):
	shot_order = list(zip(gun, cycle(players)))
	return shot_order 

def shoot_gun(ready_gun, loaded_gun, players, player, player_accounts, prize):

	shot = (ready_gun[0], players[0])
	print_like_typing(f"{shot[1]} se apoya la pistola en la cabeza y aprieta el gatillo...")
	print("")
	if shot[0] == "bala" and players[0] == player:
		print("BANG!")
		print("")
		players.remove(player)
		player_accounts[player] = 0
		print_like_typing(f"Ponz dice: 'Estás muerto. Gracias por jugar {player}. JAJAJAJAJAJA'")
		print("")
		print_like_typing(f"Este es el dinero que ha ganado cada jugador: {player_accounts}")
		print("")

		return False
	elif shot[0] == "bala" and players[0] != player:
		print("BANG!")
		print("")
		players.remove(shot[1])
		loaded_gun.remove(shot[0])
		loaded_gun.append("blank")
		survival = int((loaded_gun.count("blank")/len(loaded_gun))*100)
		player_accounts[shot[1]] = 0
		print_like_typing(f"Ponz dice: '{shot[1]} disparó y ha muerto. Le echaremos de menos. JAJAJAJAJA")
		print("")
		print_like_typing(f"Quedan {loaded_gun.count('bala')} bala(s) en la pistola")
		print("")
		print_like_typing(f"El siguiente en disparar será: {players[0]}")
		print("")
		print_like_typing(f"La probabilidad de sobrevivir al siguiente disparo es del {survival}%")
		print("")
		print_like_typing(f"Siguen vivos los siguientes jugadores: {players}")
		print("")
		print_like_typing(f"Este es el dinero que ha ganado cada jugador hasta ahora: {player_accounts}")
		print("")
		return True
	else:
		print("---CLICK---")
		players.remove(shot[1])
		players.append(shot[1])
		player_accounts[shot[1]] += prize
		survival = int((loaded_gun.count("blank")/len(loaded_gun))*100)
		
		print_like_typing(f"Ponz dice: '{shot[1]} disparó, pero no pasa nada porque no había bala en el depósito. Maldita sea. Gana ${prize} dólares")
		print("")
		print_like_typing(f"Quedan {loaded_gun.count('bala')} bala(s) en la pistola")
		print("")
		print_like_typing(f"La siguiente persona en disparar será: {players[0]}")
		print("")
		print_like_typing(f"La probabilidad de sobrevivir al siguiente disparo es del {survival}%")
		print("")
		print_like_typing(f"Siguen vivos los siguientes jugadores: {players}")
		print("")
		print_like_typing(f"Este es el dinero que ha ganado cada jugador hasta ahora: {player_accounts}")
		print("")
		return True

def check_gun_option(option, gun_dict):
	if option.lower() in gun_dict.keys():
		gun_option = True
		return gun_option
	else:
		gun_option = False
		return gun_option

def selecting_gun(choose_gun_dict, guns):
	attempt = 0
	gun_option = False
	while gun_option is False:
		if attempt < 1:
			choose_gun = input(f"¿Qué pistola quieres usar? Cada pistola tiene un tamaño de cargador diferente: a) Revolver: {guns['Revolver']} balas, b) Glock: {guns['Glock']} balas, c) Beretta {guns['Beretta']} balas. Selecciona una opción: ")
			gun_option = check_gun_option(choose_gun, choose_gun_dict)
			attempt += 1
		else:
			choose_gun = input(f"Has elegido una opción que no está disponible. Por favor selecciona una de las opciones disponibles. a) Revolver: {guns['Revolver']} balas, b) Glock: {guns['Glock']} balas, c) Beretta {guns['Beretta']} balas. Selecciona una opción: ")
			gun_option = check_gun_option(choose_gun, choose_gun_dict)
	else:
		print_like_typing("¡Excelente elección!...")
		print("")
		return(choose_gun)

def choose_bullet_number(guns, chosen_gun):
	bullet_number = input(f"¿Con cuántas balas quieres jugar? Cuántas más balas, más dinero podrás ganar y más divertida será la partida... Elige un número entre 1 y {guns[chosen_gun]-1}: ")
	print("")
	while not bullet_number.isdigit():
		bullet_number = input(f"No estás prestando atención. Sé que la situación es tensa, pero tienes que concentrate. ¿Con cuántas balas quieres jugar? Elige un número entre 1 y {guns[chosen_gun]-1}: ")
		print("")
	if int(bullet_number) > guns[chosen_gun]-1:
		print(f"Recuerda que estamos jugando a la ruleta rusa. Para que al menos un jugador sobreviva hay que dejar al menos un hueco del cargador vacío. Como has pedido jugar con más balas de las permitidas vamos a usar el número máximo de balas que permite esta pistola: {guns[chosen_gun]-1} balas")
		print("")
		bullet_number = guns[chosen_gun]-1
		return bullet_number
	elif int(bullet_number) < 1:
		print(f"Vaya, parece que te crees muy inteligente queriendo jugar con 0 balas para sobrevivir ¿no? Pues por listo, vamos a jugar con el número máximo de balas que permite esta pistola: {guns[chosen_gun]-1} balas. ¡Que te diviertas! JAJAJAJAJAJA")
		print("")
		bullet_number = guns[chosen_gun]-1
		return bullet_number
		
	else:
		return int(bullet_number)

def print_like_typing(string):
	speed = 0.01
	for letter in string:
		print(letter, end="")
		time.sleep(speed)
	print("")

def intro(player, chosen_gun, bullets, prize, players):
	print("\nTe despiertas en una habitación de paredes blancas mal iluminadas por una bombilla que cuelga del centro del techo. Te duele la cabeza. Miras a tu alrededor. Ves a otras 7 personas: 3 mujeres y 4 hombres.\n")
	input("Pulsa una tecla para continuar: ")
	print(f"\nHay una pequeña puerta en la pared de enfrente. Te levantas e intentas girar el picaporte. No se mueve. Estáis encerrados. En el centro de la habitación hay una mesa sobre la que alguien ha colocado un teléfono y una pistola. Parece del modelo {chosen_gun}.\n")
	input("Pulsa una tecla para continuar: ")
	print("\nNadie habla. Algunos de tus acompañantes lloran. Otros miran al vacío. De repente suena el teléfono y os sobresalta a todos.\n")
	input("Pulsa una tecla para continuar: ")
	print("\nTras unos instantes de tensión, el hombre que está más cerca del teléfono se acerca y responde. Quien sea que está llamando le dice algo, y el hombre pone el teléfono en altavoz:\n")
	input("Pulsa una tecla para continuar: ")
	print("\n'Por fin estais todos despiertos. Empecemos la diversión'. La persona al teléfono habla con un tono metálico, como si estuviera utilizando un aparato para distorsionar su tono de voz.\n")
	input("Pulsa una tecla para continuar: ")
	print(f"\n'Me presento: soy Ponz, profesor de Ironhack. Todos los que estais aquí ya os conoceis, salvo {player}. {player}, estos son mis alumnos de Ironhack: Anahi, Diego, Bryan, Valv, Ángel, Gaby y Tito. Alumnos queridos, os presento a {player}'\n")
	input("Pulsa una tecla para continuar: ")
	print("\n'Estais aquí porque he decidido daros una oportunidad de ganar mucho dinero muy rápido. El único problemilla es que no todos sobrevivireis. No se puede tener todo en la vida JAJAJAJAJA'", "La risa del tal Ponz suena como la de un autentico psicópata. Cuando recupera la calma continúa hablando:\n")
	input("Pulsa una tecla para continuar: ")
	print(f"\n'Estas son las reglas: en la mesa hay una pistola del modelo {chosen_gun} con {bullets} balas en el cargador. Vais a ir disparando cada uno la pistola apoyada en vuestra cabeza en el siguiente orden {players}'\n")
	input("Pulsa una tecla para continuar: ")
	print(f"\nPor cada disparo de la pistola que sobreviva una persona, ganará ${prize} dólares. El primer disparo de la ronda es obligatorio. Para los siguientes disparos, como yo y mis alumnos somos buenos anfitriones, dejaremos a {player} decidir si seguimos jugando o no.'\n")
	input("Pulsa una tecla para continuar: ")
	print("\nUno de los hombres llora desesperado. Tiene acento español: '¡Ponz por favor, no nos hagas esto, no quiero moriiiir...!'. '¡Cállate Tito! No me avergüences delante de nuestro huésped o será peor...' El chico hace un esfuerzo por calmarse, aunque se le nota aún al borde del ataque de nervios.\n")
	input("Pulsa una tecla para continuar: ")
	print(f"\n'Bien. Si ya estamos todos listos, ¡que empiece la diversión!'\n")	
	input("Pulsa una tecla para empezar a jugar a LA RULETA RUSA: ")

def calculate_survival(ready_gun):
	return int((ready_gun.count("blank")/len(ready_gun))*100)



		
	






