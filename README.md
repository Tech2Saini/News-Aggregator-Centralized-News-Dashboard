# News Aggregator – Centralized News Dashboard

**Project Type:** Python / Django Web Application  
**Status:** Completed  

---

## Overview
The **News Aggregator** is a web platform that collects news articles from multiple sources and presents them in a single, organized dashboard. Users can access real-time news from sources like **NDTV, Aaj Tak, and Times of India** without visiting each site individually.  

The system is built using **Python** and **Django**, with web scraping, custom APIs, and database integration to ensure a seamless news aggregation experience.

---

## Features
- Aggregate news from multiple sources using **custom-built APIs**  
- Scrape content using **BeautifulSoup** and **Requests**  
- Store aggregated news in a database for quick access  
- Categorize news by topics like politics, technology, sports, etc.  
- Display all news in a **centralized dashboard** with links to original articles  
- Real-time updates for latest news  

---

## Technology Stack
- **Backend:** Python, Django  
- **Web Scraping:** BeautifulSoup, Requests  
- **Database:** SQLite / PostgreSQL  
- **APIs:** Custom-built APIs for news collection  
- **Frontend:** HTML, CSS, Django templates  

---

## Project Structure
```text
news_aggregator/
├── aggregator/          # Core Django app
│   ├── models.py        # Database models for articles and categories
│   ├── views.py         # Handles views and dashboard rendering
│   ├── urls.py          # URL routes
│   └── templates/       # HTML templates for dashboard
├── scraper/             # Web scraping scripts
│   └── scraper.py
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Installation Process
#### Clone the repository
git clone https://github.com/tech2saini/news-aggregator.git
cd news-aggregator

#### Create and activate a virtual environment
python -m venv venv
### On Linux/Mac
source venv/bin/activate
### On Windows
venv\Scripts\activate

#### Install dependencies
pip install -r requirements.txt

#### Apply database migrations
python manage.py migrate

#### Run the development server
python manage.py runserver

#### Open in browser
#### Visit http://127.0.0.1:8000/

## Usages
- View aggregated news from multiple sources on the dashboard
- Click on any article to read the full content on the original site
- Use categories to filter news based on topics

## Contributions 
- Fork the repository and create a feature branch
- Make your changes and test thoroughly
- Submit a pull request for review

## Lisence
This project is open-source and licensed under the MIT License.


✅ This version wraps **everything** — including structure, installation commands, usage instructions, contributions, enhancements, and license — in **proper Markdown/code blocks** for GitHub.  

If you want, I can also **add badges, screenshots, and a Table of Contents** inside this same Markdown code block so it looks fully professional on GitHub. Do you want me to do that next?


