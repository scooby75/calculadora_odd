import streamlit as st

# Função para calcular a odd Back
def calc_odd_back(lucro_desejado, stake):
    return (lucro_desejado / stake) + 1

# Função para calcular a Responsabilidade na odd Lay
def calc_responsabilidade_lay(lucro_desejado, odd_lay):
    return lucro_desejado * (odd_lay - 1)

# Título do app
st.title("Calculadora de Odds Back e Lay")

# Entrada de dados pelo usuário
lucro_desejado = st.number_input("Informe o lucro desejado (R$):", min_value=0.0, format="%.2f")
stake_back = st.number_input("Informe o valor da aposta (R$):", min_value=0.0, format="%.2f")
odd_back = st.number_input("Informe a odd Back:", min_value=1.01, format="%.2f")
odd_lay = st.number_input("Informe a odd Lay:", min_value=1.01, format="%.2f")

# Botão para calcular as odds
if st.button("Calcular"):
    if lucro_desejado > 0 and odd_back > 1 and odd_lay > 1:
        # Calcular o valor da aposta para odd Back
        lucro_back = stake_back * (odd_back - 1)
        
        # Calcular a Responsabilidade para odd Lay
        responsabilidade_lay = calc_responsabilidade_lay(lucro_desejado, odd_lay)
        
        # Exibir os resultados
        st.write(f"Para obter um lucro de R$ {lucro_desejado:.2f}:")
        st.write(f"- Apostando R$ {stake_back:.2f} em uma odd Back de {odd_back:.2f}, você obterá um lucro de R$ {lucro_back:.2f}.")
        st.write(f"- Apostando em uma odd Lay de {odd_lay:.2f}, sua responsabilidade será de R$ {responsabilidade_lay:.2f}.")
    else:
        st.warning("Por favor, insira valores válidos para lucro e odds.")
