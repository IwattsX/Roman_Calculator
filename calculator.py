import argparse

def main():
    parser = argparse.ArgumentParser(description="Process some arguments.")
    
    parser.add_argument('args', nargs=argparse.REMAINDER, help='A list of arguments')

    args = parser.parse_args()

    # Print the parsed arguments
    equation = "".join(args.args)
    print(f"Your equation is {equation}")

if __name__ == "__main__":
    main()

