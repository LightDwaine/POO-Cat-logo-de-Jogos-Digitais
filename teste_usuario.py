#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Teste da classe Usuario com múltiplas coleções de jogos"""

from usuario import Usuario
from jogo import JogoPc, JogoMobile, JogoConsole

def teste_usuario_com_colecoes():
    """Testa usuário criando e gerenciando múltiplas coleções"""
    print("\n" + "="*70)
    print("TESTE: Usuário com Múltiplas Coleções")
    print("="*70)
    
    # Criar usuário
    print("\n1. Criando usuário...")
    usuario = Usuario(1, "Ryan")
    print(f"   ✅ Usuário criado: {usuario}")
    
    # Login
    print("\n2. Fazendo login...")
    usuario.login("192.168.1.100", 8080)
    
    # Criar coleções
    print("\n3. Criando coleções...")
    usuario.criar_colecao("RPGs Favoritos")
    usuario.criar_colecao("Jogos Mobile")
    usuario.criar_colecao("Backlog")
    
    # Tentar criar coleção duplicada
    print("\n4. Tentando criar coleção duplicada...")
    usuario.criar_colecao("RPGs Favoritos")
    
    # Listar coleções vazias
    print("\n5. Listando coleções (vazias)...")
    usuario.listar_colecoes()
    
    # Criar jogos
    print("\n6. Criando jogos...")
    jogo1 = JogoPc("The Witcher 3", 0, 0, "RPG", "2024-01-01", "", 2015)
    jogo2 = JogoPc("Elden Ring", 0, 0, "RPG", "2024-01-05", "", 2022)
    jogo3 = JogoMobile("Genshin Impact", 0, 0, "RPG", "2024-02-01", "", 2020)
    jogo4 = JogoMobile("Clash of Clans", 0, 0, "Estratégia", "2024-02-05", "", 2012)
    jogo5 = JogoPc("Cyberpunk 2077", 0, 0, "RPG", "2024-03-01", "", 2020)
    jogo6 = JogoConsole("Zelda: TOTK", 0, 0, "Aventura", "2024-03-05", "", 2023)
    print("   ✅ 6 jogos criados")
    
    # Adicionar jogos às coleções
    print("\n7. Adicionando jogos às coleções...")
    usuario.adicionar_jogo_colecao("RPGs Favoritos", jogo1)
    usuario.adicionar_jogo_colecao("RPGs Favoritos", jogo2)
    usuario.adicionar_jogo_colecao("RPGs Favoritos", jogo5)
    
    usuario.adicionar_jogo_colecao("Jogos Mobile", jogo3)
    usuario.adicionar_jogo_colecao("Jogos Mobile", jogo4)
    
    usuario.adicionar_jogo_colecao("Backlog", jogo6)
    
    # Listar coleções com jogos
    print("\n8. Listando coleções...")
    usuario.listar_colecoes()
    
    # Listar jogos de uma coleção específica
    print("\n9. Listando jogos da coleção 'RPGs Favoritos'...")
    usuario.listar_jogos_colecao("RPGs Favoritos")
    
    # Finalizar alguns jogos
    print("\n10. Finalizando alguns jogos...")
    jogo1.horasJogadas = 120
    jogo1.status = "finalizado"
    jogo1.nota = 10
    
    jogo3.horasJogadas = 50
    jogo3.status = "finalizado"
    jogo3.nota = 9
    print("   ✅ 2 jogos finalizados")
    
    # Ver estatísticas do usuário
    print("\n11. Estatísticas do usuário...")
    print(f"   Total de jogos: {usuario.total_jogos()}")
    print(f"   Total finalizados: {usuario.total_finalizados()}")
    print(f"   Info: {usuario}")
    
    # Remover um jogo
    print("\n12. Removendo um jogo da coleção 'Backlog'...")
    usuario.remover_jogo_colecao("Backlog", "Zelda: TOTK", "Console")
    
    # Listar novamente
    print("\n13. Listando coleções atualizadas...")
    usuario.listar_colecoes()
    
    # Remover uma coleção
    print("\n14. Removendo coleção 'Backlog'...")
    usuario.remover_colecao("Backlog")
    
    # Listagem final
    print("\n15. Listagem final de coleções...")
    usuario.listar_colecoes()
    
    # Logout
    print("\n16. Fazendo logout...")
    usuario.logout()
    print(f"   Status final: {usuario}")
    
    print("\n" + "="*70)
    print("✅ TESTE CONCLUÍDO COM SUCESSO!")
    print("="*70 + "\n")


def teste_multiplos_usuarios():
    """Testa múltiplos usuários com coleções separadas"""
    print("\n" + "="*70)
    print("TESTE: Múltiplos Usuários com Coleções Separadas")
    print("="*70)
    
    # Criar usuários
    print("\n1. Criando usuários...")
    usuario1 = Usuario(1, "Ryan")
    usuario2 = Usuario(2, "Maria")
    usuario3 = Usuario(3, "João")
    print("   ✅ 3 usuários criados")
    
    # Cada um cria suas coleções
    print("\n2. Cada usuário criando suas coleções...")
    usuario1.criar_colecao("RPGs")
    usuario1.criar_colecao("Ação")
    
    usuario2.criar_colecao("Indie")
    usuario2.criar_colecao("Puzzle")
    usuario2.criar_colecao("Aventura")
    
    usuario3.criar_colecao("FPS")
    
    # Adicionar alguns jogos
    print("\n3. Adicionando jogos...")
    usuario1.adicionar_jogo_colecao("RPGs", JogoPc("Skyrim", 0, 0, "RPG", "", "", 2011))
    usuario1.adicionar_jogo_colecao("RPGs", JogoPc("Fallout 4", 0, 0, "RPG", "", "", 2015))
    
    usuario2.adicionar_jogo_colecao("Indie", JogoPc("Hollow Knight", 0, 0, "Metroidvania", "", "", 2017))
    usuario2.adicionar_jogo_colecao("Puzzle", JogoPc("Portal 2", 0, 0, "Puzzle", "", "", 2011))
    
    usuario3.adicionar_jogo_colecao("FPS", JogoPc("CS:GO", 0, 0, "FPS", "", "", 2012))
    
    # Listar coleções de cada usuário
    print("\n4. Listando coleções de cada usuário...")
    usuario1.listar_colecoes()
    usuario2.listar_colecoes()
    usuario3.listar_colecoes()
    
    print("="*70)
    print("✅ TESTE DE MÚLTIPLOS USUÁRIOS CONCLUÍDO!")
    print("="*70 + "\n")


if __name__ == "__main__":
    teste_usuario_com_colecoes()
    teste_multiplos_usuarios()
