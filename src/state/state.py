from typing import TypedDict, Optional

class State(TypedDict):
    prompt: Optional[str]                
    recipient: Optional[str] 
    context: Optional[str]      
    subject: Optional[str]    
    body: Optional[str]      
    final_email: Optional[dict]
    jd: Optional[dict]
    resume: Optional[dict]