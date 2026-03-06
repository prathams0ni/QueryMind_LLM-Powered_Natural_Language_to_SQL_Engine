# 🧠 QueryMind: LLM-Powered Natural Language to SQL Engine

## 🚀 Project Overview

> QueryMind is a production-style Natural Language to SQL engine that transforms human language into secure, executable SQL queries using a locally hosted Large Language Model (Mistral via Ollama).
Unlike basic NL-to-SQL demos, QueryMind is designed as a complete system with real-world architectural considerations including:

- Dynamic multi-database discovery
- Schema-grounded prompt engineering
- Secure query execution layer
- Self-healing SQL correction loop
- Modular backend design
- Real-time visualization

The application directly connects to the MySQL server and automatically detects all available databases. Any database present in MySQL Workbench will appear in the UI without hardcoding.

---

<img width="1908" height="869" alt="image" src="https://github.com/user-attachments/assets/a7182c4c-8fdf-4120-b644-9ff44bc0543a" />

---

<img width="1916" height="864" alt="image" src="https://github.com/user-attachments/assets/1e5c43a9-5631-4f68-a614-33447a763c4e" />

---

<img width="1919" height="862" alt="image" src="https://github.com/user-attachments/assets/ce9b5d11-9e9a-4c5c-ba17-6262bae6dc6b" />

---

<img width="1904" height="863" alt="image" src="https://github.com/user-attachments/assets/f86821da-3b5f-492f-ac87-c4b2db4b0a25" />

---

Users can:

• Select any database  
• Explore available tables  
• View complete schema (columns + data types)  
• Ask questions in plain English  
• Generate SQL queries  
• Execute them safely  
• Automatically correct query errors  
• Visualize results instantly  

This system simulates how AI-powered analytics tools would function in a real enterprise environment.

---

## 🏗️ System Architecture Philosophy

QueryMind is not just a UI wrapper around an LLM. It implements:

### 1️⃣ Schema Grounding
The selected database schema is injected into the LLM prompt before SQL generation. This:

- Reduces hallucinations
- Improves JOIN accuracy
- Enables multi-table reasoning
- Increases execution success rate

### 2️⃣ Secure Execution Guard
Before executing generated SQL:

- Only SELECT statements are allowed
- Destructive operations (DELETE, UPDATE, DROP) are blocked
- Query is cleaned and validated

This ensures database safety.

### 3️⃣ Self-Healing SQL Engine
If a query fails:

1. The database error message is captured
2. Error + original query + schema are sent back to the LLM
3. A corrected query is generated
4. The system retries execution automatically

This creates a resilient AI-assisted query engine.

---

## 🏗️ Pipeline Architecture

QueryMind follows a structured, multi-layer AI execution pipeline designed for safety, resilience, and schema grounding.

| Stage | Layer | Component | Responsibility | Key Output |
|-------|-------|-----------|----------------|------------|
| 1 | User Interface Layer | Streamlit UI (`app.py`) | Captures user natural language input and selected database | User query + selected DB |
| 2 | Metadata Layer | `db.py` | Dynamically fetches databases, tables, and schema from MySQL | Structured schema metadata |
| 3 | Context Engineering Layer | `prompt_builder.py` | Injects schema + user question into structured LLM prompt | Schema-grounded prompt |
| 4 | AI Reasoning Layer | `llm.py` (Ollama + Mistral) | Converts natural language into SQL query | Generated SQL |
| 5 | Security Validation Layer | `executor.py` (Pre-check) | Validates SQL (SELECT-only guard, sanitization) | Safe executable SQL |
| 6 | Execution Layer | MySQL Connector | Executes validated SQL against selected database | Query result / error |
| 7 | Resilience Layer | Auto-Correction Loop | If error occurs → feeds error + schema back to LLM | Corrected SQL |
| 8 | Data Processing Layer | Pandas | Formats results into structured dataframe | Clean dataset |
| 9 | Visualization Layer | Streamlit Charts | Auto-detects numeric columns & generates visualization | Interactive chart |
| 10 | Presentation Layer | UI Rendering | Displays SQL, explanation (optional), result table, chart | Final user output |

---

## 🔁 Error Recovery Sub-Pipeline

When execution fails, QueryMind activates a secondary correction loop:

| Step | Action | Description |
|------|--------|-------------|
| 1 | Capture Error | MySQL execution error message is extracted |
| 2 | Context Packaging | Error + Original SQL + Schema bundled |
| 3 | Regeneration | Mistral generates corrected SQL |
| 4 | Re-validation | SELECT-only guard re-applied |
| 5 | Re-execution | Corrected query executed |
| 6 | Final Response | Success result or final error displayed |

This creates a **self-healing AI SQL engine**.

---

## 🧠 Layered Architectural Model

QueryMind follows a multi-layer architecture:

| Architecture Layer | Purpose |
|--------------------|---------|
| Presentation Layer | User interaction & UI |
| Metadata Layer | Schema discovery & grounding |
| AI Reasoning Layer | Natural language → SQL conversion |
| Security Layer | Query validation & safety |
| Execution Layer | Database interaction |
| Resilience Layer | Error correction loop |
| Analytics Layer | Result processing & visualization |

---

## 🔐 Security & Governance Controls

| Control | Implementation |
|---------|---------------|
| Query Restriction | Only SELECT statements allowed |
| SQL Sanitization | Markdown & formatting cleaned before execution |
| Schema Grounding | Reduces hallucinated table references |
| Error Feedback Loop | Controlled retry mechanism |
| Local LLM Execution | No external API exposure |

---

## 📊 End-to-End Data Flow Summary

| Input | Transformation | Output |
|-------|---------------|--------|
| Natural Language | Schema-Grounded Prompt | SQL Query |
| SQL Query | Validation & Execution | Data Result |
| Data Result | Pandas Formatting | Structured Table |
| Structured Table | Auto Visualization | Chart Output |

---

## 🚀 Architectural Strengths

✔ Modular separation of concerns  
✔ AI reasoning isolated from execution layer  
✔ Built-in safety constraints  
✔ Automatic retry resilience  
✔ Dynamic database discovery  
✔ Local LLM inference (privacy-safe)  

---

## 🔥 Engineering Insight

QueryMind is designed as a layered AI system rather than a simple LLM wrapper.

It combines:

- Prompt Engineering
- Secure Systems Design
- Database Metadata Abstraction
- Error-Driven Regeneration
- Real-Time Data Visualization

into a cohesive pipeline.

---

## 🧠 AI Model Details

Model Used: Mistral  
Runtime: Ollama  
Deployment: Local  

Why Local LLM?
- No API cost
- Full data privacy
- Fast inference
- Offline capability

---

## 🗂 Modular Architecture

The project follows a clean modular design:

• app.py – UI & orchestration  
• db.py – Database metadata retrieval  
• executor.py – Secure query execution layer  
• prompt_builder.py – Schema-aware prompt generation  
• llm.py – Ollama (Mistral) integration  
• config.py – Database configuration  

This separation improves maintainability and scalability.

---

## 📊 Real-World Applications

QueryMind can be extended into:

• AI-powered BI dashboards  
• Conversational analytics tools  
• Enterprise SQL copilots  
• Internal data exploration assistants  
• Educational SQL tutors  

---

## 💼 Who Benefits From This?

### 🎓 Students
Learn SQL interactively using natural language.

### 📊 Data Analysts
Accelerate query writing and aggregation.

### 👨‍💻 Developers
Prototype complex joins quickly.

### 🏢 Organizations
Enable non-technical teams to query databases conversationally.

---

## 🧩 Key Engineering Strengths

✔ Multi-database support  
✔ Schema-aware LLM grounding  
✔ Self-healing SQL retry mechanism  
✔ Secure execution layer  
✔ Modular architecture  
✔ Local AI inference  
✔ Automatic visualization  
✔ Production-style workflow  

---

## 🚀 What Makes This Project Stand Out?

Most NL-to-SQL demos:
- Hardcode schema
- Lack safety guard
- Have no retry mechanism
- Do not handle real DB environments

QueryMind addresses these limitations and simulates a real-world AI SQL assistant system.

---

## 🔮 Future Scope

- PostgreSQL support
- Query optimization feedback
- Conversational memory
- Role-based access control
- Cloud deployment
- LLM fine-tuning on SQL datasets

---

## 📂 Project Structure

```
QueryMind/
│
├── app.py              # Streamlit UI (Main Application)
├── db.py               # Database connection & metadata retrieval
├── executor.py         # Secure SQL execution layer
├── llm.py              # Ollama (Mistral) integration
├── prompt_builder.py   # Schema-grounded prompt logic
├── config.py           # Database configuration
├── requirements.txt
├── SQL Generator App.bat
└── README.md
```

---

## 🔥 Core Features

### 1️⃣ Multi-Database Detection

QueryMind dynamically fetches all databases from MySQL server.

Any database present in MySQL Workbench automatically appears in the UI.

---

### 2️⃣ Table & Schema Explorer

Left-side panel shows:

- Database selector
- Table list
- Expandable schema
- Column names + data types

Improves query grounding and reduces hallucination.

---

### 3️⃣ Natural Language to SQL

Example:

Input:
```
Show total sales by country
```

Generated SQL:
```sql
SELECT c.country,
       SUM(od.quantityOrdered * od.priceEach) AS total_sales
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
GROUP BY c.country;
```

---

### 4️⃣ Self-Healing SQL Engine

If execution fails:

- Database error captured
- Error sent back to Mistral
- Corrected query generated
- Query automatically retried

---

### 5️⃣ Secure Execution Layer

- Only SELECT queries allowed
- Blocks DELETE / UPDATE / DROP
- Prevents destructive operations

---

### 6️⃣ Query Explanation Mode

Optional toggle to understand:

- JOIN logic
- Aggregations
- Query structure

---

### 7️⃣ Automatic Visualization

- Detects numeric columns
- Auto-generates charts
- Works for aggregation queries

---

## 🚀 How To Run

### 1️⃣ Start Ollama

```bash
ollama run mistral
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Application

```bash
streamlit run app.py
```

Or double-click:

```
SQL Generator App.bat
```

---

## 📬 Contact Details

For queries, contributions, or collaboration opportunities, feel free to reach out:

📧 **Email:** prathamsoni1128@gmail.com 

🔗 **LinkedIn:** https://www.linkedin.com/in/pratham-soni-600787268/

💻 **GitHub:** https://github.com/prathams0ni 

**QueryMind is more than a Natural Language to SQL tool —**  
it represents a practical implementation of **schema-aware AI reasoning, secure database interaction, and self-healing system design**.

> Turning databases into intelligent, conversational systems — one query at a time.

⭐ If you found this project interesting, consider giving it a star and connecting!
