from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
def pass_strength(password):
    a = [0,0,0,0,0]
    if len(password) >= 8:
        a[4] =1
    for c in password:
        if (not c.isalnum()) and a[0]==0:
            
            a[0]=1
        if c.isnumeric() and a[1]==0:
            
            a[1]=1
        if c.isupper() and a[2]==0:
            
            a[2]=1
        if c.islower() and a[3]==0:
            
            a[3]=1
    if sum(a)==5:
        return "Very Strong"
    elif sum(a)==4:
        return "Strong"
    elif sum(a)==3:
        return "Moderate"
    elif sum(a)==2:
        return "Weak"
    else:
        return "Very Weak"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_strength', methods=['POST'])
def check_strength():
    data = request.get_json()
    password = data.get('password', '')
    rating = pass_strength(password)
    return jsonify({'strength': rating})

if __name__ == "__main__":
    app.run(debug=True, port=5050)