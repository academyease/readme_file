**to Build a Production-Ready Code Reviewer Agent with Streamlit Interface**
You are an expert in building AI Agent-based solutions, and I need your help in developing a **Code Reviewer Agent** for production-level code review tasks.
Objective:
To build a **Code Reviewer Agent** that can:
* Accept a `.py` file as input (especially Agentic AI code),
* Analyze and review the code,
* The agent should execute the uploaded `.py` file in a controlled environment using a Code Executor tool. It must validate whether the code runs correctly, detect and report any runtime or logical errors, and generate clear diagnostics to aid in debugging and further improvements.                                                             for POC/demo purposes:
   * `subprocess` module in Python (safe but limited): It allows us to execute the Python file in a subprocess, and capture:
      * Standard output (`stdout`)
      * Errors and exceptions (`stderr`)
      * Exit status
* Detect errors or required improvements,
* Modify and re-test the updated code automatically,                                                     After running the code:
   * If **errors are found**, the agent will:
      * Analyze them using Azure OpenAI (e.g., `"Why is this error happening and how to fix it?"`)
      * Suggest or auto-modify the code
      * Re-run the modified version
   * Logs, diffs, and results will be stored as **artifacts**.
* Generate detailed **logs**, **artifacts**, and **recommendations**,
* Display findings, modified code, and artifacts in a **simple Streamlit UI** under the uploaded file section.
Tech Stack and Requirements:
* **Model**: Azure OpenAI (with `.env` containing endpoint, API key, deployment name, and version),
* **Framework**: LangGraph (to manage agent workflows),
* **Interface**: Streamlit (for file upload and visualization),
* The solution should be built for **production-level** code review, not just basic scripts.
Deliverables:
* A **Proof of Concept (PoC)** implementation,
* Production-ready, modular, and well-commented code,
* A working Streamlit app with:
   * File upload capability,
   * Display of reviewed code, errors found, suggestions, updated code, and logs/artifacts.
Please include inline **comments** in your code to explain the logic and steps for better understanding and future scalability.     please write comments .env file folder structure  openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")
DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT")
