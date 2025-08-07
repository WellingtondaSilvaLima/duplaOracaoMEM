import streamlit as st

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
        nome_rodada = f'rodada{i+1}'
        rodadas[nome_rodada] = []
        
        for j in range(metade):
            primeiro = lista_mulheres[j]
            segundo = lista_mulheres[num_participantes - 1 - j]
            if primeiro != "Descansa" and segundo != "Descansa":
                rodadas[nome_rodada].append([primeiro, segundo])
        
        # Rotaciona a lista, exceto o primeiro elemento
        lista_mulheres.insert(1, lista_mulheres.pop())
    
    return rodadas

rodadas = gerar_rodadas(MULHERES.copy())  # Usamos copy para não modificar a lista original

st.title('Duplas de Oração - MEM')

for nome_rodada, duplas in rodadas.items():
    st.subheader(nome_rodada.capitalize().replace('Rodada', 'Rodada '))
    st.table(duplas)