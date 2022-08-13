geracaoxn = 0
geracaoyn = 0
geracaozn = 0
sexom = 0
sexof = 0
pfutbols = 0
pfutboln = 0
bganhars = 0
bganharn = 0

for x in range(2):
    geracao = str(input('você é da geracão  X,Y ou Z ? '))
    if geracao == 'X':
        geracaoxn = geracaoxn+1
    if geracao == 'Y':
        geracaoyn = geracaoyn+1
    if geracao == 'Z':
        geracaozn = geracaozn+1

    sexo = str(input('Seu sexo é masculino ou feminino? '))
    if sexo == 'masculino':
        sexom = sexom+1
    elif sexo == 'feminino':
        sexof = sexof+1

    pfutbol = str(input('Pratica ou já praticou futebol?\nResponda com sim ou não! '))
    if pfutbol == 'sim':
        pfutbols = pfutbols+1
    if pfutbol == 'não':
        pfutboln = pfutboln+1

    bganhar = str(input('O Brasil vai ganhar? \nResponda com sim ou não! '))
    if bganhar == 'sim':
        bganhars = bganhars+1
    if bganhar == 'não':
        bganharn = bganharn+1

    print(100 / geracaoxn, 'sao da geração X', 100 / geracaoyn, 'sao da geração Y')
