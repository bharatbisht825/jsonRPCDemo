import subprocess
import json

# JSON-RPC request
request = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "add",
    "params": {
        "a": 10,
        "b": 32
    }
}

# Start JS process
proc = subprocess.Popen(
    ["node", "/home/bharat-nobel/Documents/jsonRPCDemo/rpc.js"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Send request
stdout, stderr = proc.communicate(json.dumps(request))

# Parse response
response = json.loads(stdout)

print("Result from JS:", response)
