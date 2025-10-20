# Nome: Leonardo Henrique dos Santos
# Curso: Analise e Desenvolvimento de Sistemas / PUC-PR
# Disciplina: Raciocínio Computacional (11100010563_20251_04)
# Entrega da Atividade Somativa II (Semana 8)

import json

#﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌
# Funções de confirmação de escolha
#﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌
def confirmacao_escolha(pergunta):
  while True:
    resposta = input(pergunta + ' \nEscolha entre: Sair, S (sim) ou N (não): \n').strip().upper()
    if resposta == "S":
      return True
    elif resposta == "N":
      print("Entendi, voltando para o menu...")
      return False
    if resposta == "Sair":
      print("\n Opção cancelada. Retornando ao menu...") 
      return False
    else:
      print('Você digitou uma opção que não existe, por gentileza digite S, N ou "sair".')
      
def executar_confirmacao(pergunta, acao, *args):
  if confirmacao_escolha(pergunta):
    acao(*args) if args else acao()

#﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌
# Classes triviais do objeto
#﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌
class Objeto:
  campos = []
  arquivo = None

  @classmethod
  def carregar_dados(cls, arquivo):
    try:
      with open(arquivo, 'r', encoding='utf-8') as file:
        return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
      return []
    except Exception as erro:
      print(f"Erro ao carregar dados: {erro}")
      return []
    
  @classmethod
  def salvar_dados(cls, dados, arquivo):
    try:
      with open(arquivo, 'w', encoding='utf-8') as file:
        json.dump(dados, file, ensure_ascii=False, indent=4)
      return True
    except Exception as erro:
      print(f"Erro ao carregar dados: {str(erro)}")
      return False

  @classmethod
  def buscar_por_codigo(cls, codigo, arquivo):
    dados = cls.carregar_dados(arquivo)
    for item in dados:
      if item.get('codigo') == codigo:
        return item
    return {}
  
  @classmethod
  def validar_relacao(cls, codigo, arquivo_relacionado):
    dados_relacionados = cls.carregar_dados(arquivo_relacionado)
    return any(item.get('codigo') == codigo for item in dados_relacionados)

  @classmethod
  def validar_codigo_objeto(cls, codigo):
    dados = cls.carregar_dados(cls.arquivo)
    return any(item.get('codigo') == codigo for item in dados)

#﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌
# Operaões gerais de adicionar, listar, atualizar e excluir
#﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌  
  @classmethod
  def adicionar(cls):
    dados = cls.carregar_dados(cls.arquivo)
    
    while True:
      novo_item = {}
      try:
        print(f"\nCadastro de {cls.__name__.upper()}")
        print(f"Digite 'sair' a qualquer momento para cancelar")

        while True:
          codigo = input("Digite o código: ").strip()
          if codigo.lower() == 'sair':
            print("Cadastro cancelado.")
            return

          if not codigo.isdigit():
            print("Erro: Código deve ser um número inteiro!")
            continue
              
          codigo_int = int(codigo)
          if cls.validar_codigo_objeto(codigo_int):
            print(f"Erro: Código {codigo_int} já existe!")
            continue
              
          novo_item['codigo'] = codigo_int
          break

        for campo in cls.campos:
          if campo == 'codigo':
            continue

          while True:
            if campo.startswith('codigo_'):
              entidade = campo.split('_')[1].title()
              classe_relacionada = globals()[entidade]
              print(f"\nLista de {entidade.lower()}s disponíveis:")
              classe_relacionada.listar()

            valor = input(f"{campo.replace('_', ' ').title()}: ").strip()
                  
            if valor.lower() == 'sair':
              print("Cadastro cancelado.")
              return

            if campo.startswith('codigo_'):
              if not valor.isdigit():
                print("Erro: Deve ser um código numérico!")
                continue
                          
              valor_int = int(valor)
              if not classe_relacionada.validar_codigo_objeto(valor_int):
                print(f"Erro: {entidade} com código {valor_int} não existe!")
                continue
                                         
              novo_item[campo] = valor_int
              break
              
            else:
              if not valor:
                print("Erro: Este campo não pode estar vazio!")
                continue
                                   
              novo_item[campo] = valor
              break
        dados.append(novo_item)
        if cls.salvar_dados(dados, cls.arquivo):
          print(f"\n{cls.__name__} cadastrado(a) com sucesso!")
          
        if not confirmacao_escolha("Deseja adicionar outro registro?"):
          return

      except ValueError:
        print("Erro: Valor inválido detectado!")
      except Exception as erro:
        print(f"Erro inesperado: {str(erro)}")

  @classmethod
  def listar(cls):  
    dados = cls.carregar_dados(cls.arquivo)
    print(f"\nListagem de {cls.__name__.lower()}s")  
      
    if not dados:
      print(f"Nenhum(a) {cls.__name__.lower()} cadastrado(a). Tente novamente!")
      return
    
    for idx, item in enumerate(dados, 1):
      linha = f"{idx}. "
      for campo in cls.campos:
        valor = item.get(campo, 'N/A')
        
        if campo.startswith('codigo_'):
          classe_relacionada = globals()[campo.split('_')[1].title()]
          relacionado = classe_relacionada.buscar_por_codigo(valor, classe_relacionada.arquivo)
          nome_relacionado = relacionado.get('nome', 'N/A') if relacionado else 'N/A'
          valor = f"{valor} ({nome_relacionado})"
        
        linha += f"{campo.replace('_', ' ').title()}: {valor} | "
      print(linha[:-3])

  @classmethod
  def atualizar(cls):
    dados = cls.carregar_dados(cls.arquivo)
    if not dados:
      print(f"Não há {cls.__name__.lower()}s cadastrados(as). Tente novamente!")
      return
    
    cls.listar()
    
    try:
      codigo_input = input(f"Digite o código do(a) {cls.__name__.lower()} para atualizar (ou digite 'sair): ").strip().lower()
      if codigo_input == 'sair':
        print("\nOperação cancelada!")
        return
      
      codigo = int(codigo_input)        
      encontrado = False
      
      for item in dados:
        if item.get('codigo') == codigo:
          encontrado = True
          print(f"Atualizando {cls.__name__.lower()} com o codigo {codigo}...")
          
          for campo in cls.campos:
            if campo == 'codigo': 
              continue
            
            valor_atual = item.get(campo, '"Dado não encontrado"')
            novo_valor = input(f"{campo.replace('_', ' ').title()} (Atual: {valor_atual}): ").strip().lower()
            
            if novo_valor == 'sair':
              print("\nOperação cancelada!")
              return

            if campo.startswith('codigo_'):
              if novo_valor:
                try:
                  codigo_relacionado = int(novo_valor)
                  objeto_relacionado = campo.split('_')[1]
                  
                  if not cls.validar_codigo_objeto(codigo_relacionado, f"{objeto_relacionado}s.json"):
                    print(f"Código inválido em {objeto_relacionado.replace('.json', '')}")
                    continue
                  
                  item[campo] = codigo_relacionado

                except ValueError:
                  print("Código deve ser um valor numérico. Tente novamente!")
                  continue
            elif novo_valor:
              item[campo] = novo_valor

          if cls.salvar_dados(dados, cls.arquivo):
            print(f"Atualização do(a) {cls.__name__.lower().title()} codigo {codigo} realizada com sucesso!")
          break

      if not encontrado:
        print(f"\nCódigo {codigo} não encontrado em {cls.__name__.lower()}s!")

    except ValueError:
      print("\nErro: O código deve ser um número inteiro!")
    except Exception as erro:
      print(f"\nErro inesperado: {str(erro)}")
              
  @classmethod
  def excluir(cls):
    dados = cls.carregar_dados(cls.arquivo)
    if not dados:
      print(f"Não há {cls.__name__.lower()} cadastrado(a). Tente novamente!")
      return
    
    cls.listar()
 
    try:
      codigo_input = input(f"Digite o código do(a) {cls.__name__.lower()} para excluir (ou 'sair'): ").strip().lower()
      
      if codigo_input == 'sair':
        print("\nOperação cancelada!")
        return
      
      codigo = int(codigo_input)
      novos_dados = [item for item in dados if item['codigo'] != codigo]
      
      if len(novos_dados) == len(dados):
        print("Código não encontrado. Tente novamente!")
        return

      if confirmacao_escolha("Tem certeza que deseja excluir este registro?"):
        if cls.salvar_dados(novos_dados, cls.arquivo):
          print("Registro excluído com sucesso!")

    except ValueError:
      print("\nErro: O código deve ser um número inteiro!")
    except Exception as erro:
      print(f"\nErro inesperado: {str(erro)}")

#﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌
# Classes de objetos
#﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌
class Estudante(Objeto):
  campos = ['codigo', 'nome', 'cpf']
  arquivo = 'estudantes.json'

class Professor(Objeto):
  campos = ['codigo', 'nome', 'cpf']
  arquivo = 'professores.json'

class Disciplina(Objeto):
  campos = ['codigo','nome']
  arquivo = 'disciplinas.json'

class Turma(Objeto):
  campos = ['codigo', 'codigo_professor', 'codigo_disciplina']
  arquivo = 'turmas.json'

class Matricula(Objeto):
  campos = ['codigo', 'codigo_turma', 'codigo_estudante', 'codigo_disciplina']
  arquivo = 'matriculas.json'

#﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌
# Classes de objetos
#﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌

opcoes_menu_primario = {
    '1': ('Estudantes', Estudante),
    '2': ('Professores', Professor),
    '3': ('Disciplinas', Disciplina),
    '4': ('Turmas', Turma),
    '5': ('Matrículas', Matricula)
}

opcoes_menu_secundario = {
    '1': ('Adicionar', 'adicionar'),
    '2': ('Listar', 'listar'),
    '3': ('Atualizar', 'atualizar'),
    '4': ('Excluir', 'excluir')
}
def mostrar_menu(titulo, opcoes):
  print(f"\n=== {titulo} ===")
  for key, (nome, _) in opcoes.items():
      print(f"{key}. {nome}")
  print("5. Voltar" if titulo != "Menu Principal" else "6. Sair")

def main():

  print("\n=== Sistema de Gestão Acadêmica ===")
  
  while True:
    mostrar_menu("Menu Principal", opcoes_menu_primario)
    opcao = input("\nEscolha uma opção: ").strip()
    
    if opcao == '6':
      if confirmacao_escolha("Tem certeza que deseja sair?"):
        print("\nSistema encerrado!")
        break
      continue
        
    if opcao not in opcoes_menu_primario:
      print("\nOpção inválida. Por gentileza, escolha tente novamente!") 
      continue
        
    objeto_nome, entidade_classe = opcoes_menu_primario[opcao]
    
    while True:
      mostrar_menu(f"Operações: {objeto_nome}", opcoes_menu_secundario)
      sub_opcao = input("\nEscolha uma operação: ").strip()
        
      if sub_opcao == '5':
        break
            
      if sub_opcao not in opcoes_menu_secundario:
        print("\nOpção inválida. Por gentileza, escolha tente novamente!")
        continue
            
      _, metodo = opcoes_menu_secundario[sub_opcao]
      getattr(entidade_classe, metodo)()

if __name__ == "__main__":
  main()