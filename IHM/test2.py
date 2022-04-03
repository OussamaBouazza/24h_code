# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 23:57:05 2022

@author: thoma
"""
import pygame
import requests
import sys
from pygame.draw import line
from pygame.math import Vector2

class Niveau:
    
    
	"""Classe permettant de créer un niveau"""
	def __init__(self, array):
		self.array = array
		self.structure = 0
	
	
	def generer(self):
		"""Méthode permettant de générer le niveau en fonction du tableau
		structure_niveau = []
		#On parcourt les lignes du fichier
		for ligne in array:
			ligne_niveau = []
			#On parcourt les sprites (lettres) contenus dans le fichier
			for sprite in ligne:
				#On ignore les "\n" de fin de ligne
				if sprite != '\n':
					#On ajoute le sprite à la liste de la ligne
					ligne_niveau.append(sprite)
			#On ajoute la ligne à la liste du niveau
			structure_niveau.append(ligne_niveau)
		#On sauvegarde cette structure
		self.structure = structure_niveau"""
	
	
	def afficher(self, fenetre):
		"""Méthode permettant d'afficher le niveau en fonction 
		de la liste de structure renvoyée par generer()"""
		#Chargement des images 
		vaisseau = pygame.image.load(haut).convert()
		planete = pygame.image.load(image_planete).convert()
		
		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_case * cell_size
				y = num_ligne * cell_size
				if sprite == 'Arrive':		   
					fenetre.blit(vaisseau, (x,y))
				elif sprite == 'Planete':		   
					fenetre.blit(planete, (x,y))
                    
				num_case += 1
			num_ligne += 1
			
		
			
class Perso:
	"""Classe permettant de créer un personnage"""
    
	def __init__(self, droite, gauche, haut, bas, niveau):
		#Sprites du personnage
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		#Position du personnage en cases et en pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Direction par défaut
		self.direction = self.haut
		#Niveau dans lequel le personnage se trouve
		self.niveau = niveau
	
	
	def deplacer(self, direction):
		"""Methode permettant de déplacer le vaisseau mais on s'en fou pck on fait plus ça"""
		
		#Déplacement vers la droite
		if direction == 'droite':
			#Pour ne pas dépasser l'écran
			if self.case_x < (nb_sprite - 1):
				#On vérifie que la case de destination n'est pas un mur
				if self.niveau.structure[self.case_y][self.case_x+1] != 'M':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * cell_size
			#Image dans la bonne direction
			self.direction = self.droite
		
		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != 'M':
					self.case_x -= 1
					self.x = self.case_x * cell_size
			self.direction = self.gauche
		
		#Déplacement vers le haut
		if direction == 'haut':
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != 'M':
					self.case_y -= 1
					self.y = self.case_y * cell_size
			self.direction = self.haut
		
		#Déplacement vers le bas
		if direction == 'bas':
			if self.case_y < (nb_sprite - 1):
				if self.niveau.structure[self.case_y+1][self.case_x] != 'M':
					self.case_y += 1
					self.y = self.case_y * cell_size
			self.direction = self.bas

		#Déplacement saut droite
		if direction == 'sdroite':
			if self.case_x < (nb_sprite - 2):
				if self.niveau.structure[self.case_y][self.case_x+2] != 'M':
					self.case_x += 2
					self.x = self.case_x * cell_size
			self.direction = self.droite
            
		#Déplacement vers la gauche
		if direction == 'sgauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-2] != 'M':
					self.case_x -= 2
					self.x = self.case_x * cell_size
			self.direction = self.gauche


