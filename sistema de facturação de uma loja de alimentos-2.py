while True:
    nomeCli = str(input('digite o nome do cliente: '))
    genero = str(input('informe o genero do cliente[M/F]: ')).strip().upper()
    while genero != 'M' and genero != 'F':
        print('Erro! digite apenas M ou F')  
        genero = str(input('informe o genero do cliente[M/F]: ')).strip().upper()
    Valcompra = int(input('digite o valor total da compra (kz): '))
    if Valcompra > 100000:
        bonus = Valcompra * 0.10
    else:
        bonus = 0
    total_pagar = Valcompra - bonus
    print('=============== prioridade ==================\n')
    gravida = 'N'
    if genero == 'F':
        gravida = str(input('cliente está gravida? [S/N]: ')).strip().upper()
        while gravida != 'S' and gravida != 'N':
            print('Erro! digite penas S ou N.')
            gravida = str(input('cliente está gravida? [S/N]: ')).strip().upper()

    idoso = str(input('cliente é idoso (60+ anos)? [S/N]: ')).strip().upper()
    while idoso != 'S' and idoso != 'N':
        print('Erro! digite penas S ou N.')
        idoso = str(input('cliente é idoso (60+ anos)? [S/N]: ')).strip().upper()

    dificiente = str(input('cliente é dificiente? [S/N]: ')).strip().upper()
    while dificiente != 'S' and dificiente != 'N':
        print('Erro! digite penas S ou N.')
        dificiente = str(input('cliente é dificiente? [S/N]: ')).strip().upper()

    if gravida == 'S' or idoso == 'S' or dificiente == 'S':
        prioridade = 'SIM'
    else:
        prioridade = 'NÃO'
    print('============= Factura ================')
    print(f'O nome do cliente é: {nomeCli} o seu genero é {genero}')
    print(f'O valor da compra é: {Valcompra}(kz) e bonus da compra é: {bonus}(kz)')
    print(f'O total pago é: {total_pagar}(kz)')
    print(f'Tem prioridade no atendimento:  {prioridade}')
    continuar = True
    while continuar:
        resposta = str(input('Registrar outro cliente? [S/N]: ')).strip().upper()
        if resposta == 'S':
            break
        elif resposta == 'N':
            print('Programa Encerrado. Obrigado.')
            continuar = false
        else:
            print('Erro digite apenas S ou N.')





