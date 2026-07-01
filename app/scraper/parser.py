from bs4 import BeautifulSoup


def extract_assessment(html: str, url: str):
    soup = BeautifulSoup(html, "html.parser")

    title = ""

    if soup.find("h1"):
        title = soup.find("h1").get_text(strip=True)

    description = ""

    p = soup.find("p")

    if p:
        description = p.get_text(" ", strip=True)

    text = soup.get_text(" ", strip=True)

    return {
        "name": title,
        "url": url,
        "description": description,
        "content": text
    }