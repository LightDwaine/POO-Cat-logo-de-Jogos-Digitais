# Ryan Keven Alves - UFCA

from colecoes import Colecao

class Usuario:
    def __init__(self, id_usuario, nome):
        self.id_usuario = id_usuario
        self.nome = nome
        self.online = False
        self.ip = "127.0.0.1"
        self.porta = 0
        self.colecoes = {}  # Dicionário: nome_colecao -> objeto Colecao

    def login(self, ip, porta):
        self.ip = ip
        self.porta = porta
        self.online = True
        print(f"{self.nome} logado em {ip}:{porta}")

    def logout(self):
        self.online = False
        self.ip = "127.0.0.1"
        self.porta = 0
        print(f"{self.nome} desconectado")
    
    def criar_colecao(self, nome_colecao):
        """
        Cria uma nova coleção de jogos.
        
        Args:
            nome_colecao: Nome da coleção a criar
            
        Returns:
            bool: True se criada, False se já existe
        """
        if nome_colecao in self.colecoes:
            print(f"⚠️ Coleção '{nome_colecao}' já existe!")
            return False
        
        self.colecoes[nome_colecao] = Colecao()
        print(f"✅ Coleção '{nome_colecao}' criada com sucesso!")
        return True
    
    def remover_colecao(self, nome_colecao):
        """
        Remove uma coleção.
        
        Args:
            nome_colecao: Nome da coleção a remover
            
        Returns:
            bool: True se removida, False se não existe
        """
        if nome_colecao not in self.colecoes:
            print(f"❌ Coleção '{nome_colecao}' não encontrada!")
            return False
        
        del self.colecoes[nome_colecao]
        print(f"✅ Coleção '{nome_colecao}' removida!")
        return True
    
    def obter_colecao(self, nome_colecao):
        """
        Retorna uma coleção específica.
        
        Args:
            nome_colecao: Nome da coleção
            
        Returns:
            Colecao: Objeto da coleção ou None
        """
        return self.colecoes.get(nome_colecao)
    
    def listar_colecoes(self):
        """Lista todas as coleções do usuário"""
        if not self.colecoes:
            print(f"📭 {self.nome} não possui coleções ainda")
            return
        
        print(f"\n{'='*70}")
        print(f"📚 COLEÇÕES DE {self.nome.upper()}")
        print(f"{'='*70}")
        for i, (nome, colecao) in enumerate(self.colecoes.items(), 1):
            qtd_jogos = colecao.obter_quantidade()
            qtd_jogando = colecao.obter_quantidade_por_status("jogando")
            qtd_finalizados = colecao.obter_quantidade_por_status("finalizado")
            
            print(f"{i}. {nome}")
            print(f"   Total de jogos: {qtd_jogos}")
            print(f"   Jogando: {qtd_jogando} | Finalizados: {qtd_finalizados}")
            print()
        print(f"Total de coleções: {len(self.colecoes)}")
        print(f"{'='*70}\n")
    
    def adicionar_jogo_colecao(self, nome_colecao, jogo):
        """
        Adiciona um jogo a uma coleção específica.
        
        Args:
            nome_colecao: Nome da coleção
            jogo: Objeto Jogo a adicionar
            
        Returns:
            bool: True se adicionado, False se coleção não existe
        """
        colecao = self.obter_colecao(nome_colecao)
        if colecao is None:
            print(f"❌ Coleção '{nome_colecao}' não encontrada!")
            return False
        
        return colecao.adicionar(jogo)
    
    def remover_jogo_colecao(self, nome_colecao, titulo, plataforma=None):
        """
        Remove um jogo de uma coleção específica.
        
        Args:
            nome_colecao: Nome da coleção
            titulo: Título do jogo
            plataforma: Plataforma opcional
            
        Returns:
            bool: True se removido, False se coleção não existe
        """
        colecao = self.obter_colecao(nome_colecao)
        if colecao is None:
            print(f"❌ Coleção '{nome_colecao}' não encontrada!")
            return False
        
        return colecao.remover(titulo, plataforma)
    
    def listar_jogos_colecao(self, nome_colecao):
        """
        Lista os jogos de uma coleção específica.
        
        Args:
            nome_colecao: Nome da coleção
        """
        colecao = self.obter_colecao(nome_colecao)
        if colecao is None:
            print(f"❌ Coleção '{nome_colecao}' não encontrada!")
            return
        
        print(f"\n{'='*70}")
        print(f"📚 COLEÇÃO: {nome_colecao.upper()} ({self.nome})")
        print(f"{'='*70}")
        colecao.listar()
    
    def total_jogos(self):
        """Retorna o total de jogos em todas as coleções"""
        return sum(colecao.obter_quantidade() for colecao in self.colecoes.values())
    
    def total_finalizados(self):
        """Retorna o total de jogos finalizados em todas as coleções"""
        return sum(colecao.obter_quantidade_por_status("finalizado") for colecao in self.colecoes.values())

    def __str__(self):
        status = "Online" if self.online else "Offline"
        qtd_colecoes = len(self.colecoes)
        qtd_jogos = self.total_jogos()
        return f"{self.nome} ({status}) | Coleções: {qtd_colecoes} | Jogos: {qtd_jogos}"
