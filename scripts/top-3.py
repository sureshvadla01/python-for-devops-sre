import subprocess

def get_df_output():
    # Run `df -kh` and capture the output
    result = subprocess.run(["df", "-kh"], capture_output=True, text=True)
    return result.stdout.strip().splitlines()

def parse_df(lines):
    parsed = []
    for line in lines[1:]:  # skip header
        parts = line.split()
        if len(parts) < 5:
            continue

        filesystem = parts[0]
        usage_percent = parts[4].replace("%", "")

        try:
            usage_int = int(usage_percent)
        except ValueError:
            continue

        parsed.append((usage_int, filesystem, line))

    return parsed

def main():
    lines = get_df_output()
    parsed = parse_df(lines)

    # Sort descending by usage percent
    top = sorted(parsed, reverse=True)[:3]

    print("Top 3 filesystems by usage:")
    for usage, fs, full in top:
        print(f"{usage}%  {fs}")

if __name__ == "__main__":
    main()
