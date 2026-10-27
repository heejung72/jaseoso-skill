#!/usr/bin/env python3
"""자소서 글자수 측정 스크립트.

Usage:
    python3 count_korean_length.py <file> [--json]
    echo "텍스트" | python3 count_korean_length.py --stdin [--json]
"""

import argparse
import json
import sys


def count(text: str) -> dict:
    """다양한 기준으로 글자수를 측정한다."""
    # 앞뒤 공백 제거
    text = text.strip()

    chars_with_spaces = len(text)
    chars_without_spaces = len(text.replace(" ", "").replace("\t", ""))
    # 줄바꿈도 제외한 순수 글자수
    chars_pure = len(text.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", ""))

    utf8_bytes = len(text.encode("utf-8"))

    try:
        euckr_bytes = len(text.encode("euc-kr", errors="replace"))
    except Exception:
        euckr_bytes = None

    words = len(text.split())

    return {
        "chars_with_spaces": chars_with_spaces,
        "chars_without_spaces": chars_without_spaces,
        "chars_pure": chars_pure,
        "utf8_bytes": utf8_bytes,
        "euckr_bytes": euckr_bytes,
        "words": words,
    }


def main():
    parser = argparse.ArgumentParser(description="한국어 글자수 측정")
    parser.add_argument("file", nargs="?", help="측정할 파일 경로")
    parser.add_argument("--stdin", action="store_true", help="표준 입력에서 읽기")
    parser.add_argument("--json", action="store_true", help="JSON 형식 출력")
    args = parser.parse_args()

    if args.stdin or (args.file is None and not sys.stdin.isatty()):
        text = sys.stdin.read()
    elif args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        parser.print_help()
        sys.exit(1)

    result = count(text)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"공백 포함: {result['chars_with_spaces']}자")
        print(f"공백 제외: {result['chars_without_spaces']}자")
        print(f"순수 글자: {result['chars_pure']}자")
        print(f"UTF-8:     {result['utf8_bytes']} bytes")
        if result["euckr_bytes"]:
            print(f"EUC-KR:    {result['euckr_bytes']} bytes")
        print(f"어절 수:   {result['words']}개")


if __name__ == "__main__":
    main()
