import json
import urllib3

def lambda_handler(event, context):
    http = urllib3.PoolManager()
    url = 'YOUR_API_ENDPOINT'
    
    try:
        response = http.request('GET', url)
        data = json.loads(response.data.decode('utf-8'))
        
        return {
            'statusCode': 200,
            'body': json.dumps(data)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }