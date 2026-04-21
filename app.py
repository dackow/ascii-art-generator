from flask import Flask, render_template, request
import pyfiglet

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    ascii_art = None
    user_text = ""
    selected_font = "standard"
    
    if request.method == 'POST':
        user_text = request.form.get('text', '')
        selected_font = request.form.get('font', 'standard')
        
        try:
            # Generate ASCII art using the selected font
            fig = pyfiglet.Figlet(font=selected_font)
            ascii_art = fig.renderText(user_text)
        except Exception as e:
            ascii_art = f"Error generating ASCII art: {str(e)}"

    return render_template('index.html', 
                           ascii_art=ascii_art, 
                           user_text=user_text, 
                           selected_font=selected_font)

if __name__ == '__main__':
    app.run(debug=True)
