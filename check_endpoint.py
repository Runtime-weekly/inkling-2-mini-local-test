"""Small loopback-only runtime check; standard library, no model downloads."""
import json
import urllib.request

BASE = 'http://127.0.0.1:8112/v1'
MODEL = 'inkling-2-mini-26.4b-a3.4b-nvfp4-mxfp8'

def main():
    with urllib.request.urlopen(BASE + '/models', timeout=15) as response:
        models = json.load(response)
    assert MODEL in [m['id'] for m in models['data']], 'Expected model is not served'
    body = {'model': MODEL, 'messages': [{'role': 'user', 'content': 'Reply with a short greeting.'}],
            'max_tokens': 256, 'temperature': 1.0, 'reasoning_effort': 'minimal'}
    request = urllib.request.Request(BASE + '/chat/completions',
        data=json.dumps(body).encode(), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(request, timeout=180) as response:
        result = json.load(response)
    print(json.dumps({'message': result['choices'][0]['message'], 'usage': result.get('usage')}, indent=2))

if __name__ == '__main__':
    main()
