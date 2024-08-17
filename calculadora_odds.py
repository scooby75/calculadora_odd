import streamlit as st

# Função para calcular a odd Back
def calc_odd_back(lucro_desejado, stake):
    return (lucro_desejado / stake) + 1

# Função para calcular a Stake e Responsabilidade na odd Lay
def calc_stake_lay(lucro_desejado, odd_lay):
    return lucro_desejado / (1 - (1 / odd_lay))

def calc_responsabilidade_lay(stake_lay, odd_lay):
    return stake_lay * (odd_lay - 1)

# Título do app
st.title("Calculadora de Odds Back e Lay")

# Entrada de dados pelo usuário
stake = st.number_input("Informe o valor da aposta (Stake) R$:", min_value=0.0, format="%.2f")
lucro_desejado = st.number_input("Informe o lucro desejado (R$):", min_value=0.0, format="%.2f")

# Botão para calcular as odds
if st.button("Calcular Odds"):
    if stake > 0 and lucro_desejado > 0:
        # Calcular a odd Back necessária
        odd_back = calc_odd_back(lucro_desejado, stake)
        
        # Presumindo que a odd Lay seja fornecida
        odd_lay = st.number_input("Informe a odd Lay (ex: 1.30):", min_value=1.01, value=1.30, format="%.2f")
        stake_lay = calc_stake_lay(lucro_desejado, odd_lay)
        responsabilidade_lay = calc_responsabilidade_lay(stake_lay, odd_lay)
        
        # Exibir os resultados
        st.write(f"Para obter um lucro de R$ {lucro_desejado:.2f} com uma aposta de R$ {stake:.2f}:")
        st.write(f"- A odd Back necessária seria: **{odd_back:.2f}**")
        st.write(f"- Para obter o mesmo lucro de R$ {lucro_desejado:.2f} em uma odd Lay de {odd_lay:.2f}:")
        st.write(f"    - Stake Lay necessária: **R$ {stake_lay:.2f}**")
        st.write(f"    - Responsabilidade: **R$ {responsabilidade_lay:.2f}**")
    else:
        st.warning("Por favor, insira valores válidos para a aposta e o lucro desejado.")
