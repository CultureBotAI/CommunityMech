"""python -m communitymech.export entry point."""
import sys

from communitymech.export.kgx_export import main

if __name__ == "__main__":
    sys.exit(main())
