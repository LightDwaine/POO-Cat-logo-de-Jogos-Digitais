#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Teste da classe Colecao para gerenciar coleções de jogos"""

from jogo import JogoPc, JogoMobile, JogoConsole
from colecoes import Colecao

def teste_colecao_jogos():
    """Testa funcionalidades da classe Colecao de jogos"""
    print("\n" + "="*70)
    print("TESTE: Coleção de Jogos")
    print("="*70)
    
    # Criar coleção
    print("\n1. Criando coleção...")
    colecao = Colecao()
    print(f"   ✅ Coleção criada. Quantidade: {colecao.obter_quantidade()}")
    
    # Criar alguns jogos
    print("\n2. Criando jogos...")
    jogo1 = JogoPc("The Witcher 3", 9, 0, "RPG", "2024-01-01", "", 2015)
    jogo2 = JogoPc("Elden Ring", 10, 0, "Ação-RPG", "2024-01-05", "", 2022)
    jogo3 = JogoMobile("Genshin Impact", 8, 0, "RPG", "2024-02-01", "", 2020)
    jogo4 = JogoPc("Cyberpunk 2077", 8, 0, "RPG", "2024-02-10", "", 2020)
    
    print(f"   ✅ 4 jogos criados")
    
    # Adicionar jogos
    print("\n3. Adicionando jogos à coleção...")
    colecao.adicionar(jogo1)
    colecao.adicionar(jogo2)
    colecao.adicionar(jogo3)
    colecao.adicionar(jogo4)
    print(f"   Total na coleção: {colecao.obter_quantidade()}")
    
    # Tentar adicionar duplicado
    print("\n4. Tentando adicionar duplicado...")
    jogo_duplicado = JogoPc("The Witcher 3", 9, 0, "RPG", "2024-01-01", "", 2015)
    colecao.adicionar(jogo_duplicado)
    
    # Listar todos
    print("\n5. Listando todos os jogos...")
    colecao.listar()
    
    # Buscar por título
    print("\n6. Buscando jogo por título...")
    encontrado = colecao.buscar_por_titulo("Elden Ring")
    if encontrado:
        print(f"   ✅ Encontrado: {encontrado.titulo} ({encontrado.plataforma})")
    
    # Finalizar alguns jogos
    print("\n7. Finalizando alguns jogos...")
    jogo1.horasJogadas = 100
    jogo1.status = "finalizado"
    jogo1.nota = 9
    
    jogo2.horasJogadas = 120
    jogo2.status = "finalizado"
    jogo2.nota = 10
    
    print("   ✅ 2 jogos finalizados")
    
    # Buscar por status
    print("\n8. Buscando jogos por status 'finalizado'...")
    finalizados = colecao.buscar_por_status("finalizado")
    colecao.listar_por_status("finalizado")
    print(f"   Total finalizados: {colecao.obter_quantidade_por_status('finalizado')}")
    
    # Buscar por gênero
    print("\n9. Buscando jogos por gênero 'RPG'...")
    rpgs = colecao.buscar_por_genero("RPG")
    print(f"   ✅ Encontrados {len(rpgs)} RPGs:")
    for jogo in rpgs:
        print(f"      - {jogo.titulo}")
    
    # Remover um jogo
    print("\n10. Removendo um jogo...")
    colecao.remover("Cyberpunk 2077", "Computador")
    print(f"   Total após remoção: {colecao.obter_quantidade()}")
    
    # Listar novamente
    print("\n11. Listagem final...")
    colecao.listar()
    
    print("="*70)
    print("✅ TESTE CONCLUÍDO COM SUCESSO!")
    print("="*70 + "\n")


if __name__ == "__main__":
    teste_colecao_jogos()
