from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from ice_breaker import ice_break_with



load_dotenv()

app = Flask(__name__)


@app.route('/')
def ice_breaker():
   return render_template('index.html')

@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary, profile_pic_url = ice_break_with(name)
    print(summary.to_dict())
    print(profile_pic_url)
    print("done")
    return jsonify({"summary_and_facts": summary.to_dict(), "profile_pic_url": profile_pic_url})

if __name__ == '__main__':
    
    app.run(host="0.0.0.0", port=5000, debug=True)