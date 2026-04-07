#!/usr/bin/env python3
"""Simple static file server with CORS headers for PenguinMod extension development."""

from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class CORSRequestHandler(SimpleHTTPRequestHandler):
    """Serve static files and add CORS headers expected by PenguinMod Studio."""

    # Allow PenguinMod Studio and common local dev origins.
    allowed_origins = {
        "https://studio.penguinmod.com",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174"
    }

    def end_headers(self) -> None:
        origin = self.headers.get("Origin")
        if origin in self.allowed_origins:
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
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
        default="localhost",
        help="Host interface to bind to (default: localhost)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=5173,
        help="Port to listen on (default: 5173; will try 5174 if unavailable)",
    )
    parser.add_argument(
        "--dir",
        default=".",
        help="Directory to serve (default: current directory)",
    )
    parser.add_argument(
        "--origin",
        action="append",
        dest="origins",
        default=None,
        help='Allowed Access-Control-Allow-Origin value. Can be passed multiple times.',
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    serve_dir = Path(args.dir).resolve()

    if not serve_dir.exists() or not serve_dir.is_dir():
        raise SystemExit(f"Not a directory: {serve_dir}")

    if args.origins:
        CORSRequestHandler.allowed_origins = set(args.origins)

    handler = partial(CORSRequestHandler, directory=str(serve_dir))

    ports_to_try = [args.port]
    if args.port == 5173:
        ports_to_try.append(5174)

    server = None
    bound_port = None
    for port in ports_to_try:
        try:
            server = ThreadingHTTPServer((args.host, port), handler)
            bound_port = port
            break
        except OSError:
            continue

    if server is None or bound_port is None:
        raise SystemExit(f"Could not bind to any of these ports: {ports_to_try}")

    print(f"Serving {serve_dir}")
    print(f"URL: http://localhost:{bound_port}/")
    print("Allowed CORS origins:")
    for origin in sorted(CORSRequestHandler.allowed_origins):
        print(f"  - {origin}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
