# 🔧 OpenAI API Configuration Guide

## Method 1: Using .env file (Recommended)

1. **Create a .env file** in your project root:
```bash
# Create .env file
touch .env
```

2. **Add your API key** to the .env file:
```bash
OPENAI_API_KEY=sk-your-actual-api-key-here
```

3. **Get your API key**:
   - Go to [OpenAI Platform](https://platform.openai.com/api-keys)
   - Sign up or log in
   - Click "Create new secret key"
   - Copy the key (starts with `sk-`)

## Method 2: Environment Variable

### Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="sk-your-actual-api-key-here"
```

### Windows (Command Prompt):
```cmd
set OPENAI_API_KEY=sk-your-actual-api-key-here
```

### Linux/Mac:
```bash
export OPENAI_API_KEY="sk-your-actual-api-key-here"
```

## Method 3: Direct in App

1. Run the app: `streamlit run optantra.py`
2. Go to the sidebar
3. Enter your API key in the "OpenAI API Key" field
4. The key will be saved for the session

## Method 4: System Environment Variables

### Windows:
1. Search for "Environment Variables"
2. Click "Edit the system environment variables"
3. Click "Environment Variables"
4. Under "User variables", click "New"
5. Variable name: `OPENAI_API_KEY`
6. Variable value: `sk-your-actual-api-key-here`

### Linux/Mac:
Add to your `~/.bashrc` or `~/.zshrc`:
```bash
echo 'export OPENAI_API_KEY="sk-your-actual-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

## 🔍 Troubleshooting

### Common Issues:

1. **"Invalid API key" error**:
   - Make sure your key starts with `sk-`
   - Check for extra spaces or characters
   - Verify the key is active in your OpenAI account

2. **"No API key found" error**:
   - Ensure the .env file is in the same directory as optantra.py
   - Check that python-dotenv is installed: `pip install python-dotenv`
   - Restart the app after adding the key

3. **"Rate limit exceeded" error**:
   - Check your OpenAI account credits
   - Wait a few minutes before trying again
   - Consider upgrading your OpenAI plan

4. **"Module not found" error**:
   - Install dependencies: `pip install -r requirements.txt`
   - Or install manually: `pip install openai python-dotenv streamlit`

### Testing Your Configuration:

Run this test script to verify your API key works:

```python
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello!"}],
        max_tokens=10
    )
    print("✅ API key is working!")
except Exception as e:
    print(f"❌ Error: {e}")
```

## 💰 OpenAI Pricing

- **GPT-3.5-turbo**: ~$0.002 per 1K tokens
- **Free tier**: $5 credit for new users
- **Paid plans**: Starting at $20/month

## 🔒 Security Notes

- Never commit your API key to version control
- Use .env files (already in .gitignore)
- Rotate your API keys regularly
- Monitor your usage in OpenAI dashboard 