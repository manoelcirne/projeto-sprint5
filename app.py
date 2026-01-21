import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('../vehicles.csv') # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão
        
if hist_button: # se o botão for clicado
            # escrever uma mensagem
            st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
            # criar um histograma
            fig = px.histogram(car_data, x="odometer")
        
            # exibir um gráfico Plotly interativo
            st.plotly_chart(fig, use_container_width=True)


disp_button = st.button('Criar gráfico de dispersão') # cria um botão

if disp_button: # se o botão for clicado
        # escreve a mensagem
        st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros') 

        # cria o gráfico de dispersão
        disp = px.scatter(car_data,x='odometer')
        
        # exibir um gráfico Plotly interativo
        st.plotly_chart(disp,use_container_width=True)
        
