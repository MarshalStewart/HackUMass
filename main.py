from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def display_maze():
    return render_template('maze_template/main.html')


if __name__ == '__main__':
    app.run()

