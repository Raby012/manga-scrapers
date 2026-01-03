# Manga Scraper API

[![Under Development](https://img.shields.io/badge/status-under%20development-orange)](https://github.com/real-zephex/manga-scrapers)

A FastAPI-based web application for scraping manga information from various online sources. This project aggregates data from popular manga websites, providing a unified API for searching, retrieving manga details, and accessing chapter pages.

## Features

- **Multi-Source Support**: Scrapes data from Manganato, Mangareader, Mangapill, Asurascans, and Flamecomics.
- **Comprehensive Endpoints**: Includes search, info retrieval, chapter pages, and categorized listings (e.g., latest, popular, by genre).
- **Image Handling**: Proper headers for image retrieval to avoid access issues.
- **FastAPI Framework**: Built with FastAPI for high performance and automatic API documentation.

## Supported Sources

1. [Manganato](https://manganato.com/)
2. [Mangareader](https://mangareader.tv/)
3. [Mangapill](https://mangapill.com/)
4. [Asurascans](https://asurascans.io/) *(Note: May not work on demo sites; functions locally)*
5. [Flamecomics](https://flamecomics.me/)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/real-zephex/manga-scrapers.git
   cd manga-scrapers
   ```

2. **Create and Activate a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   - API Documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc Documentation: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

### General
- **GET /**: Returns a welcome message.
  ```json
  {
    "message": "Welcome to the Manga Scraper API"
  }
  ```

### Manganato
- **GET /manganato/search/{query}**: Search manga by query.
- **GET /manganato/info/{id}**: Get manga info by ID.
- **GET /manganato/pages/{id}**: Get manga pages by ID.
- **GET /manganato/latest/{page}**: Get latest manga (optional page number).
- **GET /manganato/newest/{page}**: Get newest manga (optional page number).
- **GET /manganato/hotest/{page}**: Get hottest manga (optional page number).
- **GET /manganato/image/{url}**: Get manga image by URL.

### Mangareader
- **GET /mangareader/search/{query}**: Search manga by query.
- **GET /mangareader/info/{id}**: Get manga info by ID.
- **GET /mangareader/pages/{id}**: Get manga pages by ID.
- **GET /mangareader/genre-list**: Get list of genres.
- **GET /mangareader/latest/{genre}**: Get latest manga by genre.

### Mangapill
- **GET /mangapill/search/{query}**: Search manga by query.
- **GET /mangapill/info/{id}**: Get manga info by ID.
- **GET /mangapill/pages/{id}**: Get manga pages by ID.
- **GET /mangapill/newest**: Get newest manga.
- **GET /mangapill/images/{url}**: Get manga image by URL.

### Asurascans
- **GET /asurascans/search/{query}**: Search manga by query.
- **GET /asurascans/info/{id}**: Get manga info by ID.
- **GET /asurascans/pages/{id}**: Get manga pages by ID.
- **GET /asurascans/popular**: Get popular manga.
- **GET /asurascans/latest/{page}**: Get latest manga (optional page number).
- **GET /asurascans/genres/{genre}**: Get manga by genre.
- **GET /asurascans/genre-list**: Get list of genres.

### Flamecomics
- **GET /flamescans/search/{query}**: Search manga by title.
- **GET /flamescans/info/{id}**: Get manga info by ID.
- **GET /flamescans/pages/{id}**: Get manga pages by ID.
- **GET /flamescans/sort/{sort_type}**: Get sorted manga. Accepts: `title`, `titlereverse`, `update`, `popular`, `added`.

## Example Queries

- **Manganato Search**: `GET /manganato/search/one_piece`
- **Mangareader Latest by Genre**: `GET /mangareader/latest/Action`
- **Mangapill Newest**: `GET /mangapill/newest`
- **Asurascans Popular**: `GET /asurascans/popular`

## Notes

- Image retrieval endpoints include appropriate headers to set the correct referer and avoid access restrictions.
- Asurascans endpoints may not function on demo deployments but work when hosted locally. Contributions to fix this are welcome.

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is for educational purposes only. Ensure compliance with the terms of service of the scraped websites and respect copyright laws. The maintainers are not responsible for any misuse of this tool.