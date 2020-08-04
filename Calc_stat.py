def calc_stat(listened):
    return(f'Вы прослушали {len(listened)} песен, общей продолжительностью {sum(listened)//60} минут и {sum(listened)%60} секунд.')
        
print(calc_stat([193, 148, 210, 144, 174, 159, 163, 189, 230, 204]))
