from flask import Flask, render_template, request, jsonify
import yfinance as yf

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ticker = request.form["ticker"].strip()

        # Append .NS if not already present
        if not ticker.endswith(".NS"):
            ticker += ".NS"

        start_date = request.form["start_date"]
        end_date = request.form["end_date"]

        try:
            # Download stock data
            data = yf.download(ticker, start=start_date, end=end_date)
            if data.empty:
                return jsonify({"error": f"No data found for ticker '{ticker}' or the given date range."})

            # Convert data to JSON for frontend
            data.reset_index(inplace=True)
            data_dict = data.to_dict(orient="records")
            return jsonify({"data": data_dict})
        except Exception as e:
            return jsonify({"error": str(e)})

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=False)
