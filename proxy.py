import http.client

class CachingProxy:
    def __init__(self, original, port):
        self.host = original
        self.port = port
        self.hash = {}

    def handel_request(self, request_path):
        if request_path in self.hash:
            print(f"[CACHE HIT] Found in cache for path: {request_path}")
            return self.hash[request_path]
        else:
            print(f"[CACHE MISS] Fetching from original server for path: {request_path}")
            response = self.get_from_original_server(request_path)
            self.hash[request_path] = response
            return response

    def get_from_original_server(self, request_path):
        conn = http.client.HTTPConnection(self.host)
        conn.request("GET", request_path)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data

    def clear_cache(self):
        self.hash.clear()
        print("Cache cleared.")