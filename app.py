import streamlit as st
from openai import OpenAI

# Load API key securely from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit UI
st.set_page_config(page_title="Herbal Ingredient Explainer", page_icon="🌿")
st.title("🌿 Herbal Ingredient Explainer")
st.write("Type the name of an herb or supplement to get a transparent, science-based explanation.")

# Input box
ingredient = st.text_input("Enter an herb (e.g., Ashwagandha, Turmeric, Ginseng):")

# On input
if ingredient:
    with st.spinner("Looking up information..."):
        try:
            # Define your prompt
            prompt = (
                f"You are a certified herbalist. Please explain what {ingredient} is, "
                "how it's typically used, what science says about its effectiveness, and any safety concerns. "
                "Keep it under 150 words. Avoid making medical claims or suggesting treatments."
            )

            # Call OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )

            # Display result
            st.success("Here's what we found:")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error("Something went wrong while contacting OpenAI:")
            st.code(str(e))
