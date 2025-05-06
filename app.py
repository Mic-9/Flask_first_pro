from flask import Flask, render_template, redirect, request, url_for

app=Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nome=request.form.get('nome')
        return redirect(url_for("saluto", nome=nome))
    else:
        return render_template("index.html")


@app.route('/saluto')
def saluto():
    if request.method == 'GET':
        nome=request.args.get('nome')
        return render_template("saluto.html", nome=nome)
    else:
        return redirect(url_for("home"))

@app.route('/about')
def about():
    return render_template("about.html")



if __name__ == '__main__':
    app.run(debug=True)