import subprocess

cmd = f"bash uwsgi/bootuwsgi.sh"
try:
	result = subprocess.check_output(cmd, shell=True, text=True)
	print(result)
except subprocess.CalledProcessError as e:
    print(f"Error executing command: {e}")