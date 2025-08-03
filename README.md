# Court-Case-Fetcher-Dashboard
A lightweight Flask-based web application that allows users to fetch **live case details from the Indian District Court Portal (eCourts)** using case number, type, and year.  
✅ No CAPTCHA bypassing   
✅ No scraping   
✅ Fully legal — uses public API requests


##  Court Chosen
**Delhi District Court – Tis Hazari**

- Official Portal: [https://services.ecourts.gov.in/ecourtindia_v6/](https://services.ecourts.gov.in/ecourtindia_v6/)
- State Code: `07` (Delhi)
- District Code: `3` (Tis Hazari)
- Court Code: `1` (Example Trial Court)

##  Features

- Input form for case type, number, and year
- Sends structured POST requests to public eCourts backend
- Displays JSON results for matching case
- Logs each user query to SQLite database
- Simple responsive HTML UI using Jinja2
- Docker support


##  Setup Instructions

###  1. Clone the repo
git clone https://github.com/Ishika446/court-case-fetcher.git
cd court-case-fetcher

## CAPTCHA & Legal Disclaimer

- This project uses only the public case query endpoint from the Indian eCourts portal.
- No CAPTCHA bypassing, credential-based access, or scraping is performed.
- Data is fetched one case at a time, mimicking manual form usage.
- Intended for educational and demo purposes only.

 ## Tech Stack

- Backend: Flask (Python)
- Requests library for court API calls
- SQLite for logging queries
- HTML/CSS + Jinja2 for frontend
- Docker 

## License
- This project is licensed under the MIT License.
- You are free to use, modify, and distribute — but please do not misuse public court data.
