import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="📊 Client Dashboard", layout="wide")

st.title("📊 Client Service Dashboard")

st.markdown("### 🔄 Отправка тестового события")

if st.button("Отправить событие в worker"):
    data = {"event": "streamlit_test", "data": "Hello from Streamlit"}
    try:
        response = requests.post("http://localhost:5050/send", json=data)
        st.success(f"✅ Ответ: {response.status_code} - {response.json()}")
    except Exception as e:
        st.error(f"❌ Ошибка при отправке: {e}")

st.markdown("### 🧾 Получить список контактов (mock CRM)")

if st.button("Получить контакты"):
    try:
        response = requests.get("http://localhost:5050/crm/contacts")
        if response.status_code == 200:
            df = pd.DataFrame(response.json())
            st.dataframe(df)
        else:
            st.warning(f"⚠️ Ошибка: {response.status_code}")
    except Exception as e:
        st.error(f"❌ Ошибка при запросе: {e}")
