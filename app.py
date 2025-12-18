from flask import Flask, render_template, request, Response
from generator import generate_project_code

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    project_name = request.form.get('project_name', 'CoolProject')
    language = request.form.get('language', 'python')

    # AI se code mangwana
    code_content = generate_project_code(project_name, language)

    # Extension set karna
    ext = "py" if language.lower() == "python" else "js"
    
    return Response(
        code_content,
        mimetype="text/plain",
        headers={"Content-disposition": f"attachment; filename={project_name}.{ext}"}
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)