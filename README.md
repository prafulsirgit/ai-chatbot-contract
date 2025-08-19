# AI Chatbot Contract

An AI-powered chatbot for interacting with documents (e.g., contracts) using vector-based search and retrieval. The system processes documents, builds a vector database, and enables conversational querying through a simple UI.

---

## 🚀 Features

* Upload and process documents (PDF, text).
* Create and manage a vector database for semantic search.
* Chat interface powered by AI for contract/document Q\&A.
* Modular Python backend with a lightweight UI (`edbot-ui`).

---

## 📦 Requirements

* Python **3.9+**
* Node.js **16+** (for UI, if needed)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Setup & Run

### 1. Clone the Repository

```bash
git clone https://github.com/prafulsirgit/ai-chatbot-contract.git
cd ai-chatbot-contract
```

### 2. Prepare Data

Place your documents (PDF, TXT, etc.) in the `data/` folder.

### 3. Create Vector Database

```bash
python create_vector_db.py
```

This will process documents and store embeddings for retrieval.

### 4. Start the Backend Server

```bash
python server.py
```

The API will be available at:

```
http://localhost:5000
```

### 5. Run the UI (Optional)

If using the UI inside `edbot-ui/`:

```bash
cd edbot-ui
npm install
npm start
```

Access at:

```
http://localhost:3000
```

---

## 📖 Usage

1. Upload/keep contracts in `data/`.
2. Run the vector DB script to index them.
3. Start the server.
4. Open the UI and chat with the bot about your documents.

---

## 📂 Project Structure

```
ai-chatbot-contract/
│── data/                  # Store your documents
│── edbot-ui/              # Frontend UI
│── app.py                 # Entry point (optional run)
│── server.py              # Backend server
│── create_vector_db.py    # Build vector DB from documents
│── document_processor.py  # Preprocess documents
│── chains.py              # Defines chatbot workflows
│── vector_store.py        # Vector storage logic
│── requirements.txt       # Python dependencies
```

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.
