from flask import Flask, render_template, request

app = Flask(__name__)

# Function to calculate the unknowns based on provided data
def calculate_unknowns(data):
    # Perform calculations here based on provided data
    # Sample calculation for demonstration
    T_H_OUT = 100  # Replace this with actual calculated value
    T_C_OUT = 50   # Replace this with actual calculated value
    return T_H_OUT, T_C_OUT

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            data = {
                'T_H_IN': float(request.form['T_H_IN']),
                'T_C_IN': float(request.form['T_C_IN']),
                'm_dot_H': float(request.form['m_dot_H']),
                'm_dot_C': float(request.form['m_dot_C']),
                'UA': float(request.form['UA'])
            }
            T_H_OUT, T_C_OUT = calculate_unknowns(data)
            return render_template('result.html', T_H_OUT=T_H_OUT, T_C_OUT=T_C_OUT)
        except Exception as e:
            error_message = str(e)
            return render_template('error.html', error_message=error_message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
