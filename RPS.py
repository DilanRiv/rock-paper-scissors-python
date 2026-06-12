import random

OPCIONES = [ "rock", "paper", "scissors"]
TRADUC = {
    "rock": "rock", 
    "paper": "paper", 
    "scissors": "scissors",
    "piedra": "rock",
    "papel": "paper", 
    "tijera": "scissors"
    }
  
TRADUCCION_SALIDA = {
    "rock": "piedra/rock",
    "paper": "papel/paper",
    "scissors": "tijera/scissors"
       }

puntaje = 0
def actualizar_puntaje (cantidad):
   global puntaje
   puntaje += cantidad
   
   
   
def jugar():
  
  pc = random.choice(OPCIONES)
  try :
   user = input("Elije entre PIEDRA PAPEL TIJERA/ Choose between ROCK PAPER SCISSORS \n").strip().lower()
   usertradu = TRADUC[user]
  except KeyError:
     print("Opcion no Valida/ Invalid Option")
     return

  print ("Tu eleccion/Your choice: " + user + " \nEleccion rival/Rival Choice : "+ TRADUCCION_SALIDA [pc] )
  resultado = determinar_ganador(usertradu,pc)

  if resultado == "usuario":
      print("GANASTES / YOU WON (+2pts)")
      actualizar_puntaje(2)
  elif resultado == "pc":
      print ("PERDISTES / YOU LOSE (-1pts)")
      actualizar_puntaje(-1)
  else:
      print ("EMPATE / DRAW")
  
     
def determinar_ganador(user,pc):
    if user == pc:
        return "empate"
    elif user == "rock" and pc == "scissors":
        return "usuario"
    elif user == "paper" and pc == "rock":
        return "usuario"
    elif user == "scissors" and pc == "paper":
        return "usuario"
    else :
        return "pc"
    
def mejor_de_tres():
    vic_usuario = 0
    vic_pc = 0
    while vic_usuario < 2 and vic_pc < 2 :

        pc = random.choice(OPCIONES)
        try :
         user = input("Elije entre PIEDRA PAPEL TIJERA/ Choose between ROCK PAPER SCISSORS \n").strip().lower()
         usertradu = TRADUC[user]
        except KeyError:
         print("Opcion no Valida/ Invalid Option")
         continue

        print ("Tu eleccion/Your choice: " + user + " \nEleccion rival/Rival Choice : "+ TRADUCCION_SALIDA [pc] )
        resultado = determinar_ganador(usertradu,pc)

        if resultado == "usuario":
          print("GANASTES / YOU WON")
          vic_usuario += 1
        elif resultado == "pc":
           print ("PERDISTES / YOU LOSE")
           vic_pc += 1
        else:
         print ("EMPATE / DRAW")

    if vic_usuario == 2:
       print("GANASTES LA SERIE/YOU WON THE SERIES (+5pts)")
       actualizar_puntaje(5)
    else : 
       print("PERDISTES LA SERIE/YOU LOST THE SERIES (-4pts)") 
       actualizar_puntaje(-4)



while True :
    
    menu = input("Bienvenido a Piedra Papel Tijera / Welcome to Rock Paper Scissors \n 1.Mejor de 1/Best of 1 \n 2.Mejor de 3/Best of 3 \n 3.Puntaje/Score \n 4.Salida/Exit \n").strip().lower()
    if menu == "1":
         jugar()
         print()
        
    elif menu == "2":

        mejor_de_tres()


    elif menu == "3":
        print("EL PUNTAJE ACUMULADO ES / SCORE: " + str(puntaje))

    elif menu == "4":
        
        print("GRACIAS POR JUGAR / THANKS FOR PLAYING")
        break
    else:
        print("OPCION NO VALIDA/INVALID OPTION")

  



















