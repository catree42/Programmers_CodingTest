def solution(bandage, health, attacks):
    heal_time = 0
    max_health = health
    
    for i in range(len(attacks)):
        if i == 0:
            health -= attacks[i][1]
            if health <= 0 :
                return -1
            continue
        
        heal_time = attacks[i][0] - attacks[i-1][0] -1 
        health += heal_time * bandage[1]
        health += bandage[2]*int(heal_time/bandage[0])
        if health > max_health :
            health = max_health
        
        health -= attacks[i][1]
        if health <= 0 :
            return -1

    return health