from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask is running inside Docker!"

@app.route("/status/github")
def github_status():
    try:
        response = requests.get("https://www.githubstatus.com/api/v2/status.json")
        data = response.json()
        return {
            "github_status": data["status"]["description"],
            "status": "operational" if data["status"]["indicator"] == "none" else "down"
        }
    except Exception as e:
        return {"error": str(e), "status": "down"}

# Commenting out the Jenkins status check for now
# @app.route("/status/jenkins")
# def jenkins_status():
#     try:
#         response = requests.get("http://your-jenkins-instance/api/json")
#         data = response.json()
#         return {
#             "jenkins_status": data["status"],
#             "status": "operational" if data["status"] == "healthy" else "down"
#         }
#     except Exception as e:
#         return {"error": str(e), "status": "down"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
