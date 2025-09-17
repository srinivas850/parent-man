# University Policies AI Assistant for Parents

A Flask-based web application that provides an AI-powered assistant to help parents understand university policies and procedures.

## Features

- **Interactive Web Interface**: Clean, user-friendly web interface for asking questions
- **AI-Powered Responses**: Uses OpenAI's GPT models to provide accurate answers
- **Knowledge Base**: Pre-built knowledge base from university policy documents
- **Fast Search**: FAISS-powered vector search for quick retrieval
- **Logging**: Comprehensive logging for monitoring and debugging

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- OpenAI API key

### 2. Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements_new.txt
   ```

### 3. Configuration

1. Create a `.env` file in the root directory:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   Replace `your_openai_api_key_here` with your actual OpenAI API key.

### 4. Data Ingestion

Run the data ingestion script to build the knowledge base:
```bash
python ingest_data.py
```

This will:
- Load policy documents from the `data/` directory
- Create embeddings using sentence transformers
- Build a FAISS index for fast retrieval

### 5. Run the Application

Start the Flask server:
```bash
python run_app.py
```

Or run directly:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage

1. Open your web browser and navigate to `http://localhost:5000`
2. Enter your question about university policies in the text field
3. Click "Ask" to get an AI-powered response
4. The assistant will provide relevant information based on the university policy documents

## Project Structure

```
├── app.py                 # Main Flask application
├── run_app.py            # Application runner script
├── query_agent.py        # AI query processing logic
├── ingest_data.py        # Data ingestion and indexing
├── test_query.py         # Testing script
├── requirements_new.txt  # Python dependencies
├── .env                  # Environment variables (create this)
├── templates/
│   └── index.html        # Web interface template
├── data/                 # University policy documents
│   ├── admission_policies.txt
│   ├── financial_aid.txt
│   ├── academic_policies.txt
│   ├── support_resources.txt
│   ├── academic_calendar.txt
│   └── housing_policies.txt
├── faiss_index/          # Generated FAISS index (created by ingest_data.py)
└── README.md            # This file
```

## API Endpoints

- `GET /`: Main web interface
- `POST /api/query`: API endpoint for queries
  - Request body: `{"question": "Your question here"}`
  - Response: `{"answer": "AI-generated answer"}`

## Troubleshooting

### Common Issues

1. **"FAISS index not found" error**
   - Run `python ingest_data.py` to build the knowledge base

2. **"OpenAI API key not found" error**
   - Ensure your `.env` file contains a valid `OPENAI_API_KEY`

3. **Import errors**
   - Make sure all dependencies are installed: `pip install -r requirements_new.txt`

4. **Port already in use**
   - The app runs on port 5000 by default. Change the port in `app.py` if needed.

### Logs

Check the console output for detailed logs. The application logs:
- Incoming queries
- Processing steps
- Any errors encountered

## Development

### Adding New Policy Documents

1. Add new `.txt` files to the `data/` directory
2. Run `python ingest_data.py` to update the knowledge base
3. Restart the application

### Testing

Run the test script to verify functionality:
```bash
python test_query.py
```

## License

This project is provided as-is for educational and demonstration purposes.

## Support

For issues or questions, please check the troubleshooting section above or examine the application logs for more details.
