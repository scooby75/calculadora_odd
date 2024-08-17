import streamlit as st

# Função para calcular a odd Back
def calc_odd_back(stake, lucro_desejado):
    return (lucro_desejado / stake) + 1

# Função para calcular a odd Lay
def calc_odd_lay(stake, lucro_desejado):
    return (stake + lucro_desejado) / stake

# Título do app
st.title("Calculadora de Odds Back e Lay")

# Entrada de dados pelo usuário
valor_aposta = st.number_input("Informe o valor da aposta (R$):", min_value=0.0, format="%.2f")
lucro_desejado = st.number_input("Informe o lucro desejado (R$):", min_value=0.0, format="%.2f")

# Botão para calcular as odds
if st.button("Calcular"):
    if valor_aposta > 0 and lucro_desejado > 0:
        # Calcular a odd Back e a odd Lay necessárias
        odd_back = calc_odd_back(valor_aposta, lucro_desejado)
        odd_lay = calc_odd_lay(valor_aposta, lucro_desejado)
        
        # Exibir os resultados
        st.write(f"Para apostar R$ {valor_aposta:.2f} e obter um lucro de R$ {lucro_desejado:.2f}:")
        st.write(f"- A odd Back necessária seria {odd_back:.2f}.")
        st.write(f"- A odd Lay necessária para obter o mesmo lucro seria {odd_lay:.2f}.")
    else:
        st.warning("Por favor, insira valores válidos para a aposta e o lucro desejado.")
