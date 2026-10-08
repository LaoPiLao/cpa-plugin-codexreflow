"""Validate and package a locally built release. Does not publish anything."""

import argparse
import hashlib
from pathlib import Path
import re
import struct
import zipfile

from native_smoke import OfflineHost

ROOT = Path(__file__).resolve().parents[1]
VERSION_PATTERN = r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)"
REPOSITORY_PATTERN = r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+"


def validate_windows_amd64_dll(raw):
    if len(raw) < 64 or raw[:2] != b"MZ":
        raise ValueError("release asset must be a Windows PE DLL")
    offset = struct.unpack_from("<I", raw, 60)[0]
    if offset + 24 > len(raw) or raw[offset:offset + 4] != b"PE\0\0":
        raise ValueError("invalid PE header")
    machine = struct.unpack_from("<H", raw, offset + 4)[0]
    characteristics = struct.unpack_from("<H", raw, offset + 22)[0]
    if machine != 0x8664 or not characteristics & 0x2000:
        raise ValueError("only Windows amd64 DLLs may use this release asset name")


def validate_metadata(metadata, version, repository):
    if not re.fullmatch(VERSION_PATTERN, version):
        raise ValueError("formal releases require a numeric MAJOR.MINOR.PATCH version")
    if not re.fullmatch(REPOSITORY_PATTERN, repository) or "REPLACE_WITH" in repository or "/OWNER/" in repository:
        raise ValueError("confirm the actual GitHub repository before packaging")
    if metadata.get("Name") != "codexreflow":
        raise ValueError("DLL plugin ID is not codexreflow")
    if metadata.get("Version") != version:
        raise ValueError("DLL version does not match the release version (development builds are rejected)")
    if metadata.get("GitHubRepository") != repository:
        raise ValueError("DLL source repository does not match the release repository")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--library", type=Path, default=ROOT / "build/codexreflow.dll")
    args = parser.parse_args()
    validate_windows_amd64_dll(args.library.read_bytes())
    host = OfflineHost(args.library)
    registration = host.call("plugin.register", {})
    host.plugin.shutdown()
    validate_metadata(registration["metadata"], args.version, args.repository)
    if args.version != (ROOT / "VERSION").read_text(encoding="utf-8").strip():
        raise ValueError("update VERSION deliberately before packaging a different release")
    dist = ROOT / "dist" / args.version
    name = f"codexreflow_{args.version}_windows_amd64.zip"
    archive = dist / name
    dist.mkdir(parents=True, exist_ok=True)
    if archive.exists() or (dist / "checksums.txt").exists():
        raise FileExistsError("release output already exists; do not silently replace a version")
    with zipfile.ZipFile(archive, "x", compression=zipfile.ZIP_DEFLATED) as out:
        out.write(args.library, "codexreflow.dll")
        for filename in ("LICENSE", "THIRD_PARTY_NOTICES.md", "THIRD_PARTY_LICENSES.txt"):
            out.write(ROOT / filename, filename)
    with archive.open("rb") as source:
        digest = hashlib.file_digest(source, "sha256").hexdigest()
    (dist / "checksums.txt").write_text(f"{digest}  {name}\n", encoding="utf-8", newline="\n")
    print(f"Packaged {archive}; no upload, Release, or store submission performed.")


if __name__ == "__main__":
    main()
