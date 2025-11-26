from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse

from src.tools.resume_extractor import ResumeExtractor
from src.tools.jd_extractor import JDExtractor
from src.graph.graphbuilder import final_graph

import json
import uvicorn
import os

app = FastAPI(title="LangGraph Email Generator")

# Serve the UI folder
app.mount("/ui", StaticFiles(directory="src/ui"), name="ui")

# CORS enabled
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process/")
async def process(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
    prompt: str = Form(...)
):
    try:
        # os.makedirs("temp", exist_ok=True)
        pdf_path = f"/tmp/{resume.filename}"
        # pdf_path = f"temp/{resume.filename}"

        with open(pdf_path, "wb") as f:
            f.write(await resume.read())

        resume_extractor = ResumeExtractor()                        #RESUME EXTRACTION
        resume_data = resume_extractor.extract(pdf_path)

        jd_extractor = JDExtractor()                                #JD EXTRACTION
        jd_data = jd_extractor.extract(job_description)


        init_state = {
            "prompt": prompt,
            "resume": resume_data,
            "jd": jd_data
                    }
        result = final_graph.invoke(init_state)

        return {
            "status": "success",
            "message": "Extraction + Email generation complete",
            "result": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/", response_class=HTMLResponse)
def root():
    return FileResponse("src/ui/index5.html")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)






