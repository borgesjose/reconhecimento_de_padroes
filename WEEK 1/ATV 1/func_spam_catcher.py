def span_catcher(w):
        


    neutro = {"a", "o", "as","de","ou","para", "e"};
    fortes = {"grátis", "oferta", "promoção", "emagreça", "crédito", "dieta", "financiamento"};
    fracas = {"relatório", "disciplina", "atividade", "prática", "entrega", "nota"};
    input_w = {w}

    flag_n = input_w.issubset(neutro)
    flag_forte = input_w.issubset(fortes)
    flag_fraco = input_w.issubset(fracas)

    if  not( flag_n or flag_forte or flag_fraco):   
        raise TypeError("A palavra não esta contida nos conjuntos predefinidos.")

    flags = [flag_n , flag_forte , flag_fraco]
    conjunto = 0
    for i in range(3):
        if flags[i]:
            conjunto = i; 

    prob_x = [0.5,0.95,0.2]
    prob_y = [0.25,0.2,0.05]

    x = prob_x[conjunto]
    y = prob_y[conjunto]

    prob_X_Y = x*0.8/(x*0.8 + 0.2 -0.2*y )

    return prob_X_Y