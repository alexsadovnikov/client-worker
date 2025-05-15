import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="📊 Client Dashboard", layout="wide")

# Используем имя сервиса worker из docker-compose
WORKER_URL = "http://worker:8000"

st.title("📊 Client Service Dashboard")

st.markdown("### 🔄 Отправка тестового события")

if st.button("Отправить событие в worker"):
    data = {"event": "streamlit_test", "data": "Hello from Streamlit"}
    try:
        response = requests.post(f"{WORKER_URL}/send", json=data)
        st.success(f"✅ Ответ: {response.status_code} - {response.json()}")
    except Exception as e:
        st.error(f"❌ Ошибка при отправке: {e}")

st.markdown("### 🧾 Получить список контактов (mock CRM)")

if st.button("Получить контакты"):
    try:
        response = requests.get(f"{WORKER_URL}/crm/contacts")
        if response.status_code == 200:
            df = pd.DataFrame(response.json())
            st.dataframe(df)
        else:
            st.warning(f"⚠️ Ошибка: {response.status_code}")
    except Exception as e:
        st.error(f"❌ Ошибка при запросе: {e}")