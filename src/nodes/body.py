from src.llm.gemini import initialize_gemini
model = initialize_gemini()

def body_node(state):
    """
    Generates a natural, human-written cold email body using:
    - JD
    - Resume
    - RAG retrieved similar email
    """
    jd = state.get("jd", "")
    resume = state.get("resume")
    recipient = state.get("recipient")
    context = state.get("context")

    # Extract name
    name = recipient.split("@")[0].split(".")[0].title() if recipient else "there"

    prompt = f"""
You are writing a short cold email body to {name} for an internship/job inquiry.

Here is the context you must use to write a better email:

Job Description (JD):
{jd}

Candidate Resume:
{resume}

Extra Context:
{context}

Your output MUST follow this exact structure:
- The email body should be divided into EXACTLY 3 sections.
- Between each section, add ONE blank line (two line breaks).
- Section 1: Hyper-personalized intro line reading job description.
- Section 2: Who the candidate is, why they are reaching out, what value they can create, and 2–3 skill proofs from projects.
- Section 3: Why the candidate likes THIS company + a short call-to-action like “If you think there’s a fit, I’d love to connect or share a quick demo.”

Additional requirements:
- Tone: friendly, confident, conversational, casual .
- 3–5 lines per section max.
- Must NOT feel AI-generated.
- No generic phrases like “I hope you're doing well”.
- No markdown.
- Start with: “Hey {name},”
- Output ONLY the email body text — nothing else.
- Do NOT merge sections into a single paragraph.

Email body:


"""

    response = model.generate_content(prompt)
    return {"body": response.text.strip()}

