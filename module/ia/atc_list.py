def atc_list(x):
    list_ivao_atc = []
    i = 0
    while i <= len(x):
      for r in range(0, len(x)):
        list_ivao_atc.append(x[r]["userId"])
        i = i +1
      break
    return list_ivao_atc