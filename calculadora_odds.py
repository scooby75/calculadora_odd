import streamlit as st

# Função para calcular a odd Back
def calc_odd_back(lucro_desejado, valor_aposta):
    return (lucro_desejado / valor_aposta) + 1

# Função para calcular o valor necessário para apostar na odd Lay
def calc_odd_lay(lucro_desejado, valor_aposta):
    return valor_aposta / (1 - lucro_desejado / valor_aposta)

# Título do app
st.title("Calculadora de Odds Back e Lay")

# Entrada de dados pelo usuário
valor_aposta = st.number_input("Informe o valor da aposta (R$):", min_value=0.0, format="%.2f")
lucro_desejado = st.number_input("Informe o lucro desejado (R$):", min_value=0.0, format="%.2f")

# Botão para calcular as odds
if st.button("Calcular Odds"):
    if valor_aposta > 0 and lucro_desejado > 0:
        # Calcular a odd Back
        odd_back = calc_odd_back(lucro_desejado, valor_aposta)
        
        # Calcular a odd Lay (usando valor da aposta e lucro desejado)
        odd_lay = 1 + lucro_desejado / valor_aposta
        
        # Exibir os resultados
        st.write(f"Para obter um lucro de R$ {lucro_desejado:.2f} com uma aposta de R$ {valor_aposta:.2f}:")
        st.write(f"- A odd Back necessária seria: **{odd_back:.2f}**")
        st.write(f"- A odd Lay necessária seria: **{odd_lay:.2f}** (apostando R$ {valor_aposta:.2f})")
    else:
        st.warning("Por favor, insira valores válidos para a aposta e o lucro desejado.")
