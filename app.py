# app.py

from flask import Flask, request, render_template, jsonify
from sentence_transformers import SentenceTransformer, util

app = Flask(__name__)

# Load the model once when the application starts
print("Loading all-MiniLM-L6-v2 model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded successfully.")

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Handles both displaying the form (GET) and processing the
    form submission (POST).
    """
    score = None
    text1 = ""
    text2 = ""
    
    if request.method == "POST":
        text1 = request.form.get("text1", "").strip()
        text2 = request.form.get("text2", "").strip()
        
        if text1 and text2:
            # --- KEY CHANGE: Prediction logic for Sentence-Transformers ---
            # 1. Encode both texts into embeddings
            embeddings = model.encode([text1, text2], convert_to_tensor=True)
            # 2. Compute cosine similarity
            cosine_score = util.cos_sim(embeddings[0], embeddings[1])
            score = f"{cosine_score.item():.4f}"
            
    return render_template("index.html", similarity_score=score, text1=text1, text2=text2)

@app.route('/similarity', methods=['POST'])
def calculate_similarity():
    """
    API endpoint to calculate semantic similarity between two texts.
    
    Expected request format:
    {
        "text1": "First text paragraph",
        "text2": "Second text paragraph"
    }
    
    Response format:
    {
        "similarity score": 0.75
    }
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        # Extract text1 and text2 from request
        text1 = data.get('text1', '')
        text2 = data.get('text2', '')
        
        if not text1 or not text2:
            return jsonify({"error": "Both text1 and text2 are required"}), 400
        
        # Calculate similarity using sentence transformers
        # 1. Encode both texts into embeddings
        embeddings = model.encode([text1, text2], convert_to_tensor=True)
        # 2. Compute cosine similarity
        cosine_score = util.cos_sim(embeddings[0], embeddings[1])
        similarity_score = cosine_score.item()
        
        # Return response in the required format
        response = {
            "similarity score": round(similarity_score, 4)
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify the API is running.
    """
    return jsonify({
        "status": "healthy",
        "model_loaded": model is not None
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)