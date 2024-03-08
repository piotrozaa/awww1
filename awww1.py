import requests
from bs4 import BeautifulSoup

# Pobieranie danych ze strony
def scrape_chess_openings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = []

    for h5 in soup.find_all('h5'):
        # Szukanie znacznika <img> przed znacznikiem <h5>
        img = h5.find_previous('img')
        if img:
            img_src = img['src']
        else:
            img_src = 'No image found'

        opening_name = h5.text.strip()
        data.append((opening_name, img_src))

    return data

# Generowanie pliku Markdown z HTML
def generate_markdown(data, base_url):
    markdown_content = "<h1>List of Chess Openings</h1>\n\n"
    for name, img in data:
        markdown_content += f"<h2>{name}</h2>\n"
        markdown_content += f"<p><img src=\"{img}\" alt=\"{name}\" /></p>\n"
        markdown_content += f"<p><a href=\"{base_url}\">More details</a></p>\n\n"
    return markdown_content

# Główna funkcja
def main():
    url = 'https://www.thechesswebsite.com/chess-openings/'
    openings_data = scrape_chess_openings(url)
    markdown_content = generate_markdown(openings_data, url)

    # Zapisanie do pliku Markdown
    with open("chess_openings.md", "w", encoding="utf-8") as file:
        file.write(markdown_content)

if __name__ == "__main__":
    main()
