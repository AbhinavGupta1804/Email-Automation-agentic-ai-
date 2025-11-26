import json
import re
import pdfplumber
from src.llm.gemini import initialize_gemini


class ResumeExtractor:
    """
    Extracts structured information from a PDF resume using Gemini LLM.
    """

    def __init__(self):
        self.model = initialize_gemini()

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """
        Extracts raw text from a PDF file using pdfplumber.
        """
        try:
            text = ""
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() + "\n"
            return text.strip()

        except Exception as e:
            raise RuntimeError(f"Error extracting PDF text: {str(e)}")

    def clean_text(self, text: str) -> str:
        """
        Optional cleaning (removes extra spaces, non-ASCII chars)
        """
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def build_prompt(self, resume_text: str) -> str:
        """
        Builds prompt for structured extraction
        """
        return f"""
Extract all important details from this resume and return STRICT JSON only.

Required fields:
{{
  "name": "",
  "email": "",
  "phone": "",
  "location": "",
  "education": [],
  "skills": [],
  "projects": [],
  "experience": [],
  "certifications": [],
  "achievements": []
}}

Resume Text:
\"\"\"
{resume_text}
\"\"\"

Return only JSON. No explanation.
"""

    def extract_json_from_response(self, raw_output: str) -> str:
        """
        Robustly extracts JSON from LLM response, handling markdown code blocks.
        """
        # Remove leading/trailing whitespace
        cleaned = raw_output.strip()
        
        # Try to extract JSON from markdown code blocks
        json_pattern = r"```(?:json)?\s*(\{.*?\})\s*```"
        match = re.search(json_pattern, cleaned, re.DOTALL)
        
        if match:
            return match.group(1).strip()
        
        # If no code blocks, try to find raw JSON
        # Look for content between first { and last }
        if cleaned.startswith('{') and cleaned.endswith('}'):
            return cleaned
        
        # Try to extract anything between first { and last }
        json_match = re.search(r'\{.*\}', cleaned, re.DOTALL)
        if json_match:
            return json_match.group(0)
        
        return cleaned

    def extract(self, pdf_path: str) -> dict:
        """
        Master function:
        1. Extract text from PDF
        2. Clean text
        3. Send prompt to Gemini
        4. Parse JSON output
        """
        resume_text = self.extract_text_from_pdf(pdf_path)
        resume_text = self.clean_text(resume_text)

        prompt = self.build_prompt(resume_text)

        try:
            response = self.model.generate_content(prompt)
            raw_output = response.text.strip()



            # Extract JSON from response
            cleaned = self.extract_json_from_response(raw_output)

            # Parse JSON
            json_output = json.loads(cleaned)
            
            return json_output

        except json.JSONDecodeError as e:
            raise ValueError(f"LLM response was not valid JSON: {str(e)}")

        except Exception as e:
            raise RuntimeError(f"Error in resume extraction: {str(e)}")


if __name__ == "__main__":
    extractor = ResumeExtractor()
    result = extractor.extract("src/data/abhinav_11.pdf")
    
    # Save JSON to file
    with open("src/data/resume_data.json", "w") as f:
        json.dump(result, f, indent=2)
    
    print("\n✓ Resume data saved to resume_data.json")