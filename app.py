import streamlit as st
import pandas as pd
from prophet import Prophet  # Updated package name for forecasting

# Correct absolute import of the CryptoCurrencies class from alphavantage.py
from alphavantage import CryptoCurrencies

# Set the title of the app
st.title("Crypto Monthly Prediction")

# Get API key from Streamlit secrets
api_key = st.secrets["ALPHA_VANTAGE"]["API_KEY"]

# Instantiate the API wrapper with your API key
crypto = CryptoCurrencies(api_key=api_key)

# Allow user to select cryptocurrency and market
symbol = st.selectbox("Choose Crypto Symbol", ["BTC", "ETH"])
market = st.selectbox("Choose Market", ["USD", "CNY"])  # Adjust based on available options

# Fetch monthly data using the API call
st.write("Fetching monthly historical data...")
monthly_data = crypto.get_digital_currency_monthly(symbol, market)

# Convert the returned data to a Pandas DataFrame.
# (Assuming the API returns a dictionary with dates as keys and a nested dict that contains '4. close')
try:
    df = pd.DataFrame.from_dict(monthly_data, orient='index')
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'ds', '4. close': 'y'}, inplace=True)
    df['ds'] = pd.to_datetime(df['ds'])
    df['y'] = pd.to_numeric(df['y'], errors='coerce')
    st.write("Raw Data", df.tail())
except Exception as e:
    st.error("Error processing data: " + str(e))
    st.stop()

# Build and fit the forecast model using Prophet
st.write("Building forecast model...")
m = Prophet()
m.fit(df[['ds', 'y']])
# Create a future dataframe to predict the next 12 months
future = m.make_future_dataframe(periods=12, freq='M')
forecast = m.predict(future)

# Display the forecast data
st.write("Forecast Data", forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# Plot the forecast
fig1 = m.plot(forecast)
st.pyplot(fig1)

# Plot the forecast components (trend, seasonality, etc.)
fig2 = m.plot_components(forecast)
st.pyplot(fig2)
