from flask import Flask, render_template_string
import subprocess
import os

app = Flask(__name__)

# Retrieve NFS server address and port from environment variables, with defaults
NFS_SERVER = os.environ.get('NFS_SERVER', 'default_nfs_server')  # Replace with a default or handle appropriately
NFS_PORT = os.environ.get('NFS_PORT', '2049')  # Default NFS port is 2049

def check_nfs():
    try:
        # Use nc (netcat) to check if the NFS port is open
        subprocess.check_output(['nc', '-z', '-w1', NFS_SERVER, str(NFS_PORT)])
        return True
    except subprocess.CalledProcessError:
        return False
    except Exception as e:
        print(f"An error occurred while checking NFS status: {e}")
        return False

@app.route('/')
def status():
    if check_nfs():
        status = 'NFS is available'
        color = 'green'
    else:
        status = 'NFS is unavailable'
        color = 'red'
    
    # HTML template with formatting and variables
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="20">
        <title>NFS Status</title>
        <style>
            .status {
                font-size: 24px;
                color: {{ color }};
            }
            .details {
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <h1 class="status">{{ status }}</h1>
        <p class="details">NFS Server: {{ nfs_server }}</p>
        <p class="details">NFS Port: {{ nfs_port }}</p>
    </body>
    </html>
    """
    return render_template_string(html_template, status=status, color=color, nfs_server=NFS_SERVER, nfs_port=NFS_PORT)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)