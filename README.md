# Python-streamlit-groq
Milestone Generator
# PathFinder🔎: Task and Milestone Generator

## Description
PathFinder is a Streamlit-based application designed to help users break down complex tasks into simple, actionable milestones or steps. Powered by Groq's `llama3-8b-8192` model, it offers detailed and structured guidance for better productivity and goal achievement.

---

## Features
- **Task Breakdown**: Input any task, and PathFinder generates milestones in an easy-to-understand manner.
- **Interactive UI**: Utilize a user-friendly interface to input tasks and view detailed steps.
- **Versatile Usage**: Offers a console mode for offline or script-based use.

---

## Prerequisites
- Python 3.8+
- Required Python libraries:
  - `streamlit`
  - `dotenv`
  - `groq`

---

## Setup

### Environment Variables
Create a `.env` file in the root directory and include the following:
```plaintext
GROQ_API_KEY=your_api_key_here
```

### Install Dependencies
Install required libraries using pip:
```bash
pip install -r requirements.txt
```

---

## Usage
1. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

2. **Enter Task Description:**
   - Use the text area to input a task.
   - Click on the "Generate" button to view the breakdown into milestones.

3. **Optional Console Mode:**
   - Uncomment the `app_console()` call in the `main()` function to run the app in a terminal.

---

## File Structure
```
.
|-- python_ai.py          # Main application file
|-- .env                  # Environment variables (not included in the repo)
|-- requirements.txt      # Python dependencies
```

---

## Future Enhancements
- Add support for additional LLMs.
- Enable task prioritization and time estimation.
- Provide data export options for generated milestones.

---

## License
MIT License. See `LICENSE` for more details.

---

## Contributors
- [Abhishek Soni]
- [abhisheksoni7227@gmail.com]

