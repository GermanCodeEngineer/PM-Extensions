#!/usr/bin/env python3
"""Simple static file server with CORS headers for PenguinMod extension development."""

from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class CORSRequestHandler(SimpleHTTPRequestHandler):
    """Serve static files and add CORS headers expected by PenguinMod Studio."""

    # Restrict this to PenguinMod Studio. Change to "*" if needed for other tools.
    allowed_origin = "https://studio.penguinmod.com"

    def end_headers(self) -> None:
        self.send_header("Access-Control-Allow-Origin", self.allowed_origin)
        self.send_header("Access-Control-Allow-Methods", "GET, HEAD, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Max-Age", "86400")
        super().end_headers()

    def do_OPTIONS(self) -> None:
        self.send_response(204)
        self.end_headers()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run a local static file server with CORS headers for PenguinMod."
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host interface to bind to (default: 127.0.0.1)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=5500,
        help="Port to listen on (default: 5500)",
    )
    parser.add_argument(
        "--dir",
        default=".",
        help="Directory to serve (default: current directory)",
    )
    parser.add_argument(
        "--origin",
        default="https://studio.penguinmod.com",
        help='Allowed Access-Control-Allow-Origin value (default: "https://studio.penguinmod.com")',
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    serve_dir = Path(args.dir).resolve()

    if not serve_dir.exists() or not serve_dir.is_dir():
        raise SystemExit(f"Not a directory: {serve_dir}")

    CORSRequestHandler.allowed_origin = args.origin
    handler = partial(CORSRequestHandler, directory=str(serve_dir))

    server = ThreadingHTTPServer((args.host, args.port), handler)
    print(f"Serving {serve_dir}")
    print(f"URL: http://{args.host}:{args.port}/")
    print(f"CORS Access-Control-Allow-Origin: {CORSRequestHandler.allowed_origin}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
