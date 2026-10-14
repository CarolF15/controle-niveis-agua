# Importa as ferramentas de cores e inicialização da biblioteca colorama

from colorama import Fore, Style, init

# Inicializa o colorama para garantir o funcionamento correto no terminal
init()

# Lista com as mensagens de alerta correspondentes a cada nível (do 1 ao 5)
niveis_agua = [
    "Nível 1: Muito baixo (crítico)",
    "Nível 2: Baixo",
    "Nível 3: Médio",
    "Nível 4: Alto",
    "Nível 5: Muito alto (alerta)",
]

def definir_cor_nivel(nivel):
#Função responsável por definir e retornar a cor conforme o nível informado.
  if nivel == 1:
    return Fore.RED
  elif nivel == 2:
    return Fore.YELLOW
  elif nivel == 3:
    return Fore.GREEN
  elif nivel == 4:
    return Fore.CYAN
  elif nivel == 5:
    return Fore.BLUE
  return Style.RESET_ALL

# Simulação de leituras do sensor do reservatório com valores definidos no código
leituras_simuladas = [1, 2, 3, 4, 5]

print(" SIMULAÇÃO DE MONITORAMENTO DO RESERVATÓRIO ")

for nivel_atual in leituras_simuladas:
  # Pega a mensagem correspondente na lista (lembrando que os índices começam em 0)
  mensagem = niveis_agua[nivel_atual - 1]

  # Utiliza a função para obter a cor correspondente
  cor = definir_cor_nivel(nivel_atual)

  # Exibe a mensagem colorida no terminal
  print(cor + mensagem)

# Restaura o estilo padrão do terminal após a exibição das mensagens
print(Style.RESET_ALL)