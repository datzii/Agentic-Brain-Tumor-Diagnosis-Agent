# Agentic Brain Tumor Diagnosis Agent
AI Agent for classification and detection of brain tumor

## 🚀 Getting Started

### 1. Create a Virtual Environment and Install Dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Set Environment Variables

Edit the `.env` file with the appropriate values:
- `LITELLM_ENDPOINT`: The endpoint of LiteLLM
- `LITELLM_MASTER_KEY`: The LiteLLM master key

### 3. Human In The Loop Testing

```bash
cd src
python -m testing.loop_agent
```

### 4. Start AI Agent
```bash
cd src
python main.py
```