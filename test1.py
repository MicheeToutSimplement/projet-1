# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 16:57:21 2023

@author: Michée Mavinga
"""
from implémentation1 import *
import unittest
class TestStringMethods(unittest.TestCase):
    
#Classe de Rectangle

    def test_upper(self):
        a = Rectangle(20,15).calcul_perimetre()
        b = 70
        self.assertEqual(a,b)

    def test_isupper(self):
        c = Rectangle(5,13).calcul_surface()
        d = 65
        self.assertEqual(c,d)
        
#Classe de cercle

    def test_circleperim(self):
        e = cercle(5.314).calcul_perimetre()
        f = 33.38884672235232
        self.assertEqual(e,f)

    def test_circlesurf(self):
        g = cercle(2).calcul_surface()
        h = 12.566370614359172
        self.assertEqual(g,h)
        
#Classe de Triangle

    def test_Triperim(self):
        e = Triangle(5,5,6,2).calcul_perimetre() #la class Triangle définie
        f = 13           #def __init__(self, hauteur, cotéa, cotéb, cotéc)
        self.assertEqual(e,f)

    def test_Trisurf(self):
        g = Triangle(3,8,6,5).calcul_surface() # 3=hauteur, 8=base
        h = 12
        self.assertEqual(g,h)

#Classe de carrée

    def test_carupper(self):
        a = Carre(20).calcul_perimetre()
        b = 80
        self.assertEqual(a,b)

    def test_carsupper(self):
        c = Carre(17).calcul_surface()
        d = 289
        self.assertEqual(c,d)

#Classe de Triangle Rectangle

    def test_TriaRectperim(self):
        a = Triangle_rectangle(4,3).calcul_perimetre()
        b = 12
        self.assertEqual(a,b)

    def test_TriaRectsurf(self):
        c = Triangle_rectangle(3,4).calcul_surface()
        d = 6
        self.assertEqual(c,d)

if __name__ == '__main__':
    unittest.main()