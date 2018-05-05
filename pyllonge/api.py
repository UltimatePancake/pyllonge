import aiohttp


class UnauthorizedException(Exception):
    pass


class ScopeException(Exception):
    pass


class FormatException(Exception):
    pass


class ValidationException(Exception):
    pass


class ServerException(Exception):
    pass


api_key = None
response_format = 'json'
base_url = 'https://api.challonge.com/v1/'

def set_key(api_key):
    api_key = api_key

def get_key():
    return api_key

async def fetch(path, **payload):
    url = '{}{}.{}'.format(base_url, path, response_format)
    payload['api_key'] = api_key

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=payload) as resp:
            return await resp.json()

async def post(path, payload):
    url = '{}{}.{}'.format(base_url, path, response_format)
    payload['api_key'] = api_key

    print(payload)

    async with aiohttp.ClientSession() as session:
        async with session.post(url, params=payload) as resp:
            return await resp.json()