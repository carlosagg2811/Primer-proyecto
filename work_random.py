
# adivina el numero

import random

numero = random.randint(1, 100)
                       
intentos = 0
max_intentos = 10
print("¡Hola! Estoy pensando en un número entre 1 y 100.")

while intentos < max_intentos:
        try:
            estimacion = int(input("Intenta adivinar: "))  # Solicita al usuario su estimación
            
            intentos += 1  # Incrementa el contador de intentos    
            if estimacion < numero:
                print("Tu estimación es muy baja.")
                    
                print(f"Le quedan {intentos} intentos:")
                
            elif estimacion > numero:

                print(f"Le quedan {intentos} intentos:")
                print("Tu estimación es muy alta.")
            else:
                print(f"¡Buen trabajo! Has adivinado mi número en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")
    
        if intentos == max_intentos and estimacion != numero:
            print(f"Lo siento, no has adivinado. El número era {numero}.")
