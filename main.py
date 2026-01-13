# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Jogo(ABC):
    def __init__(self, titulo: str, nota: int, horasJogadas: int, genero: str, dataInicio: str, dataTermino: str, anoLancamento: int):
        self.__titulo = titulo
        self.__nota = nota
        self.__horasJogadas = horasJogadas
        self.__genero = genero
        self.__dataInicio = dataInicio
        self.__dataTermino = dataTermino
        self.__anoLancamento = anoLancamento
        if self.__horasJogadas > 0:
            self.__status = "jogando"
        else:
            self.__status = "não iniciado"

    def __str__(self):
        return f"Jogo: {self.__titulo} | Nota: {self.__nota} | {self.__status}"

    @abstractmethod
    def __repr__(self):
        pass

    @property
    def titulo(self):
        return self.__titulo

    @property
    def nota(self):
        return self.__nota

    @property
    def horasJogadas(self):
        return self.__horasJogadas

    @property
    def status(self):
        return self.__status

    @property
    def genero(self):
        return self.__genero

    @property
    def dataInicio(self):
        return self.__dataInicio

    @property
    def dataTermino(self):
        return self.__dataTermino

    @property
    def anoLancamento(self):
        return self.__anoLancamento

    @titulo.setter
    def titulo (self, novoNome):
        self.__titulo = novoNome

    @nota.setter
    def nota (self, novaNota):
        if novaNota < 0 or novaNota > 10:
          raise Exception("Nota inválida")
        else:
          self.__nota = novaNota

    @horasJogadas.setter
    def horasJogadas (self, novaHora):
        self.__horasJogadas = novaHora

    @status.setter
    def status (self, novoStatus): # Renamed setStatus to status
      if novoStatus == "finalizado":
        if self.__horasJogadas >= 1:
          self.__status = novoStatus
        else:
          raise Exception("Horas jogadas insuficientes")
      elif novoStatus == "jogando":
        self.__status = novoStatus
      elif novoStatus == "não iniciado":
        if self.__horasJogadas == 0:
          self.__status = novoStatus
        else:
          raise Exception("Você já registrou tempo de jogo nesse jogo")
      else:
        raise Exception("Status inválido")

    @genero.setter
    def genero (self, novoGenero):
        self.__genero = novoGenero

    @dataInicio.setter
    def dataInicio (self, novaDataInicio):
        self.__dataInicio = novaDataInicio

    @dataTermino.setter
    def dataTermino (self, novaDataTermino):
        self.__dataTermino = novaDataTermino

    @anoLancamento.setter
    def anoLancamento (self, novoAno):
        self.__anoLancamento = novoAno


class MixinExportacao:
    # Cria um dicionário base com os dados comuns a todos os jogos
    def exportar_dados(self):
        dados = {
            "titulo": self.titulo,
            "nota": self.nota,
            "horasJogadas": self.horasJogadas,
            "status": self.status,
            "genero": self.genero,
            "dataInicio": self.dataInicio,
            "dataTermino": self.dataTermino,
            "anoLancamento": self.anoLancamento,
            "tipo_classe": self.__class__.__name__ # Imperativo para sabermos qual classe recriar ao carregar o JSON
        }
        return dados

class JogoPc(Jogo, MixinExportacao):
    def __init__(self, titulo: str, nota: float, horasJogadas: int, genero: str, dataInicio: str, dataTermino: str, anoLancamento: int):
        super().__init__(titulo, nota, horasJogadas, genero, dataInicio, dataTermino, anoLancamento)
        self.__plataforma = "Computador"

    def __repr__(self):
        return f"Título: {self.titulo} Nota: {self.nota} Horas Jogadas: {self.horasJogadas} Status: {self.status} Gênero: {self.genero} Data Início: {self.dataInicio} Data Término: {self.dataTermino} Ano Lançamento: {self.anoLancamento}"

    def __str__(self):
        return super().__str__() + f" | Plataforma: {self.__plataforma}"

    @property
    def plataforma(self):
        return self.__plataforma
    
    def exportar_dados(self):
        dados = super().exportar_dados()
        dados["plataforma"] = self.plataforma
        return dados

class JogoMobile(Jogo, MixinExportacao):
    def __init__(self, titulo: str, nota: float, horasJogadas: int, genero: str, dataInicio: str, dataTermino: str, anoLancamento: int):
        super().__init__(titulo, nota, horasJogadas, genero, dataInicio, dataTermino, anoLancamento)
        self.__plataforma = "Mobile"

    def __repr__(self):
        return f"Título: {self.titulo} Nota: {self.nota} Horas Jogadas: {self.horasJogadas} Status: {self.status} Gênero: {self.genero} Data Início: {self.dataInicio} Data Término: {self.dataTermino} Ano Lançamento: {self.anoLancamento}"

    def __str__(self):
        return super().__str__() + f" | Plataforma: {self.__plataforma}"

    @property
    def plataforma(self):
        return self.__plataforma
    
    def exportar_dados(self):
        dados = super().exportar_dados()
        dados["plataforma"] = self.plataforma
        return dados
