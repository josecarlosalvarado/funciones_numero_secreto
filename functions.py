import json
import random
import datetime
from operator import itemgetter

def play_game (scores):

    SCORE_FILE = "score_list.txt"

    secret = random.randint(1, 10)

    attempts = 0

    player = input("intruduce tu nombre")

    while True:
        guess = int(input("Guess the secret number (between 1 and 10): "))
        attempts += 1

        if guess == secret:
            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            scores. append(
                {

                    "attempts": attempts,
                    "date": str(datetime.datetime.now()),
                    "player_name": player,

                }
            )
            with open(SCORE_FILE, "w") as score_file:
                score_file.write(json.dumps(scores))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")





def lista_puntuaciones(scores):
    for score in sorted(scores, key=itemgetter("attempts")):
        print(f"{score['attempts']} attempts on day {score['date']}, {score.get('player_name', 'Anonymous Player')}")
def lectura_fichero():
    SCORE_FILE = "score_list.txt"
    with open(SCORE_FILE, "r") as score_list:
        scores = json.loads(score_list.read())
def guardado_fichero(scores):
    SCORE_FILE = "score_list.txt"
    with open(SCORE_FILE, "w") as score_file:
        score_file.write(json.dumps(scores))

