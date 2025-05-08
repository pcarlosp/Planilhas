
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Relatório de Consumo Diário', layout='wide')
st.title('📊 Painel Diário de Consumo de Combustível')

st.markdown("Faça upload de um ou mais arquivos `.xlsx` com os relatórios de consumo.")

# Upload múltiplo
arquivos = st.file_uploader("Selecionar relatórios (.xlsx)", type="xlsx", accept_multiple_files=True)

if arquivos:
    nomes = [f.name for f in arquivos]
    arquivo_escolhido = st.selectbox("Selecione o arquivo para visualizar:", nomes[::-1])

    arquivo_alvo = next((f for f in arquivos if f.name == arquivo_escolhido), None)

    if arquivo_alvo:
        try:
            df = pd.read_excel(arquivo_alvo)

            if "KM/L" in df.columns:
                df["KM/L"] = pd.to_numeric(df["KM/L"], errors='coerce').round(2)

            st.success(f"Relatório carregado: {arquivo_escolhido}")
            st.dataframe(df)

            if "KM/L" in df.columns and "PLACA" in df.columns:
                st.markdown("### 🔍 Médias de Consumo (KM/L)")
                st.bar_chart(df.set_index("PLACA")["KM/L"])

        except Exception as e:
            st.error(f"Erro ao ler o arquivo: {e}")
else:
    st.info("Aguardando upload de arquivos...")
