"""Verify that the generated public site has genuine content and no starter CV artifacts."""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path


class MetaParser(HTMLParser):
    """Collect metadata without assumptions about HTML tag/attribute order."""

    def __init__(self) -> None:
        super().__init__()
        self.properties: dict[str, str] = {}
        self.canonicals: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "meta" and values.get("property", "").startswith("og:"):
            self.properties[values["property"]] = values.get("content", "") or ""
        elif tag == "link" and values.get("rel") == "canonical":
            self.canonicals.append(values.get("href", "") or "")


def check(root: Path) -> None:
    origin = "https://jamescporter.github.io/personal-website-v2"
    required = ("", "about", "cv", "research", "publications", "portfolio", "links")
    for page in required:
        output = root / page / "index.html" if page else root / "index.html"
        assert output.is_file(), f"Missing required public page: {output}"

    home = (root / "index.html").read_text(encoding="utf-8")
    parsed = MetaParser()
    parsed.feed(home)
    assert parsed.properties.get("og:title"), "Missing Open Graph title"
    assert parsed.properties.get("og:description"), "Missing Open Graph description"
    assert f"{origin}/" in parsed.canonicals, "Incorrect homepage canonical URL"

    sitemap = root / "sitemap.xml"
    assert sitemap.is_file(), "Missing sitemap.xml"
    xml = ET.parse(sitemap)
    urls = {element.text for element in xml.iter() if element.tag.endswith("loc")}
    for page in required:
        url = f"{origin}/{page}/" if page else f"{origin}/"
        assert url in urls, f"Missing canonical page from sitemap: {url}"
    for page in ("_pages/dropdown", "writing", "personal", "people", "teaching", "books"):
        url = f"{origin}/{page}/"
        assert url not in urls, f"Non-public/demo URL remains in sitemap: {url}"

    for removed in (
        "assets/json/resume.json",
        "assets/pdf/example_pdf.pdf",
        "assets/rendercv/rendercv_output/Albert_Einstein_CV.pdf",
        "assets/video/pexels-engin-akyurt-6069112-960x540-30fps.mp4",
    ):
        assert not (root / removed).exists(), f"Demo file still published: {removed}"

    writing = root / "writing" / "index.html"
    personal = root / "personal" / "index.html"
    assert writing.is_file() and personal.is_file(), "Deferred routes should remain usable"
    assert "No public articles are currently listed here" in writing.read_text(encoding="utf-8")
    assert "No projects are currently listed here" in personal.read_text(encoding="utf-8")
    print(f"Public site audit passed: {len(required)} canonical routes, OG metadata, clean sitemap and no starter CV data.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python scripts/audit_public_site.py PATH_TO_BUILT_SITE")
    check(Path(sys.argv[1]))
