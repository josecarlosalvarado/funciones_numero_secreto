from functions import play_game, lista_puntuaciones, lectura_fichero, guardado_fichero

scores = lectura_fichero()
score = play_game()
scores.append(score)
guardado_fichero(scores)
lista_puntuaciones(scores)






