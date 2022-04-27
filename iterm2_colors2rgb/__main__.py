import json
import sys

from iterm2_colors2rgb import iterm2_colors2rgb


def toHex(c):
    r, g, b = c
    return hex((r << 16) | (g << 8) | b)[2:].zfill(6)


if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else None

    try:
        bg, fg, ansi, bold = iterm2_colors2rgb(filepath)
        print((toHex(bg), toHex(fg), [toHex(c)
              for c in ansi], [toHex(c) for c in bold]))

    except Exception as exc:
        sys.exit(str(exc))
