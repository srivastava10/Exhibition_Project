import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
headers = {"Authorization": f"Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
def get_answer(input):
    return query({
	"inputs": {
		"past_user_inputs": ["hello how are you"],
		"generated_responses": ["I am good! what about you?"],
		f"text": str(input)
	},
})
st.title("A CONVERSATIONAL CHATBOT")
with st.form("form1",clear_on_submit=True):
	input = st.text_input("Type Your Message")
	submit = st.form_submit_button("Submit")
out = get_answer(input)
if(len(out)!=0):
	out = get_answer(input)
	st.subheader(f"Answer:- {out['generated_text']}")