import asyncio
import os
import unittest
import pyllonge
from pyllonge import api, tournament


api_key = None


class CredentialsTestCase(unittest.TestCase):
    def test_set_key(self):
        api.set_key(api_key)
        self.assertEqual(api.api_key, api_key)

    def test_get_key(self):
        api.api_key = api_key
        self.assertEqual(api.get_key(), api_key)


class TournamentsTestCase(unittest.TestCase):
    def setUp(self):
        api.set_key(api_key)

    def async_test(f):
        def wrapper(*args, **kwargs):
            coro = asyncio.coroutine(f)
            future = coro(*args, **kwargs)
            loop = asyncio.get_event_loop()
            loop.run_until_complete(future)

        return wrapper

    @async_test
    def test_index_tournaments(self):
        results = yield from tournament.index()
        self.assertEqual(1, 1)

    @async_test
    def test_create_tournament(self):
        params = {
            "name" : "TEST TOURNAMENT",
            "url" : "ultimatepancake",
            "tournament_type" : "single elimination"
        }
        results = yield from tournament.create(**params)
        print(results)
        self.assertEqual(1, 1)


if __name__ == '__main__':
    api_key = os.environ.get('CHALLONGE_KEY')

    if not api_key:
        raise RuntimeError('You *must* add the CHALLONGE_KEY env var to run the tests.')

    unittest.main()