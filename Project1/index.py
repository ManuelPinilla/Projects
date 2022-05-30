import yfinance as yf
import streamlit as st
import pandas as pd
# pequeña aplicacion web en streamlit que muestra datos 
st.write("""
# Comportamiento en bolsa de la empresa PAYPAL
""")

tickerSymbol = 'PYPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

df = pd.DataFrame(tickerDf)
df.rename(columns={'Volume': 'Volumen', 'Close': 'Cierre', 
                          }, inplace=True)
st.markdown('Comportamiento acciones Paypal **_Valor Unitario_**.')

st.line_chart(df.Cierre)
st.markdown('Comportamiento acciones Paypal **_Valor Volumen Total_**.')

st.line_chart(df.Volumen)

