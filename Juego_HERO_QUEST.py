
#Juego HERO QUEST

# Reglas de enfrentamiento:
    # Cada ataque o cada defensa que tenga el personaje = una tirada de dado
    # Para que se produzca un ataque = dado > 3
    # Para defender un ataque, la Momia debe sacar en la tirada = (dado = 6)
    # Para defender un ataque, el Bárbaro debe sacar en la tirada = (dado > 4)

# Superclase PERSONAJE
class Personaje():

    def __init__(self,
    __nombre="Sin información",
    __vida=0,
    __ataque=0,
    __defensa=0):
        self.__nombre = __nombre
        self.__vida = __vida
        self.__ataque = __ataque
        self.__defensa = __defensa
    
    @property 
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nuevoValor):
        self.__nombre = nuevoValor
    
    @property 
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self,nuevoValor):
        self.__vida = nuevoValor
    
    @property 
    def ataque(self):
        return self.__ataque
    @ataque.setter
    def ataque(self,nuevoValor):
        self.__ataque = nuevoValor

    @property 
    def defensa(self):
        return self.__defensa
    @defensa.setter
    def defensa(self,nuevoValor):
        self.__defensa = nuevoValor
    

    def estarVivo(self):
        estado_vida = self.vida
        estado_final = bool()
        
        if self.vida < 0:
            self.vida = 0
        
        if estado_vida > 0:
            estado_final = True
        else:
            estado_final = False

        
        return estado_final

    def atacar(self): 
        nivel_ataque = self.ataque
        contador = 0
        lista_tiradas_dado = []
        tiradas_validas = []
        impactos = 0
        while contador < nivel_ataque:
            tirar_dado = (Dado().tira())
            print("Tira dado:",tirar_dado)
            lista_tiradas_dado.append(tirar_dado)
            contador += 1
        for i in lista_tiradas_dado:
            if i > 3:
                tiradas_validas.append(1)
        for l in tiradas_validas:
            l
            impactos +=1
        print("Son {} impactos".format(impactos))
        return impactos

    def __str__(self):
        return """PERSONAJE:
        -Nombre: {}
        -Vida: {}
        -Ataque: {}
        -Defensa: {} """.format(
            self.nombre,
            self.vida,
            self.ataque,
            self.defensa)

# Subclase MOMIA
class Momia(Personaje):
    
    def __init__(self,
    __nombre="Sin información",
    __vida=0,
    __ataque=0,
    __defensa=0):
        self.__nombre = __nombre
        self.__vida = __vida
        self.__ataque = __ataque
        self.__defensa = __defensa

        super().__init__(__nombre,__vida,__ataque,__defensa)
    
    def defender(self,numImpacto=0): 
        contador = 1
        impacto = numImpacto 
        defensas = 0
        impactos_sufridos=0
        lista_tiradas_dado = []
        tiradas_validas = []
        if numImpacto > 0:
            while contador <= self.defensa:
                tirar_dado = (Dado().tira())
                print("La Momia tira el dado para defender:",str(tirar_dado))
                lista_tiradas_dado.append(tirar_dado)
                contador += 1           
            for i in lista_tiradas_dado:
                if i == 6:
                    tiradas_validas.append(i)
            for l in tiradas_validas:
                l
                defensas +=1
            if defensas > numImpacto:
                defensas = numImpacto
            print("Son",defensas,"defensas")
            impactos_sufridos = impacto - defensas
            if numImpacto == 0:
                impactos_sufridos = 0
        else:
            print("No hay impactos que defender")
        return impactos_sufridos
    
    def __str__(self):
        return """ Los parámetros de la Momia creada son:
        -Nombre: {}
        -Vida: {}
        -Ataque: {}
        -Defensa: {}""".format(
            self.nombre,
            self.vida,
            self.ataque,
            self.defensa)

# Subclase BARBARO
class Barbaro(Personaje):
    
    def __init__(self,
    __nombre="Sin información",
    __vida=0,
    __ataque=0,
    __defensa=0):
        self.__nombre = __nombre
        self.__vida = __vida
        self.__ataque = __ataque
        self.__defensa = __defensa

        super().__init__(__nombre,__vida,__ataque,__defensa)
    
    def defender(self,numImpacto=0): 
        contador = 1
        impacto = numImpacto
        defensas = 0
        impactos_sufridos=0
        lista_tiradas_dado = []
        tiradas_validas = []
        impactos_sufridos = int()  # 1 impacto
        if numImpacto > 0:
            while contador <= self.defensa:
                tirar_dado = (Dado().tira())
                print("El Bárbaro tira el dado para defender:",str(tirar_dado))
                lista_tiradas_dado.append(tirar_dado)
                contador += 1           
            for i in lista_tiradas_dado:
                if i > 4:
                    tiradas_validas.append(i)
            for l in tiradas_validas:
                l
                defensas +=1
            if defensas > numImpacto:
                defensas = numImpacto
            print("Son",defensas,"defensas")
            impactos_sufridos = impacto - defensas
            if numImpacto == 0:
                impactos_sufridos = 0
        else:
            print("No hay impactos que defender")
        return impactos_sufridos

        
    def __str__(self):
        return """Los parámetros del bárbaro creado son:
        -Nombre: {}
        -Vida: {}
        -Ataque: {}
        -Defensa: {}""".format(
            self.nombre,
            self.vida,
            self.ataque,
            self.defensa)

# Clase DADO
class Dado():
    def tira(numCaras=6): 
        import random
        resultado = (random.randint(1,6))
        return resultado


# PROGRAMA PRINCIPAL.
# Se establece la dinámica del juego y la creación de personajes y características

if __name__ == "__main__":

    contador_turnos_partida = int(0)
    dado = Dado().tira()
    estado_vida_barbaro1 = True
    estado_vida_momia1 = True
    
    
    print("Bienvenido al juego HERO QUEST")
    print("\nPara poder jugar, deberás crear un personaje \"momia\" y un personaje \"bárbaro\".")
    print("\n")
    momia1 = (Momia(
        input("Indica el nombre de la momia: "),
        int(input("Indica el número de vidas que tiene: ")),
        int(input("Indica el ataque que tiene: ")),
        int(input("Indica la defensa que tiene: "))))
    print("\n")
    barbaro1 = (Barbaro(
        input("Indica el nombre del bárbaro: "),
        int(input("Indica el número de vidas que tiene: ")),
        int(input("Indica el ataque que tiene: ")),
        int(input("Indica la defensa que tiene: "))))
    print("\n")
    turnos_partida = int(input(""" Indica cuántos turnos máximos quieres jugar,
    debiendose ser el número de turnos un número par: """))
        
    print("""Tira el dado para saber quién comienza el juego:
    -si sale del 1 al 3, la momia comienza el juego
    -si sale del 4 al 6, el bárbaro comienza el juego""")
    print(dado)

    if dado < 4:

        #La Momia comienza el turno
        while contador_turnos_partida < turnos_partida and estado_vida_barbaro1 == True and estado_vida_momia1 == True:
                    contador_turnos_partida += 1
                    pregunta_tirador_dado = input("\nIndica S para seguir: ")
                    print("Es el turno",contador_turnos_partida,"de",turnos_partida) 
                    print("La momia",momia1.nombre,"ataca y tira el dado")
                    ataque_momia = momia1.atacar()
                    impactosNoDetenidosBarbaro= barbaro1.defender(numImpacto=ataque_momia)
                    print("El bárbaro",barbaro1.nombre,"ha sufrido {} impactos.".format(impactosNoDetenidosBarbaro))
                    barbaro1.vida=(barbaro1.vida-impactosNoDetenidosBarbaro)
                    estado_vida_barbaro1 = barbaro1.estarVivo()
                    print("El bárbaro",barbaro1.nombre,"queda con",barbaro1.vida,"de vida.")
                    estado_vida_barbaro1 = barbaro1.estarVivo()
        # El Bárbaro continúa el turno       
                    contador_turnos_partida += 1
                    pregunta_tirador_dado = input("\nIndica S para seguir: ")
                    print("Es el turno",contador_turnos_partida,"de",turnos_partida) 
                    print("El bárbaro",barbaro1.nombre,"ataca y tira el dado")
                    ataque_barbaro = barbaro1.atacar()
                    impactosNoDetenidosMomia= momia1.defender(numImpacto=ataque_barbaro)
                    print("La momia",momia1.nombre,"ha sufrido {} impactos.".format(impactosNoDetenidosMomia))
                    momia1.vida=(momia1.vida-impactosNoDetenidosMomia)
                    estado_vida_momia1 = momia1.estarVivo()
                    print("La momia",momia1.nombre,"queda con",momia1.vida,"de vida.")
                    estado_vida_momia1 = momia1.estarVivo()

                
        # Finalización de la partida cuando se da una de las tres condiciones del while que abre el bucle       
        else:
                print("\nEl bárbaro",barbaro1.nombre,"queda con {} de vida.".format(barbaro1.vida))
                print("La momia",momia1.nombre,"queda con {} de vida.".format(momia1.vida))
                if barbaro1.vida > momia1.vida:
                    print("El bárbaro",barbaro1.nombre,"ha ganado la partida!")
                elif barbaro1.vida < momia1.vida:
                    print("La momia",momia1.nombre,"ha ganado la partida!")
                elif barbaro1.vida == momia1.vida:
                    print("La momia",momia1.nombre,"y el",barbaro1.nombre,"bárbaro han quedado en tablas")
                print("El juego ha terminado.")
    
    
    elif dado >= 4:
        # El Bárbaro comienza el turno
        while contador_turnos_partida < turnos_partida and estado_vida_barbaro1 == True and estado_vida_momia1 == True:
                contador_turnos_partida += 1
                pregunta_tirador_dado = input("\nIndica S para seguir: ")
                print("Es el turno",contador_turnos_partida,"de",turnos_partida) 
                print("El bárbaro",barbaro1.nombre,"ataca y tira el dado")
                ataque_barbaro = barbaro1.atacar()
                impactosNoDetenidosMomia= momia1.defender(numImpacto=ataque_barbaro)
                print("La momia",momia1.nombre,"ha sufrido {} impactos.".format(impactosNoDetenidosMomia))
                momia1.vida=(momia1.vida-impactosNoDetenidosMomia)
                estado_vida_momia1 = momia1.estarVivo()
                print("La momia",momia1.nombre,"queda con",momia1.vida,"de vida.")
                estado_vida_momia1 = momia1.estarVivo()
        #La Momia continúa el turno      
                contador_turnos_partida += 1
                pregunta_tirador_dado = input("\nIndica S para seguir: ")
                print("Es el turno",contador_turnos_partida,"de",turnos_partida) 
                print("La momia",momia1.nombre,"ataca y tira el dado")
                ataque_momia = momia1.atacar()
                impactosNoDetenidosBarbaro= barbaro1.defender(numImpacto=ataque_momia)
                print("El bárbaro",barbaro1.nombre,"ha sufrido {} impactos.".format(impactosNoDetenidosBarbaro))
                barbaro1.vida=(barbaro1.vida-impactosNoDetenidosBarbaro)
                estado_vida_barbaro1 = barbaro1.estarVivo()
                print("El bárbaro",barbaro1.nombre,"queda con",barbaro1.vida,"de vida.")
                estado_vida_barbaro1 = barbaro1.estarVivo()

                
        # Finalización de la partida cuando se da una de las tres condiciones del while que abre el bucle        
        else:
                print("\nEl bárbaro",barbaro1.nombre,"queda con {} de vida.".format(barbaro1.vida))
                print("La momia",momia1.nombre,"queda con {} de vida.".format(momia1.vida))
                if barbaro1.vida > momia1.vida:
                    print("El bárbaro",barbaro1.nombre,"ha ganado la partida!")
                elif barbaro1.vida < momia1.vida:
                    print("La momia",momia1.nombre,"ha ganado la partida!")
                elif barbaro1.vida == momia1.vida:
                     print("La momia",momia1.nombre,"y el",barbaro1.nombre,"bárbaro han quedado en tablas")
                print("El juego ha terminado.")
                    
  

