import subprocess
import sys

port_index = sys.argv.index('--port') if '--port' in sys.argv else -1

# Get the port number from the command line arguments or use a default (e.g., 8001)
port = int(sys.argv[port_index + 1]) if port_index != -1 and port_index + 1 < len(sys.argv) else 8001


subprocess.run(['chalice', 'local', '--port', str(port), '--stage', 'dev'], check=True)