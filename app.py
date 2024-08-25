import os
import streamlit as st
import google.generativeai as genai

# Configure the Gemini API with your API key
genai.configure(api_key="AIzaSyCRZAbKS9OAY64bEhomm8QjHpWXmpSeH1g")

# Set up the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Start the chat session with initial prompt
chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
               "Act as a recipe generator. When the user enters the name of a food item, you should respond with a detailed recipe for that item, including ingredients, preparation steps, and cooking time. If the user enters something that is not a food item, respond with: 'Please enter a valid food item.'",
            ],
        },
        {
            "role": "model",
            "parts": [
                "Please tell me what food item you would like a recipe for! I'm ready to share my culinary knowledge. 😉 \n",
            ],
        },
    ]
)

# Streamlit app
st.title("Recipe Generator")

# Input for food item
food_item = st.text_input("Enter a food item:")

# Button to generate recipe
if st.button("Generate Recipe"):
    if food_item:
        # Send the message to the chat session
        response = chat_session.send_message(food_item)
        
        # Clean the response by removing stars (*) and hash symbols (#)
        cleaned_response = response.text.replace("*", "").replace("#", "")
        
        # Display the recipe in Streamlit
        st.text_area("Recipe", cleaned_response, height=400)
    else:
        st.warning("Please enter a food item.")
