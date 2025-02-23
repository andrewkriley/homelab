from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

NFS_SERVER = '192.168.1.1'   # Replace with your NFS server address
NFS_PORT = 2049               # NFS typically uses port 2049

def check_nfs():
    try:
        # Use nc to check if the NFS port is open
        subprocess.check_output(['nc', '-z', '-w1', NFS_SERVER, str(NFS_PORT)])
        return True
    except subprocess.CalledProcessError:
        return False

@app.route('/')
def status():
    if check_nfs():
        status = 'NFS is available'
    else:
        status = 'NFS is unavailable'
    return jsonify({'status': status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)