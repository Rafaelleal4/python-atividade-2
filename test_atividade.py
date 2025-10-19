"""
Script de teste automatizado para validar todas as funcionalidades
"""

# Simular o ambiente do programa
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

print("=" * 60)
print("TESTANDO TODAS AS FUNCIONALIDADES")
print("=" * 60)

# Teste 1: Criar playlist nova
print("\n[TESTE 1] Criar playlist nova 'Jazz'")
nome = "Jazz"
if nome == "":
    print("❌ Digite o nome corretamente")
elif nome in playlists:
    print("❌ Já existe uma playlist com esse nome")
else:
    playlists[nome] = []
    print(f"✓ A playlist: {nome} foi criada com sucesso!!")

# Teste 2: Tentar criar playlist duplicada
print("\n[TESTE 2] Tentar criar playlist duplicada 'Rock'")
nome = "Rock"
if nome == "":
    print("❌ Digite o nome corretamente")
elif nome in playlists:
    print("✓ Já existe uma playlist com esse nome (validação OK)")
else:
    playlists[nome] = []
    print(f"❌ A playlist: {nome} foi criada com sucesso!!")

# Teste 3: Adicionar música válida
print("\n[TESTE 3] Adicionar música válida à playlist 'Jazz'")
nome = "Jazz"
nome_Musica = "Take Five"
nome_Artista = "Dave Brubeck"
duracao = 5.24
if nome == '':
    print("❌ Escreva um nome válido")
elif nome in playlists:
    if nome_Musica == '' or nome_Artista == '':
        print("❌ Nome da música e Artista são obrigatórios")
    else:
        if duracao <= 0:
            print("❌ A duração da música deve ser maior que 0")
        else:
            playlists[nome].append((nome_Musica, nome_Artista, duracao))
            print(f"✓ Música:'{nome_Musica}' de {nome_Artista} com duração de {duracao} min foi adicionada á playlist {nome}!!")
else:
    print("❌ Playlist não encontrada")

# Teste 4: Adicionar música com duração inválida
print("\n[TESTE 4] Tentar adicionar música com duração negativa")
nome = "Jazz"
nome_Musica = "Test Song"
nome_Artista = "Test Artist"
duracao = -1.5
if duracao <= 0:
    print("✓ A duração da música deve ser maior que 0 (validação OK)")
else:
    playlists[nome].append((nome_Musica, nome_Artista, duracao))
    print(f"❌ Música inválida foi adicionada!")

# Teste 5: Remover música existente
print("\n[TESTE 5] Remover música 'Stronger' da playlist 'Treino'")
nome = "Treino"
nome_Musica = "Stronger"
encontrou = False
if nome == '':
    print("❌ Escreva um nome válido")
elif nome in playlists:
    if nome_Musica == '':
        print("❌ O nome da música é obrigatório")
    else:
        for musica in playlists[nome]:
            if musica[0] == nome_Musica:
                playlists[nome].remove(musica)
                print(f"✓ Música {nome_Musica} foi removida com sucesso da playlist {nome}")
                encontrou = True
                break
        if not encontrou:
            print(f"❌ Música {nome_Musica} não encontrada")
else:
    print("❌ Playlist não encontrada")

# Teste 6: Tentar remover música inexistente
print("\n[TESTE 6] Tentar remover música inexistente 'XYZ' da playlist 'Rock'")
nome = "Rock"
nome_Musica = "XYZ"
encontrou = False
if nome in playlists:
    for musica in playlists[nome]:
        if musica[0] == nome_Musica:
            playlists[nome].remove(musica)
            print(f"❌ Música {nome_Musica} foi removida (não deveria existir!)")
            encontrou = True
            break
    if not encontrou:
        print(f"✓ Música {nome_Musica} não encontrada (comportamento correto, mas sem feedback ao usuário)")

# Teste 7: Listar músicas de playlist com conteúdo
print("\n[TESTE 7] Listar músicas da playlist 'Rock'")
nome = "Rock"
if nome == '':
    print("❌ Escreva um nome válido")
elif nome in playlists:
    musicas = playlists[nome]
    if not musicas:
        print("❌ Não há músicas nessa playlist")
    else:
        print(f"✓ Playlist: {nome} ({len(musicas)} música(s))")
        indice = 1
        for musica in musicas:
            titulo, artista, duracao = musica
            print(f"  {indice}. {titulo} — {artista} ({duracao} min)")
            indice += 1
else:
    print("❌ Playlist não encontrada")

# Teste 8: Listar músicas de playlist vazia
print("\n[TESTE 8] Listar músicas da playlist vazia 'Jazz' (após remover)")
playlists["Jazz"] = []  # Esvaziar para testar
nome = "Jazz"
if nome in playlists:
    musicas = playlists[nome]
    if not musicas:
        print("✓ Não há músicas nessa playlist (validação OK)")
    else:
        print(f"❌ Playlist deveria estar vazia")

# Teste 9: Buscar por palavra-chave encontrada
print("\n[TESTE 9] Buscar músicas com palavra-chave 'queen'")
palavra = "queen"
resultados = 0
for chave in playlists:
    musicas = playlists[chave]
    for musica in musicas:
        titulo, artista, duracao = musica
        if palavra in titulo.lower() or palavra in artista.lower():
            print(f"✓ Playlist: {chave} — {titulo} de {artista} ({duracao} min)")
            resultados += 1
if resultados == 0:
    print("❌ Nenhuma música encontrada com essa palavra-chave")
else:
    print(f"✓ Total: {resultados} resultado(s)")

# Teste 10: Buscar por palavra-chave não encontrada
print("\n[TESTE 10] Buscar músicas com palavra-chave inexistente 'xyzabc'")
palavra = "xyzabc"
resultados = 0
for chave in playlists:
    musicas = playlists[chave]
    for musica in musicas:
        titulo, artista, duracao = musica
        if palavra in titulo.lower() or palavra in artista.lower():
            print(f"❌ Encontrou resultado que não deveria: {titulo}")
            resultados += 1
if resultados == 0:
    print("✓ Nenhuma música encontrada com essa palavra-chave (comportamento correto)")

# Teste 11: Buscar parcial
print("\n[TESTE 11] Buscar músicas com palavra-chave parcial 'light'")
palavra = "light"
resultados = 0
for chave in playlists:
    musicas = playlists[chave]
    for musica in musicas:
        titulo, artista, duracao = musica
        if palavra in titulo.lower() or palavra in artista.lower():
            print(f"✓ Playlist: {chave} — {titulo} de {artista} ({duracao} min)")
            resultados += 1
if resultados == 0:
    print("❌ Nenhuma música encontrada")
else:
    print(f"✓ Total: {resultados} resultado(s)")

print("\n" + "=" * 60)
print("RESUMO DO ESTADO FINAL DAS PLAYLISTS")
print("=" * 60)
for nome_playlist, lista_musicas in playlists.items():
    print(f"\n{nome_playlist}: {len(lista_musicas)} música(s)")
    for idx, musica in enumerate(lista_musicas, 1):
        print(f"  {idx}. {musica[0]} — {musica[1]} ({musica[2]} min)")

print("\n" + "=" * 60)
print("TESTES CONCLUÍDOS")
print("=" * 60)
