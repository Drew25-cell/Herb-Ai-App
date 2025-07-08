import streamlit as st
import openai
import os

# Get your OpenAI key from Streamlit secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🌿 Herbal Ingredient Explainer")
st.write("Ask about any herb or supplement!")

ingredient = st.text_input("Enter an herb (e.g., Ashwagandha):")

if ingredient:
    with st.spinner("Looking it up..."):
        try:
            prompt = f"""
            You are a certified herbalist. Explain what {ingredient} is, how it is used, and any safety info. Avoid medical claims.
            Keep it under 150 words.
            """
            response = openai.ChatCompletions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.success("Here’s what we found:")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
