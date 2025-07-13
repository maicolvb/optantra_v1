# 🚀 Complete Setup Guide for Windows

## Step 1: Install Python

### Option A: Microsoft Store (Easiest)
1. Open Microsoft Store
2. Search for "Python 3.11" or "Python 3.12"
3. Click "Install"
4. Wait for installation to complete

### Option B: Official Python Website
1. Go to [python.org](https://www.python.org/downloads/)
2. Download Python 3.11 or 3.12 for Windows
3. Run the installer
4. **IMPORTANT**: Check "Add Python to PATH" during installation
5. Click "Install Now"

### Verify Python Installation
Open PowerShell and run:
```powershell
python --version
```
You should see something like: `Python 3.11.x`

## Step 2: Install Dependencies

Open PowerShell in your project directory and run:
```powershell
# Install pip if not available
python -m ensurepip --upgrade

# Install required packages
pip install streamlit openai python-dotenv
```

## Step 3: Get OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create an account or sign in
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)
5. Save it securely

## Step 4: Configure API Key

### Method 1: Create .env file (Recommended)
1. In your project folder, create a file named `.env`
2. Add this line to the file:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
```
3. Replace `sk-your-actual-api-key-here` with your real API key

### Method 2: Environment Variable
In PowerShell, run:
```powershell
$env:OPENAI_API_KEY="sk-your-actual-api-key-here"
```

### Method 3: In the App
1. Run the app: `streamlit run optantra.py`
2. Enter your API key in the sidebar

## Step 5: Test Configuration

Run the test script:
```powershell
python test_api.py
```

## Step 6: Run the App

```powershell
streamlit run optantra.py
```

## 🔧 Troubleshooting

### "Python not found" error:
- Make sure Python is installed and added to PATH
- Try restarting PowerShell after installation
- Use `py` instead of `python` on some Windows systems

### "pip not found" error:
```powershell
python -m ensurepip --upgrade
```

### "Module not found" error:
```powershell
pip install -r requirements.txt
```

### API Key issues:
- Make sure the key starts with `sk-`
- Check that you have credits in your OpenAI account
- Verify the key is active in your OpenAI dashboard

## 📁 File Structure
Your project should look like this:
```
optantra_v1/
├── optantra.py          # Main app
├── requirements.txt     # Dependencies
├── .env                 # Your API key (create this)
├── test_api.py         # Test script
├── config_guide.md     # Configuration guide
└── setup_guide.md      # This file
```

## 🎯 Quick Start Commands

Copy and paste these commands in order:

```powershell
# 1. Install dependencies
pip install streamlit openai python-dotenv

# 2. Test API (after adding your key)
python test_api.py

# 3. Run the app
streamlit run optantra.py
```

## 💡 Tips

- Keep your API key secure and never share it
- The app will work even without an API key (basic mode)
- You can get $5 free credit when you sign up for OpenAI
- Monitor your usage in the OpenAI dashboard 