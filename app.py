from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Bavikati Vennela"  
    username = os.getenv("USER") or os.getenv("USERNAME")
    server_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # Get the top command output
    top_output = subprocess.getoutput("top -b -n 1")  # Adjust command if on Mac or Windows

    # HTML to display the information
    return f"""
    <html>
        <body>
            <h1>System Information</h1>
            <p><b>Name:</b> {name}</p>
            <p><b>Username:</b> {username}</p>
            <p><b>Server Time (IST):</b> {server_time}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
