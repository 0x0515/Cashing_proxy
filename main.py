import argparse
from server import run_server

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple Caching Proxy Server')
    parser.add_argument('--origin', type=str, required=True, help='Original server host')
    parser.add_argument('--port', type=int, default=8080, help='Port to run the proxy server on')
    args = parser.parse_args()
    
    run_server(args.origin, args.port)