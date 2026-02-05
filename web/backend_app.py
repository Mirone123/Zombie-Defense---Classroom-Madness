"""Simple Flask bridge: login/registration + leaderboard from SQLite."""

from __future__ import annotations

from flask import Flask, redirect, render_template_string, request, url_for

from game import database

app = Flask(__name__)

database.init_db()

PAGE = """
<!doctype html>
<html lang="cs">
<head><meta charset="utf-8"><title>Zombie Defense Web</title></head>
<body style="font-family: Arial; max-width: 760px; margin: 2rem auto;">
  <h1>Zombie Defense – Web rozhraní</h1>
  <h2>Registrace / login hráče</h2>
  <form method="post" action="{{ url_for('register') }}">
    <input name="name" placeholder="Jméno" required>
    <input name="email" type="email" placeholder="Email">
    <button type="submit">Uložit hráče</button>
  </form>
  {% if message %}<p><strong>{{ message }}</strong></p>{% endif %}

  <h2>Top výsledky</h2>
  <ol>
    {% for row in leaderboard %}
      <li>{{ row['jmeno'] }} | {{ row['skore'] }} | {{ row['datum'] }}</li>
    {% else %}
      <li>Zatím žádné výsledky</li>
    {% endfor %}
  </ol>
</body>
</html>
"""


@app.get("/")
def index():
    """Render registration form and live leaderboard."""
    return render_template_string(PAGE, leaderboard=database.get_leaderboard(10), message=request.args.get("msg"))


@app.post("/register")
def register():
    """Handle player registration/update."""
    name = request.form.get("name", "")
    email = request.form.get("email", "")
    try:
        database.register_player(name, email)
        return redirect(url_for("index", msg=f"Hráč '{name}' byl uložen."))
    except ValueError as exc:
        return redirect(url_for("index", msg=str(exc)))


if __name__ == "__main__":
    app.run(debug=True)
