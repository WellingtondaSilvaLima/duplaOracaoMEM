import streamlit as st
from datetime import datetime, timedelta

MULHERES = ['Wladia', 'Vânia', 'Ivonete', 'Dirce', 'Kelly', 'Ana Paula', 'Daisy', 'Júlia', 'Andréa', 'Thais']

def gerar_rodadas(lista_mulheres):
    num_participantes = len(lista_mulheres)
    # Se o número for ímpar, adicionamos um "fantasma" para fazer par
    if num_participantes % 2 != 0:
        lista_mulheres.append("Descansa")
        num_participantes += 1
    
    num_rodadas = num_participantes - 1
    metade = num_participantes // 2
    
    rodadas = {}
    
    for i in range(num_rodadas):
        nome_rodada = f'sessao{i+1}'
        rodadas[nome_rodada] = []
        
        for j in range(metade):
            primeiro = lista_mulheres[j]
            segundo = lista_mulheres[num_participantes - 1 - j]
            if primeiro != "Descansa" and segundo != "Descansa":
                rodadas[nome_rodada].append([primeiro, segundo])
        
        # Rotaciona a lista, exceto o primeiro elemento
        lista_mulheres.insert(1, lista_mulheres.pop())
    
    return rodadas

# Gerar as datas das sessões (começando em 12/08/2024)
def gerar_datas_sessoes(num_sessoes, data_inicio="12/08/2024"):
    data = datetime.strptime(data_inicio, "%d/%m/%Y")
    datas = []
    for i in range(num_sessoes):
        datas.append(data + timedelta(days=7*i))
    return [d.strftime("%d/%m") for d in datas]

rodadas = gerar_rodadas(MULHERES.copy())
datas_sessoes = gerar_datas_sessoes(len(rodadas))

st.title('Duplas de Oração - MEM')

for idx, (nome_rodada, duplas) in enumerate(rodadas.items()):
    # Formata o título da sessão com a data
    numero_sessao = idx + 1
    st.subheader(f'Sessão {numero_sessao} - {datas_sessoes[idx]}')
    
    # Exibe a tabela sem índices
    st.table(duplas)