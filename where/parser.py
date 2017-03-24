import argparse


from where.search import Search


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run chip8 rom')
    parser.add_argument('name', nargs='*', help='rom path')
    args = parser.parse_args()
    res = Search(args.name).format_result()
