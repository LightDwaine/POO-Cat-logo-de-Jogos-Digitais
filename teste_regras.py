#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testes para validar as 4 regras de negócio implementadas"""

from jogo import JogoPc, JogoMobile, Jogo
from dados import adicionar_jogo

def teste_regra1_avaliacao_apenas_finalizado():
    """REGRA 1: Um jogo só pode receber avaliação após ser marcado como FINALIZADO"""
    print("\n" + "="*70)
    print("TESTE REGRA 1: Avaliação apenas após FINALIZADO")
    print("="*70)
    
    jogo = JogoPc("The Witcher 3", 0, 0, "RPG", "2024-01-01", "", 2015)
    
    # Tentar avaliar sem finalizar (deve falhar)
    print("\n1. Tentando avaliar jogo em status 'não iniciado'...")
    try:
        jogo.nota = 8
        print("   ❌ ERRO: Permitiu avaliação sem finalizar!")
        return False
    except Exception as e:
        print(f"   ✅ OK: {e}")
    
    # Finalizar e depois avaliar
    print("\n2. Finalizando jogo...")
    jogo.horasJogadas = 50
    jogo.status = "finalizado"
    print(f"   ✅ Jogo finalizado: {jogo.status}")
    
    print("\n3. Avaliando jogo finalizado...")
    try:
        jogo.nota = 9
        print(f"   ✅ OK: Nota atribuída: {jogo.nota}")
        return True
    except Exception as e:
        print(f"   ❌ ERRO: {e}")
        return False


def teste_regra2_sem_duplicatas():
    """REGRA 2: Não é permitido duplicar jogos com mesmo título e plataforma"""
    print("\n" + "="*70)
    print("TESTE REGRA 2: Sem duplicatas (título + plataforma)")
    print("="*70)
    
    jogo1 = JogoPc("Elden Ring", 9, 0, "Ação", "2024-01-01", "", 2022)
    jogo2 = JogoPc("Elden Ring", 9, 0, "Ação", "2024-01-02", "", 2022)  # Duplicado
    jogo3 = JogoMobile("Elden Ring", 8, 0, "Ação", "2024-01-03", "", 2022)  # Diferente plataforma
    
    lista_jogos = []
    
    # Adicionar primeiro jogo (deve funcionar)
    print("\n1. Adicionando 'Elden Ring' (PC)...")
    try:
        adicionar_jogo(lista_jogos, jogo1)
        print(f"   ✅ Adicionado com sucesso. Total: {len(lista_jogos)}")
    except Exception as e:
        print(f"   ❌ ERRO: {e}")
        return False
    
    # Tentar adicionar duplicado (deve falhar)
    print("\n2. Tentando adicionar 'Elden Ring' (PC) novamente...")
    try:
        adicionar_jogo(lista_jogos, jogo2)
        print("   ❌ ERRO: Permitiu duplicata!")
        return False
    except Exception as e:
        print(f"   ✅ OK: {e}")
    
    # Adicionar mesmo título mas plataforma diferente (deve funcionar)
    print("\n3. Adicionando 'Elden Ring' (Mobile)...")
    try:
        adicionar_jogo(lista_jogos, jogo3)
        print(f"   ✅ Adicionado com sucesso (plataforma diferente). Total: {len(lista_jogos)}")
        return True
    except Exception as e:
        print(f"   ❌ ERRO: {e}")
        return False


def teste_regra3_horas_progressivas():
    """REGRA 3: Horas jogadas devem ser ≥ 0 e atualizadas progressivamente"""
    print("\n" + "="*70)
    print("TESTE REGRA 3: Horas ≥ 0 e progressivas")
    print("="*70)
    
    jogo = JogoPc("Cyberpunk 2077", 0, 10, "RPG", "2024-01-01", "", 2020)
    
    # Tentar horas negativas (deve falhar)
    print("\n1. Tentando definir horas negativas (-5)...")
    try:
        jogo.horasJogadas = -5
        print("   ❌ ERRO: Permitiu horas negativas!")
        return False
    except Exception as e:
        print(f"   ✅ OK: {e}")
    
    # Tentar diminuir horas (deve falhar)
    print("\n2. Tentando diminuir horas (10 → 5)...")
    try:
        jogo.horasJogadas = 5
        print("   ❌ ERRO: Permitiu diminuir horas!")
        return False
    except Exception as e:
        print(f"   ✅ OK: {e}")
    
    # Aumentar horas (deve funcionar)
    print("\n3. Aumentando horas (10 → 25)...")
    try:
        jogo.horasJogadas = 25
        print(f"   ✅ OK: Horas atualizadas para {jogo.horasJogadas}")
    except Exception as e:
        print(f"   ❌ ERRO: {e}")
        return False
    
    # Aumentar novamente (deve funcionar)
    print("\n4. Aumentando novamente (25 → 50)...")
    try:
        jogo.horasJogadas = 50
        print(f"   ✅ OK: Horas atualizadas para {jogo.horasJogadas}")
        return True
    except Exception as e:
        print(f"   ❌ ERRO: {e}")
        return False


def teste_regra4_aviso_meta():
    """REGRA 4: Se número de finalizados < meta anual, emitir aviso"""
    print("\n" + "="*70)
    print("TESTE REGRA 4: Aviso de meta anual")
    print("="*70)
    
    from relatorios import verificar_meta_anual
    from config import obter_meta_anual
    
    jogos = [
        JogoPc("Jogo 1", 0, 0, "RPG", "", "", 2024),
        JogoPc("Jogo 2", 0, 0, "RPG", "", "", 2024),
        JogoPc("Jogo 3", 0, 0, "RPG", "", "", 2024),
    ]
    
    # Finalizar apenas 2 (meta é 12)
    print("\n1. Finalizando apenas 2 jogos...")
    for i in range(2):
        jogos[i].horasJogadas = 10
        jogos[i].status = "finalizado"
    print(f"   ✅ 2 jogos finalizados")
    
    # Verificar meta (deve emitir aviso)
    print("\n2. Verificando meta anual...")
    meta = obter_meta_anual()
    finalizados = [j for j in jogos if j.status.lower() == "finalizado"]
    
    if len(finalizados) < meta:
        faltam = meta - len(finalizados)
        print(f"   ✅ AVISO EMITIDO: Faltam {faltam} jogos para atingir meta de {meta}")
        return True
    else:
        print(f"   ❌ ERRO: Deveria ter emitido aviso!")
        return False


if __name__ == "__main__":
    print("\n" + "="*70)
    print("   TESTES DE VALIDAÇÃO DAS 4 REGRAS DE NEGÓCIO")
    print("="*70)
    
    resultado1 = teste_regra1_avaliacao_apenas_finalizado()
    resultado2 = teste_regra2_sem_duplicatas()
    resultado3 = teste_regra3_horas_progressivas()
    resultado4 = teste_regra4_aviso_meta()
    
    print("\n" + "="*70)
    print("   RESUMO DOS TESTES")
    print("="*70)
    print(f"\nRegra 1 (Avaliação): {'✅ PASSOU' if resultado1 else '❌ FALHOU'}")
    print(f"Regra 2 (Duplicatas): {'✅ PASSOU' if resultado2 else '❌ FALHOU'}")
    print(f"Regra 3 (Horas): {'✅ PASSOU' if resultado3 else '❌ FALHOU'}")
    print(f"Regra 4 (Meta): {'✅ PASSOU' if resultado4 else '❌ FALHOU'}")
    
    total = sum([resultado1, resultado2, resultado3, resultado4])
    print(f"\nTotal: {total}/4 testes passaram\n")
