def calcular_recompensa_por_posicao(distancia_do_centro, largura_da_pista):
    # Recompensa por estar perto do centro da pista
    if distancia_do_centro < largura_da_pista * 0.25:
        return 1
    elif distancia_do_centro < largura_da_pista * 0.5:
        return 0.5
    else:
        return 0.1

def reward_function(params):
    distancia_do_centro = params['distance_from_center']
    largura_da_pista = params['track_width']
    heading = params['heading']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    
    
    recompensa = 1.0
    
    recompensa_posicao = calcular_recompensa_por_posicao(distancia_do_centro, largura_da_pista)
    recompensa *= recompensa_posicao
    
    
    return recompensa
