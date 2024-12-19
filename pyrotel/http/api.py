from typing import Optional

import aiohttp
from aiohttp_socks import ProxyConnector

from pyrotel.types import Results
from pyrotel.errors import APIError


class API:

    BASE_URL = "https://api.telegram.org"

    def __init__(self, client=None):
        self.client = client

    async def execute(self, name: str, method: Optional[str] = "GET", data: Optional[dict] = None):
        """
        Execute asynchronous request to BaleAPI
        """
        base_url = self.client.base_url or self.BASE_URL
        path = f"/bot{self.client.bot_token}/" + name
        connector = ProxyConnector.from_url(self.client.proxies)
        timeout = aiohttp.ClientTimeout(total=self.client.timeout)
        for _ in range(self.client.max_retry):
            async with aiohttp.ClientSession(base_url=base_url, timeout=timeout, connector=connector) as self.session:
                async with self.session.request(method=method, url=path, json=data) as response:
                    response_data = await response.json()
                    if response_data.get("ok"):
                        response_data.pop("ok")
                        return Results(response_data)
                    error_code = response_data.get("error_code")
                    description = response_data.get("description")
                    raise APIError(description, error_code)
