__CycleTLS Wrapper - convenient, fast, no bans__

## Minimal information  before start using
```shell
pip3 install aiocycletls
```
__After install you must get build from my repository  or create own for your system. (repository CycleTLS)__

__This project working with proxy on low-level of Go network__

__Some example__
```python
import aiocycletls

async def main() -> None:
    proxy = aiocycletls.WSProxyClient()
    response = await proxy.request(
        url="https://tools.scrapfly.io/api/fp/ja3?extended=1",
        method="GET",
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        ja3=aiocycletls.JA3.CHROME_107
    )
    print(response.jsonable_body()) # You see your JA3 <3
```
