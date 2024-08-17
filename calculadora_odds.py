import streamlit as st

# Função para converter odd Lay em odd Back considerando a taxa da exchange
def odd_lay_para_odd_back(odd_lay, taxa):
    try:
        odd_back = 1 + (1 - taxa) / (odd_lay - 1)
        return odd_back
    except ZeroDivisionError:
        st.error("Erro na fórmula: verifique os valores de entrada.")
        return None

# Função para converter odd Back em odd Lay considerando a taxa da exchange
def odd_back_para_odd_lay(odd_back, taxa):
    try:
        odd_lay = 1 + (1 - taxa) / (odd_back - 1)
        return odd_lay
    except ZeroDivisionError:
        st.error("Erro na fórmula: verifique os valores de entrada.")
        return None

# Título do app
st.title("Conversão de Odds com Taxa da Exchange")

# Criando as abas
tab1, tab2 = st.tabs(["Lay para Back", "Back para Lay"])

# Aba 1: Lay para Back
with tab1:
    st.header("Conversão de Odd Lay para Odd Back")
    odd_lay = st.number_input("Informe a odd Lay:", min_value=1.01, format="%.2f", key="odd_lay")
    taxa_percentual = st.number_input("Informe a taxa da exchange (%):", min_value=0.0, max_value=100.0, format="%.2f", key="taxa_percentual_lay")

    taxa_decimal = taxa_percentual / 100.0

    if st.button("Calcular", key="calcular_lay_para_back"):
        odd_back = odd_lay_para_odd_back(odd_lay, taxa_decimal)
        if odd_back and odd_back > 1:
            st.write(f"Para uma odd Lay de {odd_lay:.2f} com uma taxa de exchange de {taxa_percentual:.2f}%:")
            st.write(f"- A odd Back equivalente é {odd_back:.4f}.")
        else:
            st.warning("Resultado inválido. Verifique os valores inseridos.")

# Aba 2: Back para Lay
with tab2:
    st.header("Conversão de Odd Back para Odd Lay")
    odd_back = st.number_input("Informe a odd Back:", min_value=1.01, format="%.2f", key="odd_back")
    taxa_percentual = st.number_input("Informe a taxa da exchange (%):", min_value=0.0, max_value=100.0, format="%.2f", key="taxa_percentual_back")

    taxa_decimal = taxa_percentual / 100.0

    if st.button("Calcular", key="calcular_back_para_lay"):
        odd_lay = odd_back_para_odd_lay(odd_back, taxa_decimal)
        if odd_lay and odd_lay > 1:
            st.write(f"Para uma odd Back de {odd_back:.2f} com uma taxa de exchange de {taxa_percentual:.2f}%:")
            st.write(f"- A odd Lay equivalente é {odd_lay:.4f}.")
        else:
            st.warning("Resultado inválido. Verifique os valores inseridos.")
