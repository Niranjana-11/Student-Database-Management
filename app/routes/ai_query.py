from fastapi import APIRouter, Depends, HTTPException
from langchain_ollama import ChatOllama
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.model import Student

router = APIRouter(prefix="/ai", tags=["AI Query"])

llm = ChatOllama(model="llama3.2:3b", temperature=0)


class QueryRequest(BaseModel):
    question: str


@router.post("/query-student")
def ask_student_database(payload: QueryRequest, db: Session = Depends(get_db)):
    try:
        students = db.query(Student).all()

        records = "\n".join(
            f"- Name: {s.student_name} | Class: {s.student_class} | "
            f"Section: {s.student_section} | Date of birth: {s.student_dob} | "
            f"Subject: {s.student_sub or 'N/A'}"
            for s in students
        ) or "(no students)"

        prompt = f"""You answer questions about a student list.

Rules:
- Use ONLY the records below. Do not invent anything.
- Check EVERY record one by one before answering.
- If several students match, list ALL of them.
- If none match, say "No matching students."
- Keep the answer short. Do not repeat the records.

Records:
{records}

Question: {payload.question}
Answer:"""

        response = llm.invoke(prompt)
        return {"Question": payload.question, "answer": response.content}

    except Exception:
        raise HTTPException(status_code=500, detail="Could not process the question.")