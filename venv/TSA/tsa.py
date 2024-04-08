# Library import
import pandas as pd
import plotly.express as px
import streamlit as st
from prophet import Prophet

# Page configuration
st.set_page_config(
    page_title='Climate dashboard',
    page_icon=':sunny:'
)
st.title('Delhi Climate Forecasting')



# Read dataset
data = pd.read_csv('./DailyDelhiClimateTrain.csv')
data['date'] = pd.to_datetime(data['date'])

# Data selection
st.sidebar.subheader('Data selection')
start_date = st.sidebar.date_input('Start date', value=data['date'].min()).strftime('%Y-%m-%d')
end_date = st.sidebar.date_input('End date', value=data['date'].max()).strftime('%Y-%m-%d')

selected_data = data[(data['date'] >= start_date) & (data['date'] <= end_date)]

# Prophet sidebar
st.sidebar.subheader('Prophet parameters configuration')
#Imposta il range di previsione (max 1 anno, valore di default 90 gg)
horizon_selection = st.sidebar.slider('Forecasting horizon (days)', min_value=1, max_value=365, value=90)
#La growth selection può essere lineare o logistica
growth_selection = st.sidebar.radio(label='Growth', options=['linear', 'logistic'])
#Nel caso di scelta di grow logistica, bisogna specificare una capaacità.
#In questo caso la capacità è fissata a 1.2 (ovvero 120% del valore massimo realmente assunto)
#Sarebbe buona norma però fornire uno slider all'utente in modo che egli stesso possa variare 
#questo parametro e osservare come variano i grafici in tempo reale
if growth_selection == 'logistic':
    cap = 1.2
    selected_data['cap'] = cap

seasonality_selection = st.sidebar.radio(label='Seasonality', options=['additive', 'multiplicative'])

with st.sidebar.expander('Seasonality components'):
    monthly_selection = st.checkbox('Monthly', value=True)
    yearly_selection = st.checkbox('Yearly', value=True)

# Display selected data
st.header('Selected Data')
st.dataframe(selected_data)

# Prophet model fitting
with st.spinner('Model fitting..'):
    prophet_df = selected_data[['date', 'meantemp']]
    prophet_df = prophet_df.rename(columns={'date': 'ds', 'meantemp': 'y'})

    model = Prophet(
        seasonality_mode=seasonality_selection,
        yearly_seasonality=yearly_selection,
        growth=growth_selection,
    )
    if growth_selection == 'logistic':
        cap = 0.5
        prophet_df['cap'] = cap
        model.add_seasonality(name='monthly', period=30.5, fourier_order=5)

    model.fit(prophet_df)

# Prophet model forecasting
with st.spinner('Making predictions..'):
    future = model.make_future_dataframe(periods=horizon_selection, freq='D')
    if growth_selection == 'logistic':
        future['cap'] = cap
    forecast = model.predict(future)

# Prophet forecast plot --> Viene fatto sfruttando i grafici interattivi forniti dalla libreria plotly
fig = px.scatter(prophet_df, x='ds', y='y', labels={'ds': 'Date', 'y': 'Mean Temperature'})
fig.add_scatter(x=forecast['ds'], y=forecast['yhat'], name='Forecast')
fig.add_scatter(x=forecast['ds'], y=forecast['yhat_lower'], name='Lower Bound')
fig.add_scatter(x=forecast['ds'], y=forecast['yhat_upper'], name='Upper Bound')
st.plotly_chart(fig)
