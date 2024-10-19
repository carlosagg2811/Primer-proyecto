# basico de un condicional 

print("""
      ***********************************************
      Para validar si eres mayor o nemor de EDAD
      ***********************************************
      """)
edad = int(input("por favor digita tu edad "))
if edad >= 18:
    print("eres mayor de edad")
    print("""
      ***********************************************
      ahora podemos continuar la entrevista...
      ***********************************************    
      """)  
    ciudad = str(input("digita tu ciudad de origen "))
    print("gracias estaremos validadndo la informacion y nos coumicaremos a la mayor brevedad posible")
    

else:
    print("eres menor de edad")
    print("""
      ***********************************************
      No podemos continuar la entrevista, lo siento 
      ***********************************************
      """)
    
    