#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de uso da restrição de limite de jogos simultâneos com status "JOGANDO".

Este arquivo demonstra como usar a classe GerenciadorJogos para:
1. Verificar o limite configurado
2. Tentar alterar o status de jogos para "jogando"
3. Validar que o limite é respeitado
4. Alterar o limite dinamicamente
"""

from jogo import JogoPc, JogoMobile, JogoConsole, GerenciadorJogos, Jogo

def exemplo_basico():
    """Exemplo básico de uso do limite de jogos simultâneos."""
    
    print("\n" + "="*70)
    print("EXEMPLO: Restrição de Limite de Jogos Simultâneos")
    print("="*70)
    
    # 1. Criar alguns jogos
    print("\n1. Criando 4 jogos...")
    jogos = [
        JogoPc("The Witcher 3", 10, 0, "RPG", "2024-01-01", "", 2015),
        JogoPc("Elden Ring", 9, 0, "Ação-RPG", "2024-01-05", "", 2022),
        JogoConsole("Zelda: Tears of the Kingdom", 10, 0, "Aventura", "2024-02-01", "", 2023),
        JogoMobile("Genshin Impact", 8, 0, "RPG", "2024-02-10", "", 2020),
    ]
    
    for jogo in jogos:
        print(f"   ✓ {jogo.titulo}")
    
    # 2. IMPORTANTE: Definir a lista global de jogos para validação
    print("\n2. Registrando a lista de jogos para validação...")
    Jogo.definir_lista_jogos(jogos)
    print("   ✓ Lista registrada")
    
    # 3. Obter o gerenciador e verificar limite
    print("\n3. Verificando limite configurado...")
    gerenciador = GerenciadorJogos()
    limite = gerenciador.obter_limite()
    print(f"   ✓ Limite atual: {limite} jogos simultâneos com status 'JOGANDO'")
    
    # 4. Tentar alterar status de jogos
    print("\n4. Alterando status de jogos para 'JOGANDO'...")
    
    for i, jogo in enumerate(jogos[:3], 1):
        try:
            jogo.status = "jogando"
            print(f"   ✓ {i}. {jogo.titulo}: {jogo.status}")
        except Exception as e:
            print(f"   ✗ {i}. {jogo.titulo}: {e}")
    
    # 5. Tentar adicionar um 4º jogo (deve falhar)
    print(f"\n5. Tentando adicionar um 4º jogo (deve falhar)...")
    try:
        jogos[3].status = "jogando"
        print(f"   ✗ {jogos[3].titulo}: {jogos[3].status}")
    except Exception as e:
        print(f"   ✓ {jogos[3].titulo}: Bloqueado!")
        print(f"      Motivo: {e}")
    
    # 6. Liberar um slot finalizando um jogo
    print(f"\n6. Finalizando um jogo para liberar um slot...")
    try:
        # Adicionar horas para poder finalizar
        jogos[0].horasJogadas = 50
        jogos[0].status = "finalizado"
        print(f"   ✓ {jogos[0].titulo}: {jogos[0].status}")
    except Exception as e:
        print(f"   ✗ Erro: {e}")
    
    # 7. Agora tentar adicionar o 4º jogo novamente
    print(f"\n7. Tentando novamente com o 4º jogo...")
    try:
        jogos[3].status = "jogando"
        print(f"   ✓ {jogos[3].titulo}: {jogos[3].status}")
    except Exception as e:
        print(f"   ✗ Erro: {e}")
    
    # 8. Demonstrar alteração de limite
    print(f"\n8. Alterando o limite para 5 jogos simultâneos...")
    try:
        gerenciador.atualizar_limite(5)
        novo_limite = gerenciador.obter_limite()
        print(f"   ✓ Novo limite: {novo_limite} jogos simultâneos")
        
        # Adicionar jogos[0] de volta
        jogos[0].status = "jogando"
        print(f"   ✓ {jogos[0].titulo} agora pode ser jogado novamente")
    except Exception as e:
        print(f"   ✗ Erro: {e}")
    
    # 9. Exibir status final
    print(f"\n9. Status final de todos os jogos:")
    for jogo in jogos:
        print(f"   • {jogo.titulo}: {jogo.status}")
    
    print("\n" + "="*70)
    print("Limite máximo de jogos simultâneos implementado com sucesso!")
    print("="*70 + "\n")


def exemplo_configuracao():
    """Exemplo de como configurar o limite dinamicamente."""
    
    print("\n" + "="*70)
    print("EXEMPLO: Configuração Dinâmica do Limite")
    print("="*70)
    
    gerenciador = GerenciadorJogos()
    
    # Tentar diferentes limites
    limites_para_testar = [2, 3, 5, 10]
    
    print("\nTestando diferentes limites:")
    for limite in limites_para_testar:
        try:
            gerenciador.atualizar_limite(limite)
            print(f"   ✓ Limite atualizado para: {limite}")
        except ValueError as e:
            print(f"   ✗ Erro: {e}")
    
    # Testar limite inválido
    print("\nTentando definir um limite inválido (0):")
    try:
        gerenciador.atualizar_limite(0)
        print(f"   ✗ Limite inválido aceito (ERRO!)")
    except ValueError as e:
        print(f"   ✓ Erro esperado: {e}")
    
    # Restaurar limite original
    print("\nRestaurando limite padrão (3):")
    gerenciador.atualizar_limite(3)
    print(f"   ✓ Limite: {gerenciador.obter_limite()}")
    
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    # Executar exemplos
    exemplo_basico()
    exemplo_configuracao()
