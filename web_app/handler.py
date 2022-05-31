from flask import Flask, request
from rossmann import Rossmann
import pandas as pd

app = Flask(__name__)
stores = pd.read_csv("store.csv")

@app.route("/", methods=["POST"])
def rossmann_predict():
    store_number = int(request.form["Store"])
    if store_number in stores["Store"]:
        store_data = stores[stores["Store"] == store_number]
        aux = pd.read_csv("test.csv")
        aux = pd.merge(store_data, aux, how="left", on="Store")
    else:
        return "Store not found"

if __name__ == "__main__":
    app.run("0.0.0.0")