# Resume Builder Application

## Project Structure
```
resume_builder/
├── app.py              # Flask app (routes + server)
├── api.py              # Database API (SQLite CRUD)
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Main application UI
└── static/
    └── css/
        └── style.css   # All styling
```

## Setup & Run

1. Install Python 3.8+

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python app.py
```

4. Open browser at: http://localhost:5000

## Features
- **Photo Upload** — Add profile photo to resume
- **11 Sections** — Basics, Summary, Experience, Education, Skills, Projects, Certifications, Languages, Interests, References, Design
- **Live Preview** — See changes in real time
- **5 Color Themes** — Midnight Gold, Navy, Forest, Burgundy, Slate
- **3 Font Styles** — Classic Serif, Modern Sans, Minimal Mono
- **2 Layouts** — Two Column / Full Width
- **Save / Load** — SQLite database via REST API
- **Print / PDF** — Browser print dialog

## API Endpoints
| Method | URL | Description |
|--------|-----|-------------|
| GET | /api/resumes | List all resumes |
| POST | /api/resumes | Create new resume |
| GET | /api/resumes/:id | Get one resume |
| PUT | /api/resumes/:id | Update resume |
| DELETE | /api/resumes/:id | Delete resume |
