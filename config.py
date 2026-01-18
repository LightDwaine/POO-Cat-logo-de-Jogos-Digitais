# -*- coding: utf-8 -*-
"""
Módulo centralizado para gerenciamento de configurações do projeto.
Evita duplicação de código entre jogo.py, dados.py e relatorios.py
"""

import json
import os

# Constantes
ARQUIVO_SETTINGS = 'settings.json'
ARQUIVO_JOGOS = 'jogos.json'

# Configurações padrão
CONFIGURACOES_PADRAO = {
    "generos_favoritos": [],
    "meta_anual_finalizados": 12,
    "plataforma_principal": "PC",
    "limite_jogos_simultaneos": 3
}


def carregar_configuracoes():
    """
    Carrega as configurações do arquivo settings.json.
    
    Returns:
        dict: Dicionário com as configurações ou configurações padrão se arquivo não existir
    """
    try:
        if os.path.exists(ARQUIVO_SETTINGS):
            with open(ARQUIVO_SETTINGS, 'r', encoding='utf-8') as f:
                return json.load(f)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Aviso ao carregar configurações: {e}")
    
    return CONFIGURACOES_PADRAO.copy()


def salvar_configuracoes(config):
    """
    Salva as configurações no arquivo settings.json.
    
    Args:
        config: Dicionário com as configurações a salvar
    """
    try:
        with open(ARQUIVO_SETTINGS, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Aviso ao salvar configurações: {e}")


def obter_configuracao(chave, valor_padrao=None):
    """
    Obtém uma configuração específica.
    
    Args:
        chave: Chave da configuração
        valor_padrao: Valor padrão se a chave não existir
        
    Returns:
        Valor da configuração ou valor_padrao
    """
    config = carregar_configuracoes()
    return config.get(chave, valor_padrao)


def atualizar_configuracao(chave, valor):
    """
    Atualiza uma configuração específica.
    
    Args:
        chave: Chave da configuração
        valor: Novo valor
    """
    config = carregar_configuracoes()
    config[chave] = valor
    salvar_configuracoes(config)


def obter_limite_jogos_simultaneos():
    """Retorna o limite de jogos simultâneos configurado"""
    return obter_configuracao('limite_jogos_simultaneos', 3)


def obter_meta_anual():
    """Retorna a meta anual de jogos finalizados"""
    return obter_configuracao('meta_anual_finalizados', 12)


def obter_generos_favoritos():
    """Retorna a lista de gêneros favoritos"""
    return obter_configuracao('generos_favoritos', [])


def obter_plataforma_principal():
    """Retorna a plataforma principal"""
    return obter_configuracao('plataforma_principal', 'PC')
