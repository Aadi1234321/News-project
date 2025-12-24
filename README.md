# Nexus News Platform

Nexus News is a next-generation, multi-purpose news site designed for high engagement and modern aesthetics. It features a dual-interface for readers and professional journalists.

## Features
- **Dynamic News Feed**: Location-based (area) and category-based filtering.
- **Rich Media**: Full support for high-resolution images and videos in articles.
- **Journalist Portal**: A dedicated secure upload form for journalists to submit reports with media.
- **Ultra-Modern UI**: Glassmorphic design, dark mode, vibrant neon accents, and smooth animations.

## How to Run
1. Ensure Python is installed.
2. The project uses a virtual environment already set up in `.venv`.
3. Start the server:
   ```bash
   .\.venv\Scripts\python.exe app.py
   ```
4. Open your browser and navigate to:
   `http://127.0.0.1:5000`

## Core Directory Structure
- `app.py`: Main Flask application and database logic.
- `static/`: Contains images, CSS, and JS.
- `templates/`: HTML templates for Home, News Detail, and Upload.
- `uploads/`: Directory where journalist-uploaded media is stored.
- `news.db`: SQLite database for persistent storage.

## Seeding Initial Data
If you want to reset and seed the database with demo content:
```bash
.\.venv\Scripts\python.exe seed_db.py
```
