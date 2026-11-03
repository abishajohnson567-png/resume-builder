from flask import Flask, request, jsonify, render_template
import api, base64, os

app = Flask(__name__)
api.init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/resumes", methods=["GET"])
def list_resumes():
    return jsonify(api.get_all_resumes())

@app.route("/api/resumes", methods=["POST"])
def create_resume():
    body = request.json
    rid = api.save_resume(body["name"], body["data"], body.get("photo"))
    return jsonify({"id": rid, "message": "Resume saved!"}), 201

@app.route("/api/resumes/<int:rid>", methods=["GET"])
def get_resume(rid):
    r = api.get_resume(rid)
    return jsonify(r) if r else (jsonify({"error": "Not found"}), 404)

@app.route("/api/resumes/<int:rid>", methods=["PUT"])
def update_resume(rid):
    body = request.json
    api.update_resume(rid, body["name"], body["data"], body.get("photo"))
    return jsonify({"message": "Updated!"})

@app.route("/api/resumes/<int:rid>", methods=["DELETE"])
def delete_resume(rid):
    api.delete_resume(rid)
    return jsonify({"message": "Deleted!"})

if __name__ == "__main__":
    app.run(debug=True)
