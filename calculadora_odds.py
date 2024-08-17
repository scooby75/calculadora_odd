import streamlit as st

# Função para calcular a responsabilidade em uma aposta Lay
def calc_responsabilidade(odd_lay, stake):
    return stake * (odd_lay - 1)

# Função para converter odd Lay em odd Back
def calc_odd_back(odd_lay):
    return 1 / (1 - (1 / odd_lay))

# Título do app
st.title("Calculadora de Odds Lay e Back")

# Entrada de dados pelo usuário
valor_aposta = st.number_input("Informe o valor da aposta Lay (R$):", min_value=0.0, format="%.2f")
odd_lay = st.number_input("Informe a odd Lay:", min_value=1.01, format="%.2f")

# Botão para calcular a responsabilidade e a odd Back
if st.button("Calcular"):
    if valor_aposta > 0 and odd_lay > 1:
        # Calcular a responsabilidade e a odd Back
        responsabilidade = calc_responsabilidade(odd_lay, valor_aposta)
        odd_back = calc_odd_back(odd_lay)
        
        # Exibir os resultados
        st.write(f"Para uma odd Lay de {odd_lay:.2f} e uma aposta Lay de R$ {valor_aposta:.2f}:")
        st.write(f"- A responsabilidade seria R$ {responsabilidade:.2f}.")
        st.write(f"- A odd Back equivalente seria {odd_back:.2f}.")
    else:
        st.warning("Por favor, insira valores válidos para a aposta Lay e a odd Lay.")
