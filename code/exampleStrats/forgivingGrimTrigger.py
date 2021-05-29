# Reminder: For the history array, "tell truth" = 0, "stay silent" = 1

# Forgiving Grim Trigger
# Created by Heliodex, 20th May 2021
# Last updated 24th May 2021, tomorrow is my 14th birthday yay


def strategy(history, memory):
	if history.shape[1] == 0:  # We're on the first turn!
		return "stay silent", None

	choice = "stay silent"
	if history.shape[1] >= 1 and history[1,-1] == 0:  # Choose to "tell the truth" if the opponent also just "told the truth".
		return "tell truth", None

	try: # "index -2 is out of bounds" Now I remember why I left python.
		if history[0,-2] == 0 and history[0,-1] == 0:
			choice = "tell truth"
	except: # Cary, why couldn't we do this in C++?
		if history[0,-1] == 0:
			choice = "tell truth"

	return choice, None


# This originally started as an attempt to make an "tit for two tats".

# Telling the truth once will just do tit for tat.
# Telling the truth twice in a row will activate grim
# trigger mode.

# Against the other 10 example algorithms, it beats Tit 
# for Tat by about 0.08 average. It probably won't fare
# well in the real competition, due to its inability to 
# react to the opponents' strategy once grim trigger mode 
# has been activated.


# I did have another program that won almost every match,
# but the score came out bad overall because it didn't 
# cooperate as well.