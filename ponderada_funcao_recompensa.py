# -*- coding: utf-8 -*-
"""Ponderada_Funcao_Recompensa.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ra-2j0Dmfqfe41aCi72ioU0cKUtNW91B
"""

def calculate_reward_by_position(distance_from_center, track_width):
    # Recompensa por estar perto do centro da pista
    if distance_from_center < track_width * 0.25:
        return 1
    elif distance_from_center < track_width * 0.5:
        return 0.5
    else:
        return 0.1

def reward_function(params):
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    reward = 1.0

    # Calcula a recompensa com base na posição
    position_reward = calculate_reward_by_position(distance_from_center, track_width)
    reward *= position_reward


    return reward