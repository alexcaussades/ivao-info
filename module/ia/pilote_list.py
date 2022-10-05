def pilote_list(p):
    list_ivao_pilot = []
    i = 0
    while i <= len(p):
        for r in range(0, len(p)):
            list_ivao_pilot.append(p[r]["userId"])
            i = i+1
        break
    return list_ivao_pilot
