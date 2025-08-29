# lawyers-automate-routine

# 🏛️ Lawyers Routine – Jagriti Case Search (Mock API)

This project provides a **FastAPI-based service** to search consumer court cases (State and District Commissions) in India.  

Originally, the assignment required integration with the official **[e-Jagriti portal](https://e-jagriti.gov.in/advance-case-search)**.  
However, since that website does **not expose a public API**, direct integration was not possible.  

👉 Instead, I created a **mock implementation** with **manually added states, commissions, and sample cases**.  
This lets you test and use the API **exactly as if the real system existed**, while keeping the structure flexible for future live integration.

---

## 📂 Folder Structure

lawyers-automate-routine/
│── app/
│ ├── main.py # FastAPI entry point
│ ├── models.py # Pydantic models
│ ├── routers/
│ │ ├── states.py # Endpoints for states
│ │ ├── commissions.py # Endpoints for commissions
│ │ ├── cases.py # Endpoints for case searches
│ ├── services/
│ │ ├── jagriti_service.py # Core scraper/service logic
│── requirements.txt # Dependencies
│── README.md # Project documentation



---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/lawyers-automate-routine.git
cd lawyers-automate-routine

# 2. Create Virtual Environment

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


# 3. Install Dependencies
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# 4. Install Playwright Browsers
playwright install

# 5. Run the Server
uvicorn app.main:app --reload


# Check API In Postman

📘 API Documentation

Swagger UI available at: http://127.0.0.1:8000/docs

🔹 States API
Get all states
GET /states


Response:

[
  { "id": "1", "name": "KARNATAKA" },
  { "id": "2", "name": "DELHI" }
]

🔹 Commissions API
Get all commissions for a state
POST /commissions


Body:

{
  "state": "KARNATAKA"
}


Response:

[
  { "id": "101", "name": "Bangalore 1st & Rural Additional", "type": "DISTRICT" },
  { "id": "102", "name": "Bangalore Urban", "type": "DISTRICT" }
]

🔹 Cases API
1. Search by Case Number
POST /cases/by-case-number


Body:

{
  "state": "KARNATAKA",
  "commission": "Bangalore 1st & Rural Additional",
  "search_value": "12345/2023"
}

2. Search by Complainant
POST /cases/by-complainant


Body:

{
  "state": "KARNATAKA",
  "commission": "Bangalore 1st & Rural Additional",
  "search_value": "RAMESH KUMAR"
}

3. Search by Respondent
POST /cases/by-respondent


Body:

{
  "state": "KARNATAKA",
  "commission": "Bangalore 1st & Rural Additional",
  "search_value": "ICICI BANK LTD"
}

4. Search by Complainant Advocate
POST /cases/by-complainant-advocate


Body:

{
  "state": "KARNATAKA",
  "commission": "Bangalore 1st & Rural Additional",
  "search_value": "ADV. RAJU"
}

5. Search by Respondent Advocate
POST /cases/by-respondent-advocate


Body:

{
  "state": "KARNATAKA",
  "commission": "Bangalore 1st & Rural Additional",
  "search_value": "ADV. SHARMA"
}

6. Search by Industry Type
POST /cases/by-industry-type


Body:

{
  "state": "KARNATAKA",
  "commission": "Bangalore 1st & Rural Additional",
  "search_value": "BANKING"
}

7. Search by Judge
POST /cases/by-judge


Body:

{
  "state": "KARNATAKA",
  "commission": "Bangalore 1st & Rural Additional",
  "search_value": "JUSTICE KUMAR"
}

🔹 Example Case Response
[
  {
    "case_number": "12345/2023",
    "case_stage": "Pending",
    "filing_date": "2023-05-14",
    "complainant": "RAMESH KUMAR",
    "complainant_advocate": "ADV. RAJU",
    "respondent": "ICICI BANK LTD",
    "respondent_advocate": "ADV. SHARMA",
    "document_link": "https://e-jagriti.gov.in/case-doc/12345"
  }
]


