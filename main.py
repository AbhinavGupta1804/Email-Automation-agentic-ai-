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

        resume_extractor = ResumeExtractor()
        resume_data = resume_extractor.extract(pdf_path)

        jd_extractor = JDExtractor()
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








# from fastapi import FastAPI, UploadFile, File, Form, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from src.tools.resume_extractor import ResumeExtractor
# from src.tools.jd_extractor import JDExtractor
# from src.graph.graphbuilder import final_graph
# import json
# import uvicorn
# import os

# app = FastAPI(title="LangGraph Email Generator")

# # Enable CORS for frontend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # You can restrict later
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.post("/process/")
# async def process(
#     resume: UploadFile = File(...),
#     job_description: str = Form(...),
#     prompt: str = Form(...)
# ):
#     try:
#         # Save PDF temporarily
#         os.makedirs("temp", exist_ok=True)
#         pdf_path = f"temp/{resume.filename}"

#         with open(pdf_path, "wb") as f:
#             f.write(await resume.read())

#         # Extract resume JSON
#         resume_extractor = ResumeExtractor()
#         resume_data = resume_extractor.extract(pdf_path)

#         with open("src/data/resume_data.json", "w") as f:
#             json.dump(resume_data, f, indent=2)

#         # Extract JD JSON
#         jd_extractor = JDExtractor()
#         jd_data = jd_extractor.extract(job_description)

#         with open("src/data/jd_data.json", "w") as f:
#             json.dump(jd_data, f, indent=2)

#         # Run graph
#         init_state = {
#             "prompt": prompt
#         }

#         result = final_graph.invoke(init_state)

#         return {
#             "status": "success",
#             "message": "Extraction + Email generation complete",
#             "result": result
#         }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# @app.get("/")
# def root():
#     return {"message": "Backend running successfully 🚀"}


# if __name__ == "__main__":
#     uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)









# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from src.graph.graphbuilder import final_graph, State  # import your compiled graph
# import uvicorn

# app = FastAPI(title="LangGraph Email Pipeline")

# # Input schema
# class EmailInput(BaseModel):
#     prompt: str

# @app.post("/run-graph/")
# def run_graph(data: EmailInput):
#     try:
#         init_state = {"prompt": data.prompt}
#         result = final_graph.invoke(init_state)

#         return {"status": "success", "result": result}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# @app.get("/")
# def root():
#     return {"message": "LangGraph FastAPI backend is running 🚀"}

# if __name__ == "__main__":
#     uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)

