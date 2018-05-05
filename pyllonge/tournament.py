from pyllonge import api


async def index(**params):
    return await api.fetch('tournaments', **params)

async def create(**params):
    data = { "tournament" : params }
    return await api.post('tournaments', data)

async def show(tournament, **params):
    return await api.fetch('tournaments/{}'.format(tournament), **params)
