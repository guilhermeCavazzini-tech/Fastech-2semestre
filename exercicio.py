if 1 == 1:
    geracaoxn = 0
    geracaoyn = 0
    geracaozn = 0
    pfutebol = 0
    pfutebols = 0
    pfuteboln = 0
    bganhars = 0
    bganharn = 0
    sexom = 0
    sexof = 0
    sexo = 0
    np = 1
    p = 'S'
for x in range(np):
    while p == 'SIM' or p == 'S':
        geracao = str(input('Qual sua geração: X Y ou Z ? ')).upper()
        if geracao == 'X':
            geracaoxn = geracaoxn + 1
        if geracao == 'Y':
            geracaoyn = geracaoyn + 1
        if geracao == 'Z':
            geracaozn = geracaozn + 1

        print('\n')

        sexo = (input('Seu sexo é masculino ou feminino? ')).upper()
        if sexo == 'M' or sexo == 'MASCULINO':
            sexom = sexof + 1
        if sexo == 'F' or sexo == 'FEMININO':
            sexof = sexof + 1
        print('\n')

        pfutebol = str(input('Pratica ou já praticou futebol?\nResponda com sim ou não! ')).upper()
        if pfutebol == 'SIM' or pfutebol == 'S':
            pfutebols = pfutebols + 1
        if pfutebol == 'NÃO' or pfutebol == 'N' or pfutebol == 'NAO':
            pfuteboln = pfuteboln + 1
        print('\n')

        bganhar = str(input('O Brasil vai ganhar? \nResponda com sim ou não! ')).upper()
        if bganhar == 'SIM' or bganhar == 'S':
            bganhars = bganhars + 1
        if bganhar == 'NÃO' or bganhar == 'N' or bganhar == 'NAO':
            bganharn = bganharn + 1

        print('\n')
        p = input('fazer mais uma pesquisa?').upper()
        if p == 'SIM' or p == 'S':
            np = np + 1
            print('\n')
        if p == 'NÃO' or p == 'N' or p == "NAO":
            print('\n')
if 1 == 1:
    print('\n')
    print('O numero total de pessoas que fizeram a pesquisa foi:', np)
    print(('-----' * 32))
    print('geração X: ', (100 / np) * geracaoxn, '%')
    print('\ngeração Y: ', (100 / np) * geracaoyn, '%')
    print('\ngeração Z: ', (100 / np) * geracaozn, '%')
    print('-----' * 32)
    print('Sexo masculino:', (100 / np) * sexom, '%' '\nSexo feminino:', (100 / np) * sexof, '%')
    print(('-----' * 32))
    print(f'Já praticou futebol: \nsim:', (100 / np) * pfutebols, '%' '\nnão:', (100 / np) * pfuteboln, '%')
    print(('-----' * 32))
    print(f'O Brasil vai ganhar? \nsim:', (100 / np) * bganhars, '%' '\nnão:', (100 / np) * bganharn, '%')
    print(('-----' * 32))
