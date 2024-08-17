import streamlit as st

# Função para converter odd Back em odd Lay
def odd_back_para_odd_lay(odd_back):
    probabilidade_back = 1 / odd_back
    probabilidade_lay = 1 - probabilidade_back
    odd_lay = 1 / probabilidade_lay
    return odd_lay

# Título do app
st.title("Conversão de Odds Back para Odds Lay")

# Entrada de dados pelo usuário
odd_back = st.number_input("Informe a odd Back:", min_value=1.01, format="%.2f")

# Botão para calcular a odd Lay equivalente
if st.button("Calcular"):
    if odd_back > 1:
        # Calcular a odd Lay equivalente
        odd_lay = odd_back_para_odd_lay(odd_back)
        
        # Exibir o resultado
        st.write(f"Para uma odd Back de {odd_back:.2f}:")
        st.write(f"- A odd Lay equivalente seria {odd_lay:.2f}.")
    else:
        st.warning("Por favor, insira uma odd Back válida (maior que 1).")
