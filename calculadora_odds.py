import streamlit as st

# Função para calcular a odd Back
def calc_odd_back(lucro_desejado, valor_aposta):
    return (lucro_desejado + valor_aposta) / valor_aposta

# Função para calcular a responsabilidade e odd Lay
def calc_responsabilidade_lay(valor_aposta, odd_lay):
    return (odd_lay - 1) * valor_aposta

# Função para calcular o valor necessário para apostar no Lay para o mesmo lucro
def calc_valor_aposta_lay(lucro_desejado, odd_lay):
    return lucro_desejado / (1 - 1 / odd_lay)

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
        
        # Presumindo que odd lay seja 1.30 para cálculo da responsabilidade e valor lay
        odd_lay = 1.30
        valor_aposta_lay = calc_valor_aposta_lay(lucro_desejado, odd_lay)
        
        # Exibir os resultados
        st.write(f"Para obter um lucro de R$ {lucro_desejado:.2f} com uma aposta de R$ {valor_aposta:.2f}:")
        st.write(f"- A odd Back necessária seria: **{odd_back:.2f}**")
        st.write(f"- Para uma odd Lay de {odd_lay:.2f}, você precisaria apostar **R$ {valor_aposta_lay:.2f}** para obter o mesmo lucro.")
    else:
        st.warning("Por favor, insira valores válidos para a aposta e o lucro desejado.")
