import streamlit as st

# Função para converter odd Lay em odd Back considerando a taxa da exchange
def odd_lay_para_odd_back(odd_lay, taxa):
    try:
        # Debug: Mostrar valores intermediários
        st.write(f"Debug: Odd Lay = {odd_lay}, Taxa = {taxa}")
        
        # Calculando a odd Back com a fórmula correta
        odd_back = (odd_lay * (1 - taxa)) / ((1 - taxa) * odd_lay - 1)
        
        # Debug: Mostrar valor calculado da odd Back antes de retornar
        st.write(f"Debug: Odd Back calculada = {odd_back:.4f}")
        
        return odd_back
    except ZeroDivisionError:
        st.error("Erro na fórmula: verifique os valores de entrada.")
        return None

# Título do app
st.title("Teste de Conversão de Odds Lay para Odds Back com Taxa da Exchange")

# Entrada de dados pelo usuário
odd_lay = st.number_input("Informe a odd Lay:", min_value=1.01, format="%.2f")
taxa_percentual = st.number_input("Informe a taxa da exchange (%):", min_value=0.0, max_value=100.0, format="%.2f")

# Convertendo a taxa percentual para decimal
taxa_decimal = taxa_percentual / 100.0

# Debug: Mostrar valor da taxa convertida para decimal
st.write(f"Debug: Taxa convertida para decimal = {taxa_decimal}")

# Botão para calcular a odd Back equivalente
if st.button("Calcular"):
    # Calcular a odd Back equivalente
    odd_back = odd_lay_para_odd_back(odd_lay, taxa_decimal)
    
    # Exibir o resultado
    if odd_back and odd_back > 1:
        st.write(f"Para uma odd Lay de {odd_lay:.2f} com uma taxa de exchange de {taxa_percentual:.2f}%:")
        st.write(f"- A odd Back equivalente é {odd_back:.4f}.")
    else:
        st.warning("Resultado inválido. Verifique os valores inseridos.")
