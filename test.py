import pytest
from jogo import JogoPc

# Fixture: Cria um jogo "padrão" para ser usado em vários testes, evitando repetição de código
@pytest.fixture
def jogo_exemplo():
    return JogoPc(
        titulo="Cyberpunk 2077",
        nota=9,
        horasJogadas=50,
        genero="RPG",
        dataInicio="2024-01-01",
        dataTermino="2024-02-01",
        anoLancamento=2020
    )

def test_criacao_jogo(jogo_exemplo):
    """Testa se os atributos foram atribuídos corretamente na criação."""
    assert jogo_exemplo.titulo == "Cyberpunk 2077"
    assert jogo_exemplo.plataforma == "Computador" # Verifica se a classe JogoPc definiu a plataforma corretamente
    assert jogo_exemplo.status == "jogando" # Com 50 horas, o status deve ser 'jogando' automaticamente

def test_validacao_nota_invalida(jogo_exemplo):
    """Testa se o sistema bloqueia notas fora do intervalo 0-10."""
    # O pytest.raises verifica se a exceção correta é lançada
    with pytest.raises(Exception) as erro_info:
        jogo_exemplo.nota = 11  # Tentando definir uma nota inválida
    
    assert "Nota inválida" in str(erro_info.value) # Confirma a mensagem de erro definida no seu setter

def test_mudanca_status_valida(jogo_exemplo):
    """Testa a lógica de transição de status."""
    jogo_exemplo.status = "finalizado"
    assert jogo_exemplo.status == "finalizado"

def test_mudanca_status_erro_horas(jogo_exemplo):
    """Testa a regra: não pode finalizar com menos de 1 hora jogada."""
    jogo_novo = JogoPc("Teste", 0, 0, "RPG", "", "", 2024) # 0 horas jogadas
    
    with pytest.raises(Exception) as erro_info:
        jogo_novo.status = "finalizado"
    
    assert "Horas jogadas insuficientes" in str(erro_info.value)

def test_exportacao_dados(jogo_exemplo):
    """Testa se o MixinExportacao está gerando o dicionário corretamente."""
    dados = jogo_exemplo.exportar_dados()
    assert dados['titulo'] == "Cyberpunk 2077"
    assert dados['tipo_classe'] == "JogoPc" # Importante para o seu sistema de carregar_jogos