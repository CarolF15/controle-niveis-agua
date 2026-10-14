# 📘 Projeto de Controle de Níveis de Água 
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

# Sistema de Monitoramento de Reservatório

Projeto desenvolvido para praticar programação estruturada e manipulação de listas com Python. O programa simula o monitoramento de um reservatório de água executado diretamente no terminal, exibindo mensagens de alerta coloridas de acordo com o nível de criticidade através da biblioteca `colorama`.

---

## 🎯 Objetivo do Programa 

- Simular um ambiente real de monitoramento de um reservatório de água utilizando valores definidos no código.
- Utilizar a biblioteca `colorama` para destacar visualmente cada situação de risco com uma cor específica no terminal.
- Aplicar estruturas fundamentais da linguagem Python, como listas para o armazenamento dos dados e funções para a organização do código.
- Garantir a boa prática de restaurar o estilo padrão do terminal após a exibição das mensagens.

---

## 📋 Regras e Funcionalidades

| Nível do Reservatório | Situação / Alerta | Cor Sugerida |
|---|---|---|
| Nível 1 | Muito baixo (crítico) | ![Vermelho](https://img.shields.io/badge/Vermelho-ff0000?style=flat-square&logoColor=white) |
| Nível 2 | Baixo | ![Amarelo](https://img.shields.io/badge/Amarelo-ffff00?style=flat-square&logoColor=black) |
| Nível 3 | Médio | ![Verde](https://img.shields.io/badge/Verde-00ff00?style=flat-square&logoColor=black) |
| Nível 4 | Alto | ![Ciano](https://img.shields.io/badge/Ciano-00ffff?style=flat-square&logoColor=black) |
| Nível 5 | Muito alto (alerta) | ![Azul](https://img.shields.io/badge/Azul-0000ff?style=flat-square&logoColor=white) |

---

## 🚀 Como Executar o Programa

### Pré-requisitos
- **Python 3.10** (ou superior) instalado.

### Passo a Passo

1. Clone este repositório:
   ```bash
   git clone https://github.com/CarolF15/controle-niveis-agua.git
   ```

2. Instale a biblioteca necessária (`colorama`):
   ```bash
   pip install colorama
   ```

3. Execute o programa:
   ```bash
   python app.py
   ```
