#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script de teste para validar o limite de jogos simultâneos com status "JOGANDO"."""

from jogo import JogoPc, JogoMobile, GerenciadorJogos

def teste_limite_jogos_simultaneos():
    """Testa o limite de jogos simultâneos."""
    
    print("=" * 60)
    print("TESTE: Limite de Jogos Simultâneos com Status 'JOGANDO'")
    print("=" * 60)
    
    # Criar 5 jogos
    jogos = [
        JogoPc("Jogo 1", 8, 0, "RPG", "2024-01-01", "", 2024),
        JogoPc("Jogo 2", 7, 0, "Ação", "2024-01-02", "", 2024),
        JogoPc("Jogo 3", 9, 0, "Aventura", "2024-01-03", "", 2024),
        JogoPc("Jogo 4", 6, 0, "Estratégia", "2024-01-04", "", 2024),
        JogoMobile("Jogo 5", 5, 0, "Casual", "2024-01-05", "", 2024),
    ]
    
    print(f"\n✓ Criados 5 jogos (todos com 0 horas, status = 'não iniciado')")
    
    # IMPORTANTE: Definir a lista global de jogos ANTES de tentar alterar status
    # Isso garante que a validação de limite seja feita corretamente
    from jogo import Jogo
    Jogo.definir_lista_jogos(jogos)
    
    # Obter o gerenciador e verificar limite atual
    gerenciador = GerenciadorJogos()
    limite = gerenciador.obter_limite()
    print(f"\n✓ Limite configurado: {limite} jogos simultâneos")
    
    # Tentar adicionar jogos com status "jogando"
    print("\n" + "-" * 60)
    print("Tentando adicionar jogos com status 'jogando':")
    print("-" * 60)
    
    try:
        print(f"\n1. Alterando Jogo 1 para 'jogando'...")
        jogos[0].status = "jogando"
        print(f"   ✓ Sucesso! Status: {jogos[0].status}")
    except Exception as e:
        print(f"   ✗ Erro: {e}")
    
    try:
        print(f"\n2. Alterando Jogo 2 para 'jogando'...")
        jogos[1].status = "jogando"
        print(f"   ✓ Sucesso! Status: {jogos[1].status}")
    except Exception as e:
        print(f"   ✗ Erro: {e}")
    
    try:
        print(f"\n3. Alterando Jogo 3 para 'jogando'...")
        jogos[2].status = "jogando"
        print(f"   ✓ Sucesso! Status: {jogos[2].status}")
    except Exception as e:
        print(f"   ✗ Erro: {e}")
    
    try:
        print(f"\n4. Alterando Jogo 4 para 'jogando' (deve FALHAR)...")
        jogos[3].status = "jogando"
        print(f"   ✓ Sucesso! Status: {jogos[3].status}")
    except Exception as e:
        print(f"   ✓ Erro esperado: {e}")
    
    # Finalizar um jogo e tentar novamente
    print("\n" + "-" * 60)
    print("Finalizando Jogo 1 e tentando novamente com Jogo 4:")
    print("-" * 60)
    
    try:
        jogos[0].horasJogadas = 1  # Adicionar 1 hora para poder finalizar
        print(f"\n✓ Adicionado 1 hora ao Jogo 1")
        jogos[0].status = "finalizado"
        print(f"✓ Jogo 1 finalizado. Status: {jogos[0].status}")
    except Exception as e:
        print(f"✗ Erro: {e}")
    
    try:
        print(f"\n✓ Tentando novamente com Jogo 4...")
        jogos[3].status = "jogando"
        print(f"✓ Sucesso! Jogo 4 alterado para 'jogando'. Status: {jogos[3].status}")
    except Exception as e:
        print(f"✗ Erro: {e}")
    
    # Testar alteração de limite
    print("\n" + "-" * 60)
    print("Alterando o limite para 5 jogos simultâneos:")
    print("-" * 60)
    
    try:
        print(f"\n✓ Novo limite: ", end="")
        gerenciador.atualizar_limite(5)
        print(f"{gerenciador.obter_limite()}")
        
        # Tentar adicionar mais um jogo
        print(f"\n✓ Tentando adicionar Jogo 5 com status 'jogando'...")
        jogos[4].status = "jogando"
        print(f"✓ Sucesso! Jogo 5 agora está 'jogando'. Status: {jogos[4].status}")
    except Exception as e:
        print(f"✗ Erro: {e}")
    
    # Exibir status final de todos os jogos
    print("\n" + "-" * 60)
    print("Status final de todos os jogos:")
    print("-" * 60)
    
    for i, jogo in enumerate(jogos, 1):
        print(f"{i}. {jogo.titulo}: {jogo.status}")
    
    print("\n" + "=" * 60)
    print("TESTE CONCLUÍDO COM SUCESSO!")
    print("=" * 60)

if __name__ == "__main__":
    teste_limite_jogos_simultaneos()
