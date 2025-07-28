# Cold Email Outreach Agent

A Python-based agent that automates cold outreach to AI startups. It generates personalized emails using GPT-4 and sends them with Gmail via SMTP. Designed for junior AI/ML job applications.

### Features
- Uses OpenAI's GPT-4 to generate natural emails
- Reads a CSV of target companies
- Sends emails via Gmail (app password required)
- Attaches your CV and includes your GitHub

### How it works
You feed it a CSV like this:

```csv
company_name,recruitment_email,company_info
TestAI,test@example.com,LLM-powered assistants for legal teams
