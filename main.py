import sys
import fcopy as f


def main():
    if len(sys.argv) > 1:
        source_path = sys.argv[0]
        output_path = sys.argv[1]

        with open(source_path), open(output_path):
            f.fcopy(source_path, output_path)

    else:
        raise SystemError("arguments aren't input correctly")


if __name__ == "__main__":
    main()