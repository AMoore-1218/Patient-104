
from fasthtml.common import *

app = FastHTML()

@app.route('/')
def home():
    return Html(
        Head(Title("My FastHTML App")),
        Body(
            H1("Welcome to FastHTML!"),
            P("This is a simple FastHTML application."),
            A("Learn more about FastHTML", href="https://fastht.ml/")
        )
    )

if __name__ == "__main__":
    serve(host="0.0.0.0", port=5000)
