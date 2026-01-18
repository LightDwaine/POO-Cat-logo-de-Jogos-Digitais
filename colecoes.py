from jogo import Jogo

class Colecao:
    """Classe para gerenciar uma coleção de jogos"""
    
    def __init__(self):
        self.jogos = []
    
    def adicionar(self, jogo):
        """
        Adiciona um jogo à coleção, verificando duplicatas.
        
        Args:
            jogo: Objeto Jogo a ser adicionado
            
        Returns:
            bool: True se adicionado, False se já existe
        """
        # Verificar duplicata (título + plataforma)
        if not self.buscar_por_titulo(jogo.titulo) or \
           (self.buscar_por_titulo(jogo.titulo) and 
            self.buscar_por_titulo(jogo.titulo).plataforma != jogo.plataforma):
            self.jogos.append(jogo)
            print(f"✅ Adicionado: {jogo.titulo} ({jogo.plataforma})")
            return True
        print(f"⚠️ Já existe: {jogo.titulo} ({jogo.plataforma})")
        return False
    
    def remover(self, titulo, plataforma=None):
        """
        Remove um jogo da coleção pelo título (e plataforma se especificada).
        
        Args:
            titulo: Título do jogo a remover
            plataforma: Plataforma opcional para remover específico
            
        Returns:
            bool: True se removido, False se não encontrado
        """
        for i, j in enumerate(self.jogos):
            if j.titulo.lower() == titulo.lower():
                if plataforma is None or j.plataforma.lower() == plataforma.lower():
                    removido = self.jogos.pop(i)
                    print(f"✅ Removido: {removido.titulo} ({removido.plataforma})")
                    return True
        print(f"❌ Não encontrado: {titulo}")
        return False
    
    def buscar_por_titulo(self, titulo):
        """
        Busca um jogo pela título.
        
        Args:
            titulo: Título do jogo a buscar
            
        Returns:
            Jogo: Objeto do jogo encontrado ou None
        """
        for j in self.jogos:
            if j.titulo.lower() == titulo.lower():
                return j
        return None
    
    def buscar_por_status(self, status):
        """
        Busca todos os jogos com um status específico.
        
        Args:
            status: Status a buscar (ex: "jogando", "finalizado")
            
        Returns:
            list: Lista de jogos com o status especificado
        """
        return [j for j in self.jogos if j.status.lower() == status.lower()]
    
    def buscar_por_genero(self, genero):
        """
        Busca todos os jogos de um gênero específico.
        
        Args:
            genero: Gênero a buscar
            
        Returns:
            list: Lista de jogos do gênero especificado
        """
        return [j for j in self.jogos if j.genero.lower() == genero.lower()]
    
    def listar(self):
        """Lista todos os jogos da coleção"""
        if not self.jogos:
            print("📭 Nenhum jogo na coleção")
            return
        
        print("\n" + "="*70)
        print("📚 COLEÇÃO DE JOGOS")
        print("="*70)
        for i, j in enumerate(self.jogos, 1):
            print(f"{i}. {j.titulo}")
            print(f"   Plataforma: {j.plataforma}")
            print(f"   Status: {j.status}")
            print(f"   Horas: {j.horasJogadas}h | Nota: {j.nota}")
            print()
        print(f"Total: {len(self.jogos)} jogo(s)")
        print("="*70 + "\n")
    
    def listar_por_status(self, status):
        """Lista jogos filtrados por status"""
        jogos_filtrados = self.buscar_por_status(status)
        
        if not jogos_filtrados:
            print(f"📭 Nenhum jogo com status '{status}'")
            return
        
        print(f"\n{'='*70}")
        print(f"📚 JOGOS COM STATUS: {status.upper()}")
        print(f"{'='*70}")
        for i, j in enumerate(jogos_filtrados, 1):
            print(f"{i}. {j.titulo} ({j.plataforma}) - {j.horasJogadas}h")
        print(f"Total: {len(jogos_filtrados)} jogo(s)")
        print("="*70 + "\n")
    
    def obter_quantidade(self):
        """Retorna a quantidade de jogos na coleção"""
        return len(self.jogos)
    
    def obter_quantidade_por_status(self, status):
        """Retorna a quantidade de jogos com um status específico"""
        return len(self.buscar_por_status(status))