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
		
		#file = open("highscores.txt","a+")
		#scoreDump = file.readlines()
		
		#for i in range(0,len(scoreDump)-1):
		#	temp = scoreDump[i]
		#	self._topScores[]

		# Take the top 20 films from the movieData list and append them to their respective attributes
		for i in range(20): 
			self._filmIds.append(self._movieData['results'][i]['id'])
			self._filmTitles.append((self._movieData['results'][i]['title']))

		print("\nSorted films...")

	def get_director_and_film(self):
		
		print("\nGetting Director")
		info = []

		# Get a random director from the list of film IDs
		j = randint(0,len(self._filmIds) - 1)
		credits = "https://api.themoviedb.org/3/movie/" + str(self._filmIds[j]) + "/credits?api_key=" + self._apiKey 
		movie = "https://api.themoviedb.org/3/movie/" + str(self._filmIds[j]) + "?api_key=" + self._apiKey

		# Loop through the credits until the director is found
		for i in range(30):

			if requests.get(credits).json()['crew'][i]['job'] == 'Director':

				info.append(requests.get(credits).json()['crew'][i]['name'])

		info.append(requests.get(movie).json()['original_title'])
		return info

	def play(self):

		# Game set-up
		end = 0
		print("Welcome to Movie Test!")
		i = 0

		while end == 0:

			info = self.get_director_and_film()
			print(info)
			answer = info[0]
			print("\nQuestion " + str(i) + ":\nWho was the director of the film " + info[1])
			guess = input()

			if answer == guess:
				print("Correct!")
				i += 1
				self._cScore += 1
			else:
				print("Incorrect! The correct answer was " + answer + "!")
				end = 1
			

		# Begin game


print("\nInitialising...")
game = Game()
print("\nRunning game...")
game.play()

