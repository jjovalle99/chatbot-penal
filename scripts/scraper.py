import argparse
import asyncio
import os
from typing import List

from dotenv import load_dotenv
from playwright.async_api import Browser, async_playwright

load_dotenv()


async def fetch_page_content(browser: Browser, url: str) -> str:
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto(url, wait_until="domcontentloaded")

    links = await page.query_selector_all(".caja_vja_encabezado")
    print(f"Se encontraron {len(links)} links en {url}")

    for link in links:
        await link.click(timeout=int(6e4))

    content = await page.content()
    await context.close()
    return content


async def write_content_to_file(file_name: str, content: str) -> None:
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(content)


async def process_url(browser: Browser, url: str, idx: int, output_path: str) -> None:
    print(f"Processing URL {idx}: {url}")
    content = await fetch_page_content(browser, url)
    await write_content_to_file(os.path.join(output_path, f"output_{idx}.html"), content)


async def main(urls: List[str], output_path: str) -> None:
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(
            f"wss://chrome.browserless.io?token={os.getenv('BROWSERLESS_API_KEY')}"
        )
        tasks = [process_url(browser, url, idx, output_path) for idx, url in enumerate(urls, start=1)]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output_path",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--webpage",
        action="append",
        required=True,
    )

    args = parser.parse_args()
    asyncio.run(main(args.webpage, args.output_path))
