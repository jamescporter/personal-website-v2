"""Capture consistent visual-review screenshots of the published personal website."""

import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path

import fitz
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout

BASE_URL = "https://jamescporter.github.io/personal-website-v2/"
OUT = Path("visual-review")

CAPTURES = [
    ("01_home_desktop_light.png", "", "light", 1440, 900, False, False),
    ("02_home_desktop_dark.png", "", "dark", 1440, 900, False, False),
    ("03_research_desktop_dark.png", "research/", "dark", 1440, 900, False, False),
    ("04_experience_desktop_light.png", "cv/", "light", 1440, 900, False, False),
    ("05_publications_desktop_light.png", "publications/", "light", 1440, 900, False, False),
    ("06_portfolio_desktop_light.png", "portfolio/", "light", 1440, 900, False, False),
    ("07_home_mobile_light.png", "", "light", 390, 844, True, False),
    ("08_research_mobile_light.png", "research/", "light", 390, 844, True, False),
    ("09_home_mobile_menu_open.png", "", "light", 390, 844, True, True),
    ("10_links_desktop_light.png", "links/", "light", 1440, 900, False, False),
]

EXPECTED = {
    "": ".jp-home",
    "research/": ".rs-page",
    "cv/": ".xp-profile",
    "publications/": ".rs-publications",
}

async def load_page(browser, route, theme, width, height, mobile):
    context = await browser.new_context(
        viewport={"width": width, "height": height},
        device_scale_factor=1,
        color_scheme=theme,
        is_mobile=mobile,
        has_touch=mobile,
        locale="en-GB",
        reduced_motion="reduce",
    )
    await context.add_init_script(f"localStorage.setItem('theme', '{theme}');")
    page = await context.new_page()
    url = BASE_URL + route
    response = await page.goto(url, wait_until="domcontentloaded", timeout=45000)
    if not response or response.status != 200:
        raise RuntimeError(f"Page fetch failed: {url} (HTTP {response.status if response else 'none'})")

    try:
        await page.wait_for_load_state("load", timeout=20000)
    except PlaywrightTimeout:
        pass  # Slow optional third-party assets must not block a screenshot.

    await page.evaluate("""theme => {
        localStorage.setItem('theme', theme);
        if (typeof setThemeSetting === 'function') setThemeSetting(theme);
        else document.documentElement.setAttribute('data-theme', theme);
    }""", theme)
    await page.wait_for_function("expected => document.documentElement.dataset.theme === expected", arg=theme, timeout=10000)
    try:
        await asyncio.wait_for(page.evaluate("document.fonts.ready"), timeout=12000)
    except (asyncio.TimeoutError, PlaywrightTimeout):
        pass
    await page.wait_for_timeout(450)
    selector = EXPECTED.get(route)
    if selector and await page.locator(selector).count() == 0:
        raise RuntimeError(f"Expected updated site content '{selector}' missing at {url}")
    return context, page


async def capture(browser, entry):
    filename, route, theme, width, height, mobile, menu = entry
    context, page = await load_page(browser, route, theme, width, height, mobile)
    try:
        if menu:
            toggle = page.locator("button.navbar-toggler-main")
            await toggle.wait_for(state="visible", timeout=10000)
            await toggle.click()
            await page.wait_for_function(
                "() => document.querySelector('button.navbar-toggler-main')?.getAttribute('aria-expanded') === 'true'",
                timeout=10000,
            )
            await page.wait_for_timeout(350)
        await page.screenshot(path=str(OUT / filename), full_page=not menu, animations="disabled")
        record = {
            "file": filename,
            "url": page.url,
            "title": await page.title(),
            "theme_requested": theme,
            "theme_rendered": await page.locator("html").get_attribute("data-theme"),
            "viewport": f"{width}x{height}",
            "mobile": mobile,
            "menu_open": menu,
            "document_height": await page.evaluate("document.documentElement.scrollHeight"),
        }
        print(f"CAPTURED {filename}: {record['document_height']}px, theme={record['theme_rendered']}", flush=True)
        return record
    finally:
        await context.close()


async def capture_print(browser):
    context, page = await load_page(browser, "research/", "light", 1440, 900, False)
    try:
        await page.emulate_media(media="print")
        pdf_path = OUT / "11_research_print_a4.pdf"
        await page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            display_header_footer=False,
            prefer_css_page_size=False,
        )
        document = fitz.open(pdf_path)
        number = len(document)
        for index in range(number):
            pixmap = document[index].get_pixmap(matrix=fitz.Matrix(1.4, 1.4), alpha=False)
            pixmap.save(str(OUT / f"11_research_print_page_{index + 1:02d}.png"))
        document.close()
        print(f"PRINTED {pdf_path.name}: {number} pages", flush=True)
        return number
    finally:
        await context.close()


async def main():
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {"captured_utc": datetime.now(timezone.utc).isoformat(), "base_url": BASE_URL, "captures": []}
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        try:
            manifest["browser_version"] = browser.version
            for entry in CAPTURES:
                manifest["captures"].append(await capture(browser, entry))
            manifest["print_page_count"] = await capture_print(browser)
        finally:
            await browser.close()

    (OUT / "capture_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (OUT / "README.txt").write_text(
        "Website visual-review captures\n"
        f"Source: {BASE_URL}\n"
        f"Captured (UTC): {manifest['captured_utc']}\n"
        f"Browser: Chromium {manifest['browser_version']}\n\n"
        "All numbered PNGs except the expanded mobile menu are full-page screenshots.\n"
        "Mobile menu is a viewport screenshot with the navigation expanded.\n"
        "11_research_print_a4.pdf is the Chromium print-media rendering on A4.\n"
        "11_research_print_page_XX.png show its individual pages for visual review.\n"
        "No website files are modified by the capture script.\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    asyncio.run(main())
