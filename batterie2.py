from implémentation2 import *

import time

start = time.time()

if __name__ == '__main__':
    



    myRectangle = Rectangle(32,28)
    print("Le périmètre du rectangle vaut ",myRectangle.calcul_perimetre(),"mètres")
    print("La surface du rectangle vaut ",myRectangle.calcul_surface(),"mètres carré")

    myCircle = cercle(14)
    print("Le périmètre du cercle vaut",myCircle.calcul_perimetre(),"mètres")
    print("La surface du cercle",myCircle.calcul_surface(),"mètres carré")

    myTriangle = Triangle(15.4,12,40,25)
    print("Le périmètre du triangle vaut ",myTriangle.calcul_perimetre(),"mètres")
    print("La surface du triangle est ",myTriangle.calcul_surface(),"mètres carré")

    mySquare = Carre(5)
    print("Le périmètre du carré vaut ",mySquare.calcul_perimetre(),"mètres")
    print("La surface du carré vaut ",mySquare.calcul_surface(),"mètres carré")

    myRecTriangle = Triangle_rectangle(20,15)
    print("Le périmètre du triangle rectangle vaut ",myRecTriangle.calcul_perimetre(),"mètres")
    print("La surface du triangle rectangle vaut ",myRecTriangle.calcul_surface(),"mètres carré")

    end = time.time()

    print(end-start)




