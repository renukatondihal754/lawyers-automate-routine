# # import requests
# # from bs4 import BeautifulSoup

# # BASE_URL = "https://e-jagriti.gov.in"

# # # Dummy mappings (replace with actual scraping results later)
# # STATE_MAP = {"KARNATAKA": "29"}
# # COMMISSION_MAP = {
# #     "29": {
# #         "Bangalore 1st & Rural Additional": "12345"
# #     }
# # }

# # def get_states():
# #     return [{"id": v, "name": k} for k, v in STATE_MAP.items()]

# # def get_commissions(state_id: str):
# #     commissions = COMMISSION_MAP.get(state_id, {})
# #     return [{"id": v, "name": k} for k, v in commissions.items()]

# # # def search_cases(state: str, commission: str, search_type: str, search_value: str):
# # #     # map state & commission
# # #     state_id = STATE_MAP.get(state.upper())
# # #     commission_id = COMMISSION_MAP.get(state_id, {}).get(commission)

# # #     if not state_id or not commission_id:
# # #         return []

# # #     # --- MOCKED data for assignment (replace with scraping if needed) ---
# # #     results = [
# # #         {
# # #             "case_number": "123/2025",
# # #             "case_stage": "Hearing",
# # #             "filing_date": "2025-02-01",
# # #             "complainant": "John Doe",
# # #             "complainant_advocate": "Adv. Reddy",
# # #             "respondent": "XYZ Ltd.",
# # #             "respondent_advocate": "Adv. Mehta",
# # #             "document_link": f"{BASE_URL}/docs/case123"
# # #         }
# # #     ]
# # #     return results


# # # app/services/jagriti_service.py
# # def search_cases(state: str, commission: str, search_type: str, search_value: str):
# #     """
# #     search_type can be: case_number, complainant, respondent,
# #     complainant_advocate, respondent_advocate, industry_type, judge
# #     """
# #     state_id = STATE_MAP.get(state.upper())
# #     commission_id = COMMISSION_MAP.get(state_id, {}).get(commission)

# #     if not state_id or not commission_id:
# #         return []

# #     # Mocked results (later scrape here)
# #     return [
# #         {
# #             "case_number": "123/2025",
# #             "case_stage": "Hearing",
# #             "filing_date": "2025-02-01",
# #             "complainant": "John Doe",
# #             "complainant_advocate": "Adv. Reddy",
# #             "respondent": "XYZ Ltd.",
# #             "respondent_advocate": "Adv. Mehta",
# #             "document_link": f"{BASE_URL}/docs/case123"
# #         }
# #     ]



# # app/services/jagriti_service.py
# import httpx
# from bs4 import BeautifulSoup

# # BASE_URL = "https://www.consumer.jagritidigital.in"
# BASE_URL = "https://consumer.jagritidigital.in"



# async def get_states():
#     async with httpx.AsyncClient() as client:
#         r = await client.get(f"{BASE_URL}/searchCases")
#         soup = BeautifulSoup(r.text, "lxml")

#         state_options = soup.select("select#state_id option")
#         states = {}
#         for opt in state_options:
#             if opt.get("value") and opt.text.strip():
#                 states[opt.text.strip().upper()] = opt["value"]

#         return states

# async def get_commissions(state_id: str):
#     async with httpx.AsyncClient() as client:
#         r = await client.post(f"{BASE_URL}/getCommissions", data={"state_id": state_id})
#         soup = BeautifulSoup(r.text, "lxml")

#         commission_options = soup.select("option")
#         commissions = {}
#         for opt in commission_options:
#             if opt.get("value") and opt.text.strip():
#                 commissions[opt.text.strip()] = opt["value"]

#         return commissions


# # async def scrape_cases(state: str, commission: str, search_type: str, search_value: str):
# #     state_id = STATE_MAP.get(state.upper())
# #     commission_id = COMMISSION_MAP.get(state_id, {}).get(commission)

# #     if not state_id or not commission_id:
# #         return {"error": "Invalid state or commission"}

# #     async with httpx.AsyncClient() as client:
# #         payload = {
# #             "state_id": state_id,
# #             "commission_id": commission_id,
# #             "search_type": search_type,
# #             "search_value": search_value
# #         }

# #         r = await client.post(f"{BASE_URL}/searchCases", data=payload)
# #         soup = BeautifulSoup(r.text, "lxml")

# #         cases = []
# #         rows = soup.select("table tr")[1:]  # skip header
# #         for row in rows:
# #             cols = [c.text.strip() for c in row.find_all("td")]
# #             if not cols:
# #                 continue
# #             case = {
# #                 "case_number": cols[0],
# #                 "case_stage": cols[1],
# #                 "filing_date": cols[2],
# #                 "complainant": cols[3],
# #                 "complainant_advocate": cols[4],
# #                 "respondent": cols[5],
# #                 "respondent_advocate": cols[6],
# #                 "document_link": BASE_URL + row.find("a")["href"] if row.find("a") else None
# #             }
# #             cases.append(case)

# #         return cases


# async def scrape_cases(state: str, commission: str, search_type: str, search_value: str):
#     states = await get_states()
#     state_id = states.get(state.upper())
#     if not state_id:
#         return {"error": "Invalid state"}

#     commissions = await get_commissions(state_id)
#     commission_id = commissions.get(commission)
#     if not commission_id:
#         return {"error": "Invalid commission"}

#     async with httpx.AsyncClient() as client:
#         payload = {
#             "state_id": state_id,
#             "commission_id": commission_id,
#             "search_type": search_type,
#             "search_value": search_value
#         }
#         r = await client.post(f"{BASE_URL}/searchCases", data=payload)
#         soup = BeautifulSoup(r.text, "lxml")

#         cases = []
#         rows = soup.select("table tr")[1:]  # skip header
#         for row in rows:
#             cols = [c.text.strip() for c in row.find_all("td")]
#             if not cols:
#                 continue
#             case = {
#                 "case_number": cols[0],
#                 "case_stage": cols[1],
#                 "filing_date": cols[2],
#                 "complainant": cols[3],
#                 "complainant_advocate": cols[4],
#                 "respondent": cols[5],
#                 "respondent_advocate": cols[6],
#                 "document_link": BASE_URL + row.find("a")["href"] if row.find("a") else None
#             }
#             cases.append(case)

#         return cases




# app/services/jagriti_service.py

from typing import List
from app.models import State, Commission, Case

# ---- Hardcoded states ----
STATES = [
    {"id": "11", "name": "KARNATAKA"},
    {"id": "12", "name": "KERALA"},
    {"id": "14", "name": "MAHARASHTRA"},
]

# ---- Hardcoded commissions per state (only DCDRC) ----
COMMISSIONS = {
    "11": [  # Karnataka
        {"id": "11-1", "name": "Bangalore 1st & Rural Additional", "type": "DISTRICT"},
        {"id": "11-2", "name": "Mysore DCDRC", "type": "DISTRICT"},
    ],
    "12": [
        {"id": "12-1", "name": "Ernakulam DCDRC", "type": "DISTRICT"},
    ],
    "14": [
        {"id": "14-1", "name": "Mumbai DCDRC", "type": "DISTRICT"},
    ],
}

# ---- Sample cases ----

# ---- Sample cases ----
SAMPLE_CASES = [
    # Karnataka - Bangalore
    {
        "case_number": "123/2025",
        "case_stage": "Hearing",
        "filing_date": "2025-02-01",
        "complainant": "John Doe",
        "complainant_advocate": "Adv. Reddy",
        "respondent": "XYZ Ltd.",
        "respondent_advocate": "Adv. Mehta",
        "document_link": "https://e-jagriti.gov.in/case123",
        "state_id": "11",
        "commission_id": "11-1",
    },
    {
        "case_number": "124/2025",
        "case_stage": "Order Passed",
        "filing_date": "2025-03-05",
        "complainant": "Alice",
        "complainant_advocate": "Adv. Sharma",
        "respondent": "ABC Pvt Ltd",
        "respondent_advocate": "Adv. Khan",
        "document_link": "https://e-jagriti.gov.in/case124",
        "state_id": "11",
        "commission_id": "11-1",
    },
    # Karnataka - Mysore
    {
        "case_number": "125/2025",
        "case_stage": "Hearing",
        "filing_date": "2025-03-10",
        "complainant": "Ramesh Kumar",
        "complainant_advocate": "Adv. Iyer",
        "respondent": "LMN Corp",
        "respondent_advocate": "Adv. Das",
        "document_link": "https://e-jagriti.gov.in/case125",
        "state_id": "11",
        "commission_id": "11-2",
    },
    # Kerala - Ernakulam
    {
        "case_number": "223/2025",
        "case_stage": "Hearing",
        "filing_date": "2025-02-15",
        "complainant": "Bob Thomas",
        "complainant_advocate": "Adv. Varma",
        "respondent": "XYZ Kerala Ltd",
        "respondent_advocate": "Adv. Nair",
        "document_link": "https://e-jagriti.gov.in/case223",
        "state_id": "12",
        "commission_id": "12-1",
    },
    # Maharashtra - Mumbai
    {
        "case_number": "323/2025",
        "case_stage": "Order Passed",
        "filing_date": "2025-03-20",
        "complainant": "Priya Singh",
        "complainant_advocate": "Adv. Deshmukh",
        "respondent": "Mumbai Corp",
        "respondent_advocate": "Adv. Joshi",
        "document_link": "https://e-jagriti.gov.in/case323",
        "state_id": "14",
        "commission_id": "14-1",
    },
]

# ----- Services -----
def get_states() -> List[State]:
    return [State(**s) for s in STATES]

def get_commissions(state_id: str) -> List[Commission]:
    return [Commission(**c) for c in COMMISSIONS.get(state_id, [])]

# Generic case search
def search_cases(state_name: str, commission_name: str, search_value: str, search_field: str) -> List[Case]:
    # Map state name -> ID
    state = next((s for s in STATES if s["name"].upper() == state_name.upper()), None)
    if not state:
        return []

    # Map commission name -> ID
    commissions = COMMISSIONS.get(state["id"], [])
    commission = next((c for c in commissions if c["name"].upper() == commission_name.upper()), None)
    if not commission:
        return []

    # Filter sample cases
    results = []
    for case in SAMPLE_CASES:
        if case["state_id"] == state["id"] and case["commission_id"] == commission["id"]:
            # Match by search field
            if search_field == "case_number" and search_value.lower() in case["case_number"].lower():
                results.append(Case(**case))
            elif search_field == "complainant" and search_value.lower() in case["complainant"].lower():
                results.append(Case(**case))
            elif search_field == "respondent" and search_value.lower() in case["respondent"].lower():
                results.append(Case(**case))
            elif search_field == "complainant_advocate" and search_value.lower() in case["complainant_advocate"].lower():
                results.append(Case(**case))
            elif search_field == "respondent_advocate" and search_value.lower() in case["respondent_advocate"].lower():
                results.append(Case(**case))
            elif search_field == "industry_type":
                # Mock: all cases are same industry
                results.append(Case(**case))
            elif search_field == "judge":
                # Mock: all cases same judge
                results.append(Case(**case))
    return results
