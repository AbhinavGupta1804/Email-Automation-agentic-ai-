import json
import re
from src.llm.gemini import initialize_gemini


class JDExtractor:
    """
    Extracts structured information from a Job Description using Gemini LLM.
    """

    def __init__(self):
        self.model = initialize_gemini()

    def build_prompt(self, jd_text: str) -> str:
        """
        Builds prompt for extracting structured JD fields.
        """
        return f"""
Extract key details from the following Job Description and return STRICT JSON only.

Required JSON structure:
{{
  "role": "",
  "company": "",
  "job_type": "",
  "location": "",
  "experience_required": "",
  "skills_required": [],
  "responsibilities": [],
  "nice_to_have": [],
  "keywords": []
}}

Job Description:
\"\"\" 
{jd_text}
\"\"\"

Return ONLY JSON. No explanation.
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

    def extract(self, jd_text: str) -> dict:
        """
        Sends JD to LLM → returns structured JSON
        """
        
        prompt = self.build_prompt(jd_text)

        try:
            response = self.model.generate_content(prompt)
            raw_output = response.text.strip()
            # Extract JSON from response
            cleaned = self.extract_json_from_response(raw_output)            
            parsed = json.loads(cleaned)
            return parsed

        except json.JSONDecodeError:
            raise ValueError("JD extraction failed: LLM did not return valid JSON.")

        except Exception as e:
            raise RuntimeError(f"JD extraction error: {str(e)}")


if __name__ == "__main__":
    jd_text = """Selected Intern's Day-to-Day Responsibilities Include:
Demonstrating strong programming skills in Python, with experience in designing and implementing machine learning algorithms, information extraction, and probabilistic matching models.
Applying knowledge of deep learning algorithms in NLP (e.g., LSTMs, RNNs) and Computer Vision (e.g., CNNs) using frameworks such as TensorFlow, Keras, and PyTorch to solve real-world problems.
Developing solutions for object detection, recognition, and image classification tasks using machine learning, deep learning algorithms, and transfer learning techniques.
Leveraging innovative and automated approaches for data annotation, labeling, and data augmentation, as well as implementing active learning methods.
Providing online code assistance, mentorship, and education-based solutions to support learners in mastering machine learning concepts.
Committing to continuous learning and adapting quickly to new systems and concepts as they emerge.
Working on research-based machine learning projects, staying updated on new developments in NLP and image recognition."""
    extractor = JDExtractor()
    result = extractor.extract(jd_text)
        # Save JSON to file
    with open("src/data/jd_data.json", "w") as f:
        json.dump(result, f, indent=2)
