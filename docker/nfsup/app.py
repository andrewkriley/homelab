from flask import Flask, jsonify
import subprocess
import os

app = Flask(__name__)

NFS_SERVER = (os.environ.get('NFS_SERVER'))  # Replace with your NFS server address
NFS_PORT = (os.environ.get('NFS_PORT'))              # NFS typically uses port 2049

print(NFS_SERVER)
print(NFS_PORT)

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