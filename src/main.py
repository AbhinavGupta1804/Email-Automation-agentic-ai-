from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.graph.graphbuilder import final_graph, State  # import your compiled graph

app = FastAPI(title="LangGraph Email Pipeline")

# Input schema
class EmailInput(BaseModel):
    prompt: str

@app.post("/run-graph/")
def run_graph(data: EmailInput):
    try:
        init_state = {"prompt": data.prompt}
        result = final_graph.invoke(init_state)

        return {"status": "success", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
def root():
    return {"message": "LangGraph FastAPI backend is running 🚀"}
