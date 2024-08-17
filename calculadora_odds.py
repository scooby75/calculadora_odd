import streamlit as st

# Função para calcular a stake Lay
def calcular_stake_lay(lucro_desejado, odd_lay):
    return lucro_desejado / (odd_lay - 1)

# Função para calcular a responsabilidade Lay
def calcular_responsabilidade_lay(stake_lay, odd_lay):
    return stake_lay * (odd_lay - 1)

# Função para calcular a odd Back equivalente
def calcular_odd_back(lucro_desejado, stake_lay):
    return (lucro_desejado / stake_lay) + 1

# Título do app
st.title("Cálculo de Odd Back e Responsabilidade Lay")

# Entrada de dados pelo usuário
lucro_desejado = st.number_input("Informe o lucro desejado (R$):", min_value=0.01, format="%.2f")
odd_lay = st.number_input("Informe a odd Lay:", min_value=1.01, format="%.2f")

# Botão para calcular os resultados
if st.button("Calcular"):
    if odd_lay > 1:
        # Calcular a stake Lay
        stake_lay = calcular_stake_lay(lucro_desejado, odd_lay)
        
        # Calcular a responsabilidade Lay
        responsabilidade_lay = calcular_responsabilidade_lay(stake_lay, odd_lay)
        
        # Calcular a odd Back equivalente
        odd_back = calcular_odd_back(lucro_desejado, stake_lay)
        
        # Exibir os resultados
        st.write(f"Para um lucro de R$ {lucro_desejado:.2f}:")
        st.write(f"- A stake necessária para uma aposta Lay com odd {odd_lay:.2f} é R$ {stake_lay:.2f}.")
        st.write(f"- A responsabilidade para uma aposta Lay com odd {odd_lay:.2f} e stake de R$ {stake_lay:.2f} é R$ {responsabilidade_lay:.2f}.")
        st.write(f"- A odd Back equivalente para o mesmo lucro seria {odd_back:.2f}.")
    else:
        st.warning("Por favor, insira uma odd Lay válida (maior que 1).")
