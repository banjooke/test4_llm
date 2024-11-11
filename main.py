# main.py
import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

# Initialize OpenAI API key (use an environment variable for deployment)
openai_api_key = st.secrets["openai"]["OPENAI_API_KEY"]

# Set up LangChain components
llm = OpenAI(api_key=openai_api_key, max_tokens=1500)
template = "You are an expert Chemistry teacher, provide contents on: {input_text} write only on Chemistry and Chemistry only.If a topic is not related to chemistry, your response should be sorry I only write on chemistry. If a topic is not related to chemistry, do not write more than one sentence."
prompt = PromptTemplate(template=template, input_variables=["input_text"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Streamlit App Interface
st.title("Chemisty Contents App")
user_input = st.text_input("Enter the Chemistry topic here:")

if st.button("Generate contents"):
    if user_input:
        response = llm_chain.run(input_text=user_input)
        st.write(response)
    else:
        st.write("Please enter some text.")
