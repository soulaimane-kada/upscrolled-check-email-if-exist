from playwright.async_api import async_playwright
from apify import Actor
from curl_cffi import requests
import json, secrets, asyncio


async def check_email(email):
    api_url = 'https://api.upscrolled.com/account/check/email'
    headers = {
        "accept-encoding": "gzip",
        "content-length": "55",
        "content-type": "application/json",
        "host": "api.upscrolled.com",
        "sentry-trace": "f429d81e34ab49a5b3e2947975f74279-46545a98cdd7410f-0",
        "user-agent": "Dart/3.10 (dart:io)",
        "x-api-key": "Wsjxb3BqTL72pfvB4ikO3aKR1fBsCFz63Jb1RuJ7"
    }

    data = {
        "email": email,
        "getStreamToken": ""
    }

    headers['content-length'] = str(len(json.dumps(data, separators=(',', ':')).encode('utf-8')))
    headers["sentry-trace"] = f"f429d81e34ab49a5b3e2947975f74279-{secrets.token_hex(8)}-0"

    try:
        proxy = await Actor.create_proxy_configuration(groups=['RESIDENTIAL'])
        proxy_url = await proxy.new_url()
        
        response = requests.post(
            api_url, json=data, headers=headers,
            proxies={
                "http": proxy_url,
                "https": proxy_url,
            },
            timeout=10)
        
        return {'success': True, 'results': response.json()}
    except:
        return {'success': False, 'message': 'error'}


async def main():
    async with Actor:
        input_data = await Actor.get_input()
        email = input_data.get('email')
        result = await check_email(email)
        await Actor.push_data(result)

if __name__ == "__main__":
    asyncio.run(main())
