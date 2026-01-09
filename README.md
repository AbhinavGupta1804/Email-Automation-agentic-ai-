# Agentic Cold Email Automation System 🚀  
**Generative AI | FastAPI | LangGraph | Gemini 2.5 Flash | GCP | SendGrid**

A high-performance Agentic AI system that generates and sends fully personalized cold emails for job and internship seekers. The system uses Resume + Job Description inputs to create tailored, high-conversion outreach emails with extremely high efficiency.

---

## 🌟 Key Highlights

### ⚡ 95% Reduction in Manual Email Drafting  
Built an AI-powered Cold Email Automation App that uses **Gemini 2.5 Flash** to generate personalized emails based on a user’s Resume and a company’s Job Description — eliminating almost all manual writing effort.

### 🧠 Enterprise-Grade Agentic Pipeline  
Designed a modular **LangGraph pipeline** with **5 specialized nodes**, featuring:
- Structured state management  
- LLM reasoning steps  
- Tool nodes  
- Config-driven modular design  
- Parallel subject + body generation  
- Centralized output aggregation  

This enables scalable, maintainable, production-level agentic workflows.

### 📧 Automated Email Dispatch (SendGrid)  
Integrated **SendGrid API** for automated email sending with **99% delivery reliability**, ensuring fast and secure message delivery.

### 🌩 Deployment  
Fully containerized and deployed on **Google Cloud Run** for fast, serverless, globally accessible performance.

---

## 🔗 Live Demo  
**GCP Cloud Run:**  
https://emailone-269395596918.europe-west1.run.app/

## Folder Structure
```
src/
├── data/
├── graph/
│   ├── __init__.py
│   ├── graphbuilder.py
│
├── llm/
│   ├── __init__.py
│   ├── gemini.py
│
├── nodes/
│   ├── __init__.py
│   ├── aggregator.py
│   ├── body.py
│   ├── router.py
│   ├── send.py
│   ├── subject.py
│
├── rag/
│   ├── __init__.py
│   ├── build_vectorstore.py
│   ├── retriever.py
│
├── state/
│   ├── __init__.py
│   ├── state.py
│
├── tools/
│   ├── __init__.py
│   ├── jd_extractor.py
│   ├── resume_extractor.py
│   ├── tools.py
│
├── ui/
│   ├── __init__.py
│
├── main.py
├── requirements.txt
|-- Dockerfile
```
![image](https://github.com/user-attachments/assets/ce966667-f582-4e95-a4c0-cf2aa5f071ad)

## 👨‍💻 Author  
**Abhinav Gupta**  
## 📬 Contact

📧 Email: [abhi1804gupta@gmail.com](mailto:abhi1804gupta@gmail.com)

🔗 LinkedIn: [Abhinav Gupta](https://www.linkedin.com/in/abhinav-gupta-369159282)


If you found this project useful, please ⭐ the repository!
