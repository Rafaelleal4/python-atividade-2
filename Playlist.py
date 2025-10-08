
playlists = [
    {
        "nome": "Rock Clássico",
        "musicas": [
            ("Bohemian Rhapsody", "Queen", 5.55),
            ("Stairway to Heaven", "Led Zeppelin", 8.02),
            ("Hotel California", "Eagles", 6.30),
            
        ]
    },
    {
        "nome": "Pop Hits",
        "musicas": [
            ("Blinding Lights", "The Weeknd", 3.20),
            ("Shape of You", "Ed Sheeran", 3.53),
            ("Levitating", "Dua Lipa", 3.23)
        ]
    },
    {
        "nome": "MPB Favoritas",
        "musicas": [
            ("Aquarela do Brasil", "João Gilberto", 4.15),
            ("Tocando em Frente", "Almir Sater", 4.40),
            ("Pais e Filhos", "Legião Urbana", 5.06)
        ]
    },
    {
        "nome": "Eletrônica",
        "musicas": [
            ("Titanium", "David Guetta", 4.05),
            ("Wake Me Up", "Avicii", 4.09),
            ("Animals", "Martin Garrix", 5.03)
        ]
    }
]

print("Seja bem-vindo à sua playlist de músicas!")
print("Escolha uma opção:")
print("1 - Criar uma nova playlist")
print("2 - Adicionar músicas a uma playlist existente")
print("3 - Remover músicas de uma playlist")
print("4 - Listar músicas de uma playlist")
print("5 - Buscar músicas por palavra-chave")
print("6 - Exibir estatísticas musicais")
print("7 - Encerrar o programa")

opcao = input("Digite a opção (1-7): ").strip()

while opcao != "7":
    if opcao == "1":
        nome_playlist = input("Digite o nome da nova playlist:").strip()
        if nome_playlist == "":
            print("Nome de playlist inválido.")
        else:
            playlists.append({"nome": nome_playlist, "musicas": []})
            print(f"Playlist '{nome_playlist}' criada com sucesso!")

    elif opcao == "2":
        nome_playlist = input("Digite o nome da playlist onde deseja adicionar músicas:").strip()
        encontrada = None
        for playlist in playlists:
            if playlist.get("nome") == nome_playlist:
                encontrada = playlist
                break
        if encontrada is None:
            print(f"Playlist '{nome_playlist}' não encontrada.")
        else:
            titulo = input("Informe o título da música:").strip()
            if titulo == "":
                print("Título inválido.")
            else:
                artista = input("Informe o artista da música:").strip()
                if artista == "":
                    print("Artista inválido.")
                else:
                    duracao_str = input("Informe a duração da música em minutos (ex: 3.5) ou deixe vazio:").strip()
                    if duracao_str == "":
                        duracao = None
                    else:
                        try:
                            duracao = float(duracao_str)
                            if duracao < 0:
                                print("Duração inválida; registrada como desconhecida.")
                                duracao = None
                        except ValueError:
                            print("Duração inválida; registrada como desconhecida.")
                            duracao = None
                    encontrada["musicas"].append((titulo, artista, duracao))
                    dur_display = f"{duracao} min" if duracao is not None else "desconhecida"
                    print(f"Música '{titulo}' - {artista} ({dur_display}) adicionada à playlist '{nome_playlist}'.")

    elif opcao == "3":
        nome_playlist = input("Digite o nome da playlist de onde deseja remover músicas:").strip()
        encontrada = None
        for playlist in playlists:
            if playlist.get("nome") == nome_playlist:
                encontrada = playlist
                break
        if encontrada is None:
            print(f"Playlist '{nome_playlist}' não encontrada.")
        else:
            titulo = input("Informe o título da música a ser removida:").strip()
            artista = input("Informe o artista da música a ser removida:").strip()
            achou = False
            for musica in encontrada["musicas"]:
                if musica[0] == titulo and musica[1] == artista:
                    encontrada["musicas"].remove(musica)
                    print(f"Música '{titulo}' - {artista} removida da playlist '{nome_playlist}'.")
                    achou = True
                    break
            if not achou:
                print(f"Música '{titulo}' - {artista} não encontrada na playlist '{nome_playlist}'.")

    elif opcao == "4":
        nome_playlist = input("Digite o nome da playlist que deseja listar as músicas:").strip()
        encontrada = None
        for playlist in playlists:
            if playlist.get("nome") == nome_playlist:
                encontrada = playlist
                break
        if encontrada is None:
            print(f"Playlist '{nome_playlist}' não encontrada.")
        else:
            if len(encontrada["musicas"]) == 0:
                print(f"A playlist '{nome_playlist}' está vazia.")
            else:
                print(f"Músicas na playlist '{nome_playlist}':")
                indice = 1
                for musica in encontrada["musicas"]:
                    titulo, artista, duracao = musica
                    dur_display = f"{duracao} min" if duracao is not None else "desconhecida"
                    print(f"{indice}. '{titulo}' - {artista} ({dur_display})")
                    indice += 1

    elif opcao == "5":
        palavra = input("Digite a palavra-chave para buscar músicas:").strip().lower()
        resultados = []
        for playlist in playlists:
            for musica in playlist["musicas"]:
                titulo, artista, duracao = musica
                if palavra in titulo.lower() or palavra in artista.lower():
                    resultados.append((playlist["nome"], titulo, artista, duracao))
        if len(resultados) == 0:
            print("Nenhuma música encontrada com a palavra-chave fornecida.")
        else:
            print("Músicas encontradas:")
            idx = 1
            for resultado in resultados:
                nome_pl, titulo, artista, duracao = resultado
                dur_display = f"{duracao} min" if duracao is not None else "desconhecida"
                print(f"{idx}. '{titulo}' - {artista} ({dur_display}) na playlist '{nome_pl}'")
                idx += 1
    
    else:
        print("Opção inválida. Tente novamente.")

    # reexibir o menu completo a cada iteração antes de pedir a opção
    print("Escolha outra opção:")
    print("1 - Criar uma nova playlist")
    print("2 - Adicionar músicas a uma playlist existente")
    print("3 - Remover músicas de uma playlist")
    print("4 - Listar músicas de uma playlist")
    print("5 - Buscar músicas por palavra-chave")
    print("6 - Exibir estatísticas musicais")
    print("7 - Encerrar o programa")
    opcao = input("Digite a opção (1-7): ").strip()

print("Encerrando. Até mais!")

