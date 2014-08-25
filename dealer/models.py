from django.db import models

# clubs = '♣'
# diamonds = '♦'
# hearts = '♥'
# spades = '♠'
suits = (['C', 'D', 'H', 'S'])
values = (['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'])

# Create your models here.
class Card(models.Model):
	"""Class representing card"""
	suit = models.CharField(max_length=8)
	value = models.CharField(max_length=1)

