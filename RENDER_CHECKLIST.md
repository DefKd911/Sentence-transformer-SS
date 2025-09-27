# Render Deployment Checklist

## ✅ **Pre-Deployment Checklist**

### 1. Files Ready
- [x] `app.py` - Main Flask application
- [x] `requirements_deploy.txt` - Dependencies
- [x] `render.yaml` - Render configuration
- [x] `templates/index.html` - Web interface
- [x] `test_render.py` - Testing script

### 2. GitHub Repository
- [ ] Push all files to GitHub
- [ ] Repository is public (for free Render tier)
- [ ] All files are in root directory

## 🚀 **Render Deployment Steps**

### Step 1: Create Render Account
1. Go to https://render.com
2. Sign up with GitHub
3. Authorize Render to access your repositories

### Step 2: Deploy Web Service
1. Click **"New +"** → **"Web Service"**
2. **Connect GitHub repository**
3. **Configure service**:
   - **Name**: `semantic-similarity-api`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements_deploy.txt`
   - **Start Command**: `gunicorn app:app`
   - **Python Version**: `3.10.0`

### Step 3: Deploy
1. Click **"Create Web Service"**
2. Wait for deployment (5-10 minutes)
3. Get your URL: `https://your-app-name.onrender.com`

## 🧪 **Testing Your Deployment**

### Quick Test
```bash
# Test health endpoint
curl https://your-app-name.onrender.com/health

# Test similarity endpoint
curl -X POST https://your-app-name.onrender.com/similarity \
  -H "Content-Type: application/json" \
  -d '{"text1": "nuclear body seeks new tech", "text2": "terror suspects face arrest"}'
```

### Python Test Script
```bash
python test_render.py
# Enter your Render URL when prompted
```

## 📋 **Expected Results**

### Health Check Response
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### Similarity Response
```json
{
  "similarity score": 0.2
}
```

## ⚠️ **Render Free Tier Notes**

- **First request** after sleep takes 30+ seconds
- **Subsequent requests** are fast
- **Sleeps after 15 minutes** of inactivity
- **750 hours/month** limit (usually enough)

## 🎯 **For Assignment Submission**

1. **Deploy to Render** ✅
2. **Test API works** ✅
3. **Get live URL** ✅
4. **Submit URL** with assignment

## 📞 **Your Live API Endpoint**

Once deployed, your API will be available at:
- **Base URL**: `https://your-app-name.onrender.com`
- **Similarity**: `https://your-app-name.onrender.com/similarity`
- **Health**: `https://your-app-name.onrender.com/health`
- **Web Interface**: `https://your-app-name.onrender.com/`

## ✅ **Ready for Submission!**

Your semantic similarity API is now ready for the DataNeuron assignment submission!
