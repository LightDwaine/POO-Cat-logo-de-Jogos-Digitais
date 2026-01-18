# Ryan Keven Alves - UFCA

class Usuario:
    def __init__(self, id_usuario, nome):
        self.id_usuario = id_usuario
        self.nome = nome
        self.online = False
        self.ip = "127.0.0.1"
        self.porta = 0

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

    def __str__(self):
        status = "Online" if self.online else "Offline"
        return f"{self.nome} ({status}) {self.ip}:{self.porta}"

class Colecao:
    def __init__(self):
        self.usuarios = []

    def adicionar(self, usuario):
        if not self.buscar(usuario.id_usuario):
            self.usuarios.append(usuario)
            print(f"Adicionado: {usuario.nome}")
            return True
        print(f"Ja existe: {usuario.nome}")
        return False

    def remover(self, id_usuario):
        for i, u in enumerate(self.usuarios):
            if u.id_usuario == id_usuario:
                removido = self.usuarios.pop(i)
                print(f"Removido: {removido.nome}")
                return True
        print(f"Não encontrado ID {id_usuario}")
        return False

    def buscar(self, id_usuario):
        for u in self.usuarios:
            if u.id_usuario == id_usuario:
                return u
        return None

    def listar(self):
        if not self.usuarios:
            print("Nenhum usuario")
            return
        print("USUARIOS:")
        for u in self.usuarios:
            print(f"- {u}")
        print(f"Total: {len(self.usuarios)}")

# TESTE SIMPLES
print("TESTE PRATICA 03")
colecao = Colecao()

u1 = Usuario(1, "Ryan")
u2 = Usuario(2, "Maria")

colecao.adicionar(u1)
colecao.adicionar(u2)

u1.login("192.168.1.10", 8080)
colecao.listar()

colecao.remover(2)
colecao.listar()

print("SUCESSO!")
