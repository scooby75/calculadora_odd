import streamlit as st

# Função para converter odd Lay em odd Back
def odd_lay_para_odd_back(odd_lay):
    probabilidade_lay = 1 / odd_lay
    probabilidade_nao_ocorrer = 1 - probabilidade_lay
    odd_back = 1 / probabilidade_nao_ocorrer
    return odd_back

# Título do app
st.title("Conversão de Odds Lay para Odds Back")

# Entrada de dados pelo usuário
odd_lay = st.number_input("Informe a odd Lay:", min_value=1.01, format="%.2f")

# Botão para calcular a odd Back equivalente
if st.button("Calcular"):
    if odd_lay > 1:
        # Calcular a odd Back equivalente
        odd_back = odd_lay_para_odd_back(odd_lay)
        
        # Exibir o resultado
        st.write(f"Para uma odd Lay de {odd_lay:.2f}:")
        st.write(f"- A odd Back equivalente é {odd_back:.2f}.")
    else:
        st.warning("Por favor, insira uma odd Lay válida (maior que 1).")
