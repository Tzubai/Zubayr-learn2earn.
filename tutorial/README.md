# Ascii-art-web

## Description

A small Go HTTP server that converts plain text into ASCII art using three available banners: `shadow`, `standard` and `thinkertoy`. The web UI allows entering text, selecting a banner, and viewing the generated ASCII art.

## Authors

- Original author (project workspace)

## Usage

Build and run the server from the project root:

```bash
go build -o ascii-art .
./ascii-art
# then open http://localhost:8080 in your browser
```

Alternatively run directly with `go run`:

```bash
go run Main.go
```

## Implementation details: algorithm

The server loads the banner font files (`shadow.txt`, `standard.txt`, `thinkertoy.txt`) from the project root. When a POST request is made to `/ascii-art`, the server:

- Reads the requested banner file.
- Splits the banner file into lines and computes the offset for each printable ASCII character.
- For each line of the input text, it composes 8 rows (font height) by mapping each character to the corresponding lines in the banner file and concatenating them.
- The result is rendered into the HTML template and returned to the client.

HTTP status codes used:

- `200 OK` for successful requests.
- `400 Bad Request` for invalid inputs (empty text).
- `404 Not Found` when templates or banner files are missing.
- `500 Internal Server Error` for unexpected template execution or server failures.
