from src.llm.gemini import initialize_gemini
model = initialize_gemini()

def subject_node(state):
    """
    Uses Gemini to generate a catchy subject line based on the email context.
    """
    jd = state.get("jd", "")
    
    prompt = f"""Generate ONLY a short email subject line (5-8 words max) for this jd: {jd}
    Requirements:
- Write like a human, not AI
- NO markdown, NO formatting, NO asterisks
- Be specific and natural
- Avoid spam words like "sincere", "regarding", "follow-up"
- Just the subject line text, nothing else   
    """
    response = model.generate_content(prompt)
    subject =  response.text.strip()
    return {"subject": subject}    





