# Text Emotion detector 
A python API that analyzes text and detects the dominant emotion using IBM Watson NLP services. 

It can classify emotions such as anger, disgust, fear, joy and sadness. 

1. API Rquirements:
  - You will need an IBM Cloud account.
  - Obtain your IBM Watson NLP API token and service URL.
  - Store your credentials in a .env file (or environment variables) for security:
        IBM_TOKEN=your_ibm_watson_token
        IBM_URL=your_ibm_service_url
  - important: Make sure .env is added to .gitignore to avoid expoisng your credentials on GitHub.
    
2. Usage:
   - The main application file is "server.py".
   - The deployment port is 5000
   - Once deployed, you can start typing text in the interface displayed.
     
3. Static code Analysis:
   - This project uses pylint for code quality check
   - Install pylint.
     
4. Python version
  - This project runs with Python 3.11
  - Make sure your environment matches to avoid compatibility issues.

### Credits
- The basis of this code comes from a cloned repository: https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai
- This is an adapted and extended version for personal use with IBM Watson NLP integration. 
   
