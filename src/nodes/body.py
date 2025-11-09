from src.llm.gemini import initialize_gemini
model = initialize_gemini()

def body_node(state):
    """
    Uses Gemini to generate the body of the email.
    """
    context = state.get("context","")
    recipient = state.get("recipient", "")
    
    # Extract first name from email for personalization
    name = recipient.split('@')[0] if recipient else "there"
    
    prompt = f"""Write a brief, conversational email body for this context: {context}
                    Requirements:
                    - Write like you're texting a colleague, not writing a formal letter
                    - Be warm and genuine, not robotic
                    - Keep it under 4 sentences
                    - NO markdown formatting (no **, no *, no #)
                    - NO phrases like "I hope this email finds you well"
                    - Start with a casual greeting using the name: {name}
                    - NO meta-commentary or explanations
                    - Just the email body text

                    Context: {context}

                    Email body:"""
    

    response = model.generate_content(prompt)
    body =  response.text.strip()
    return {"body": body}  