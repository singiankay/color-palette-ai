from openai import OpenAI
from dotenv import dotenv_values
from flask import Flask, render_template, request
import json

config = dotenv_values('.env')
client = OpenAI(
    api_key=config["OPENAI_API_KEY"]
)

app = Flask(
    __name__,
    template_folder='templates',
    static_url_path='',
    static_folder='static'
)


def get_colors(msg):
    system_content = (
        "You are a color palette generating assistant that "
        "responds to text prompts for color palettes "
        "You should generate color palettes that fit the theme, "
        "mood, or instructions in the prompt. "
        "The palettes should be between 2 and 8 colors. "
        "Desired Format: a JSON array of hexadecimal color codes"
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_content
             },
            {
                "role": "user",
                "content": (
                    "Convert the following verbal description "
                    "of a color palette into a list of colors: "
                    "The Mediterranean Sea"
                )
            },
            {
                "role": "assistant",
                "content": (
                    '['
                        '"#006699", '
                        '"#66CCCC", '
                        '"#F0E68C", '
                        '"#008000", '
                        '"#F08080"'
                    ']'
                )
            },
            {
                "role": "user",
                "content": (
                    "Convert the following verbal description "
                    "of a color palette into a list of colors: "
                    "sage, nature, earth"
                )
            },
            {
                "role": "assistant",
                "content": (
                    '['
                        '"#EDF1D6", '
                        '"#9DC08B", '
                        '"#609966", '
                        '"#40513B"'
                    ']'
                )
            },
            {
                "role": "user",
                "content": (
                    "Convert the following verbal description "
                    f"of a color palette into a list of colors: {msg}"
                )
            }
        ],
        max_tokens=200
    )
    return json.loads(response.choices[0].message.content)


@app.route("/palette", methods=["POST"])
def get_palette():
    query = request.form.get("query")
    return {"colors": get_colors(query)}


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
