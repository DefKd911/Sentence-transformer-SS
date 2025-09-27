# 🚀 Render Deployment Steps

## ✅ **Current Status**
- ✅ Git repository initialized
- ✅ All files committed
- ✅ Virtual environment activated
- ✅ Dependencies installed
- ✅ Ready for deployment

## 📋 **Step-by-Step Render Deployment**

### Step 1: Push to GitHub
```bash
# Add remote repository (replace with your GitHub repo URL)
git remote add origin https://github.com/yourusername/your-repo-name.git

# Push to GitHub
git push -u origin main
```

### Step 2: Deploy on Render
1. **Go to**: https://render.com
2. **Sign up** with GitHub account
3. **Click "New +"** → **"Web Service"**
4. **Connect your GitHub repository**

### Step 3: Configure Render Service
- **Name**: `semantic-similarity-api`
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements_deploy.txt`
- **Start Command**: `gunicorn app:app`
- **Python Version**: `3.10.0`

### Step 4: Deploy
1. **Click "Create Web Service"**
2. **Wait for deployment** (5-10 minutes)
3. **Get your URL**: `https://your-app-name.onrender.com`

## 🧪 **Test Your Deployment**

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

## 📝 **Expected Results**

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

## ✅ **Ready for Deployment!**

Your semantic similarity API is now ready for Render deployment and DataNeuron assignment submission!
