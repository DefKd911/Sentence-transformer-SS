# Render Deployment Guide for DataNeuron Assignment

## 🚀 **Deploy to Render (Free)**

### Step 1: Prepare Your Repository
1. **Push all files to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit for DataNeuron assignment"
   git branch -M main
   git remote add origin https://github.com/yourusername/your-repo-name.git
   git push -u origin main
   ```

### Step 2: Deploy on Render
1. **Go to Render**: https://render.com
2. **Sign up** with GitHub account
3. **Click "New +"** → **"Web Service"**
4. **Connect your GitHub repository**
5. **Configure the service**:

### Step 3: Render Configuration
- **Name**: `semantic-similarity-api`
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements_deploy.txt`
- **Start Command**: `gunicorn app:app`
- **Python Version**: `3.10.0`

### Step 4: Environment Variables (Optional)
- **PYTHON_VERSION**: `3.10.0`
- **PORT**: `10000` (Render sets this automatically)

### Step 5: Deploy
1. **Click "Create Web Service"**
2. **Wait for deployment** (5-10 minutes)
3. **Get your URL**: `https://your-app-name.onrender.com`

## 🧪 **Test Your Deployed API**

### Health Check
```bash
curl https://your-app-name.onrender.com/health
```

### Similarity Test
```bash
curl -X POST https://your-app-name.onrender.com/similarity \
  -H "Content-Type: application/json" \
  -d '{"text1": "nuclear body seeks new tech", "text2": "terror suspects face arrest"}'
```

**Expected Response:**
```json
{"similarity score": 0.2}
```

## 📋 **Render Free Tier Limits**
- ✅ **750 hours/month** (usually enough for demos)
- ✅ **Automatic deployments** from GitHub
- ✅ **Custom domains** supported
- ✅ **HTTPS** enabled by default
- ⚠️ **Sleeps after 15 minutes** of inactivity (wakes up on request)

## 🔧 **Troubleshooting**

### If deployment fails:
1. **Check logs** in Render dashboard
2. **Verify requirements_deploy.txt** has all dependencies
3. **Ensure app.py** is in root directory
4. **Check Python version** is 3.10

### If API is slow to respond:
- **First request** after sleep takes ~30 seconds
- **Subsequent requests** are fast
- **This is normal** for free tier

## 📝 **For Assignment Submission**

1. **Deploy to Render** using steps above
2. **Test your API** works correctly
3. **Get your live URL**: `https://your-app-name.onrender.com`
4. **Submit the URL** with your assignment

## 🎯 **Final API Endpoint**

Your deployed API will be available at:
- **Base URL**: `https://your-app-name.onrender.com`
- **Similarity**: `https://your-app-name.onrender.com/similarity`
- **Health**: `https://your-app-name.onrender.com/health`
- **Web Interface**: `https://your-app-name.onrender.com/`

## ✅ **Ready for Submission**

Once deployed, you'll have:
- ✅ Live API endpoint
- ✅ Correct request/response format
- ✅ Working semantic similarity
- ✅ Health check endpoint
- ✅ Web interface for testing
