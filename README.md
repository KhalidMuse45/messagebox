🎬 AI Movie Recommendation Platform

A personalized movie recommendation website that uses your Letterboxd watch history and the Gemini 3 API to suggest films tailored to your taste.

By analyzing the movies you’ve already watched, the platform generates recommendations that go beyond generic ratings and trends.

🚀 How It Works

Export your Letterboxd data
Download your data from Letterboxd and locate the watched.csv file.

Upload your watch history
Upload the watched.csv file to the website.

Get recommendations
The platform analyzes your viewing history using the Gemini 3 API and returns 3 personalized movie recommendations.

✨ Features

Personalized recommendations based on real watch history

No account or login required

Simple CSV upload workflow

AI-powered suggestions using Gemini 3

Privacy-focused (no data storage)

🛠 Tech Stack

Frontend: TBD

Backend: TBD

AI: Gemini 3 API

Data Input: Letterboxd watched.csv

📂 Data Requirements

This project requires the watched.csv file from Letterboxd’s official data export.

Only watched.csv is used. Other files in the export are ignored.

⚙️ Setup & Installation
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
npm install
npm run dev


Create a .env file in the root directory and add your API key:

GEMINI_API_KEY=your_api_key_here

🧪 Usage

Run the application locally or visit the deployed site

Upload your watched.csv file

Receive 3 AI-generated movie recommendations

🔒 Privacy

Uploaded data is used only during the session

No data is stored or shared

No direct connection to your Letterboxd account
