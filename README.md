The "Big Picture" Goal
I have built a Production Data Pipeline. Instead of just a script on laptop, i have a cloud-hosted system that manages Secret Credentials, Automated Scheduling, and Versioned Data Storage.

Step 1: The Engineering ( Mac)The Script: I wrote fetch_market_data.py. It pulls NVIDIA stock data via an API.The Fallback: I added yfinance so that if one API fails (or hits a rate limit), the pipeline stays alive.The Environment: used a venv and a .gitignore to keep the project professional and isolated.Security: used a .env file to hide your API keys locally.

Step 2: The "Ops" (GitHub Infrastructure)Secret Management: I moved your API Key into GitHub Secrets. This allows the cloud to use my key without ever showing it to the public.

The Workflow (.yml): I created a set of instructions that tells GitHub:Wake up a virtual computer.Install Python and the libraries (pandas, requests, yfinance).Run the script to get the latest data.The Write-Back: I configured Permissions and used the git-auto-commit-action to allow that virtual computer to save the data back into your repository automatically.

Step 3: The Deployment (The Cloud)Automation: The script is now set to run every night at midnight.Future-Proofing: I updated my infrastructure to Node.js 24 standards to ensure it doesn't break when GitHub updates its systems later this year.

Next: the "Moving Average" script to start visualizing the trends in your new CSV?
