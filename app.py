import streamlit as st
import openai
import os

# Load your API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="🌿 Herbal Ingredient Explainer")
st.title("🌿 Herbal Ingredient Explainer")
st.write("Type the name of an herb or supplement to learn about it.")

ingredient = st.text_input("Enter an herb (e.g., Ashwagandha):")

if ingredient:
    with st.spinner("Looking it up..."):
        try:
            prompt = f"""
            You are a certified herbalist. Explain what {ingredient} is, how it's used,
            and any known safety concerns. Limit to 150 words. Avoid medical claims.
            """

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )

            st.success("Here's what we found:")
            st.write(response.choices[0].message["content"])

        except Exception as e:
            st.error("Something went wrong.")
            st.code(str(e))

