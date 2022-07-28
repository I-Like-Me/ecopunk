from flask import Flask, render_template
from helper import people, char_type, job, faction, inventory

app = Flask(__name__)

@app.route('/')
def directory():
    return render_template("directory.html", template_people=people)

@app.route('/listing/<string:code>')
def listing(code):
    return render_template("listing.html", template_people=people[code], template_char_type=char_type[code], template_job=job[code], template_faction=faction[code], template_inventory=inventory[code])

if __name__ == '__main__':
    app.run(debug=True)