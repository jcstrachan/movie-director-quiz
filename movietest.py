from pip._vendor import requests
import json
from config import *
from random import randint

class Game:

	def __init__(self):

		#initialise the game attributes

		self._apiKey = api_key
		self._movieData = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=" + self._apiKey + "&language=en-US&page=1")
		self._movieData = self._movieData.json()
		self._filmTitles = []
		self._filmIds = []
		self._cScore = 0
		self._topScores = {}
		self._directorMap = self.get_director_and_film()
		self._filmTitles = self._directorMap.items()
		
		#file = open("highscores.txt","a+")
		#scoreDump = file.readlines()
		
		#for i in range(0,len(scoreDump)-1):
		#	temp = scoreDump[i]
		#	self._topScores[]

		# Take the top 20 films from the movieData list and append them to their respective attributes
		for i in range(20): 
			self._filmIds.append(self._movieData['results'][i]['id'])

		print("\nSorted films...")

	def get_director_and_film(self):
		
		print("\nGetting Director")
		directors = []
		titles = []
		infoMap = {}

		# Get a random director from the list of film IDs
		for x in self._filmIds:
			credits = "https://api.themoviedb.org/3/movie/" + str(x) + "/credits?api_key=" + self._apiKey 
			movie = "https://api.themoviedb.org/3/movie/" + str(x) + "?api_key=" + self._apiKey

			# Loop through the credits until the director is found
			try:
				for i in range(30):

					if requests.get(credits).json()['crew'][i]['job'] == 'Director':

						directors.append(requests.get(credits).json()['crew'][i]['name'])

			except IndexError:

				break

			titles.append(requests.get(movie).json()['original_title'])
		
		i = 0
		for x in titles:

			infoMap[x] = directors[i]
			i +=1

		print("\n\nDirectors: " + str(directors))
		print("\n\nTitles: " + str(titles))
		return infoMap

	def play(self):

		# Game set-up
		end = 0
		print("Welcome to Movie Test!")
		i = 0

		while end == 0:

			print(self._filmTitles)
			print(self._directorMap[self._filmTitles[i]])
			print("\nCurrent Score: " + str(self._cScore) + "")
			print("\nQuestion " + str(i+1) + ":\nWho was the director of the film " + self._filmTitles[i])
			guess = input()

			if guess == self._directorMap[self._filmTitles[i]]:
				print("Correct!")
				i += 1
				self._cScore += 1
			else:
				print("Incorrect! The correct answer was " + self._directorMap[self._filmTitles[i]] + "!")
				end = 1
			

		# Begin game


print("\nInitialising...")
game = Game()
print("\nRunning game...")
game.play()

