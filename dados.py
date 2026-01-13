import json
import os
from main import JogoPc, JogoMobile 

# Nomes dos arquivos
ARQUIVO_JOGOS = 'jogos.json'
ARQUIVO_SETTINGS = 'settings.json'

def carregar_configuracoes():
    try:
        # Carrega as configurações do arquivo settings.json
        with open(ARQUIVO_SETTINGS, 'r', encoding='utf-8') as f:
            return json.load(f)
        
    except FileNotFoundError:
        # Configuração padrão caso o arquivo não exista
        return {
            "generos_favoritos": [],
            "meta_anual_finalizados": 12,
            "plataforma_principal": "PC",
            "limite_jogos_simultaneos": 3
        }

def salvar_jogos(lista_jogos):
    lista_para_json = []

    for jogo in lista_jogos:
        # Verifica se o objeto tem o método do Mixin (exportar_dados), se sim, adiciona o dicionário retornado à lista
        if hasattr(jogo, 'exportar_dados'):
            lista_para_json.append(jogo.exportar_dados())

    try:
        # Salva a lista de dicionários no arquivo jogos.json
        with open(ARQUIVO_JOGOS, 'w', encoding='utf-8') as f:
            json.dump(lista_para_json, f, indent=4, ensure_ascii=False)

        print("Dados salvos com sucesso.")

    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

def carregar_jogos():
    # Verifica se o arquivo existe, se não existir, retorna uma lista vazia
    if not os.path.exists(ARQUIVO_JOGOS):
        return []

    try:
        # Carrega os dados do arquivo jogos.json
        with open(ARQUIVO_JOGOS, 'r', encoding='utf-8') as f:
            dados_brutos = json.load(f)
        
        lista_objetos = []

        # Recria os objetos a partir dos dicionários carregados, usando o campo "tipo_classe" para identificar a classe correta
        for item in dados_brutos:

            # Remove o tipo da classe para decidir qual classe instanciar
            tipo = item.pop("tipo_classe") 

            # Remove o status para setar depois, evitando conflitos com a lógica de validação do setter
            status_salvo = item.pop("status", None)

            # Remove a plataforma, pois ela é definida internamente nas classes e não deve ser passada no construtor
            item.pop("plataforma", None)

            novo_jogo = None

            try:
                if tipo == "JogoPc":
                    novo_jogo = JogoPc(**item) # **item desempacota o dicionário nos argumentos
                elif tipo == "JogoMobile":
                    novo_jogo = JogoMobile(**item)

                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                # Aqui podemos adicionar mais tipos, caso o Kelvin implemente

                else:
                    print(f"Tipo de jogo desconhecido: {tipo}")
                    continue
                
                # Agora, tenta setar o status salvo, se houver
                if novo_jogo and status_salvo:
                    try:
                        novo_jogo.status = status_salvo

                    except Exception as e:
                        print(f"Aviso ao restaurar status: {e}")
 
                # Se foi recriado com sucesso, adiciona à lista
                if novo_jogo:
                    lista_objetos.append(novo_jogo)

            except TypeError as e:
                print(f"Erro ao instanciar {tipo} (Título: {item.get('titulo')}): {e}")

        return lista_objetos

    except Exception as e:
        print(f"Erro crítico ao carregar dados: {e}")
        return []