playlists = {
    "Rock": [
        ("Lose Yourself", "Eminem", 5.26),
        ("Bohemian Rhapsody", "Queen", 5.55),
        ("Stairway to Heaven", "Led Zeppelin", 8.02)
    ],
    "Pop": [
        ("Blinding Lights", "The Weeknd", 3.20),
        ("Levitating", "Dua Lipa", 3.23),
        ("Shape of You", "Ed Sheeran", 3.53)
    ],
    "Treino": [
        ("Eye of the Tiger", "Survivor", 4.05),
        ("Stronger", "Kanye West", 5.12)
    ]
}

def menu() :
    print('Bem Vindo a sua playlist de músicas!')
    print('1 - Criar uma playlist')
    print('2 - Adicionar uma música a uma playlist')
    print('3 - Remover uma música de uma playlist')
    print('4 - Listar todas as músicas de uma playlist')
    print('5 - Buscar músicas por palavra-chave')
    print('6 - Exibir estatísticas musicais')
    print('7 - Encerrar o programa')

def opcaoValida():
    while True:
        escolha = input('Escolha um valor entre 1 - 7: ').strip()
        try:
            opcao = int(escolha)
            if 1 <= opcao <= 7:
                return opcao
            else:
                print('Escolha uma opção válida')
                menu()
        except ValueError:
            print('Entrada inválida. Escolha um número entre 1 - 7')

while True:
    menu()
    opcao = opcaoValida()
    if opcao == 7:
        print('Programa Encerrado')
        break

    #Opção 1: Criar uma playlist
    if opcao == 1:
        nome = input('Informe o nome da playlist que deseja criar: ' ).strip()
        if nome == "":
            print('Digite o nome corretamente')
        elif nome in playlists:
            print('Já existe uma playlist com esse nome')
        else:
            playlists[nome] = []
            print(f' A playlist: {nome} foi criada com sucesso!!')

                
    #Opção 2: Adicionar uma música a uma playlist
    elif opcao == 2:
        nome = input('Informe o nome da playlist em que deseja adicionar a música: ').strip()
        if nome == '':
            print('Escreva um nome válido')
        elif nome in playlists:
            nome_Musica = input('Informe o nome da música: ').strip()
            nome_Artista = input('Informe o nome do Artista: ').strip()
            if nome_Musica == '' or nome_Artista == '':
                print('Nome da música e Artista são obrigatórios')
            else:
                texto_Duracao = input('Informa a duração da música: ').strip().replace(',', '.')
                try:
                    duracao = float(texto_Duracao)
                    if duracao <= 0:
                        print('A duração da música deve ser maior que 0')
                    else:
                        playlists[nome].append((nome_Musica, nome_Artista, duracao))
                        print(f"Música:'{nome_Musica}' de {nome_Artista} com duração de {duracao} min foi adicionada á playlist {nome}!!")
                except ValueError:
                    print('Duraçao inválida. Digite um número (ex: 3.5).')        
        else:
            print('Playlist não encontrada')
    
    #Opção 3: Remover uma Música de uma Playlist
    elif opcao == 3:
        nome = input('Informe o nome da playlist em que deseja remover a música: ').strip()
        if nome == '':
            print('Escreva um nome válido')
        elif nome in playlists:
            nome_Musica = input('Informe o nome da música: ').strip()
            if nome_Musica == '':
                print('O nome da música é obrigatório')
            else:
                encontrada = False
                for musica in playlists[nome]:
                    if musica[0] == nome_Musica:
                        playlists[nome].remove(musica)
                        print(f'Música {nome_Musica} foi removida com sucesso da playlist {nome}')
                        encontrada = True
                        break
                if not encontrada:
                    print(f"Música {nome_Musica} não encontrada na playlist {nome}")
        else:
            print('Playlist não encontrada')

    #Opção 4: Listar todas as músicas de uma playlist
    elif opcao == 4:
        nome = input('Informe o nome da playlist em que deseja listar as músicas: ').strip()
        if nome == '':
            print('Escreva um nome válido')
        elif nome in playlists:
            musicas = playlists[nome]
            if not musicas:
                print('Não há músicas nessa playlist')
            else:
                print(f'Playlist: {nome} ({len(musicas)} música(s))')
                indice = 1
                for musica in musicas:
                    titulo, artista, duracao = musica
                    print(f"{indice}. {titulo} — {artista} ({duracao} min)")
                    indice += 1
        else:
            print('Playlist não encontrada')
        
    #Opção 5: Buscar músicas por palavra chave
    elif opcao == 5:
        palavra = input('Informe a palavra_chave para encontrar a música: ').strip().lower()
        if palavra == '':
            print('Escreva uma palavra válida')
        else:
            resultados = 0
            for chave in playlists:
                musicas = playlists[chave]
                for musica in musicas:
                    titulo, artista, duracao = musica
                    if palavra in titulo.lower() or palavra in artista.lower():
                        print(f'Playlist: {chave} — {titulo} de {artista} ({duracao} min)')
                        resultados += 1
            if resultados == 0:
                print('Nenhuma música encontrada com essa palavra-chave')

