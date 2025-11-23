from flask import Flask , render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station , date):
    filepath = "/Users/abdullah37/STUDY/IT 315/PracticingForPython/WepAppWithHtml/Jupyter-Prac/data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filepath , skiprows=20 , parse_dates=["    DATE"])
    temp = df.loc[df['    DATE']==date]['   TG'].squeeze() /10
    dictonary = {"station":station, "date":date , "temp":temp}
    return dictonary

if __name__ == "__main__":
    app.run(debug=True , port=8000)

