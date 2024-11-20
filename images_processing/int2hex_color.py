def int2hex(col):
    return f"{(col >> 16) & 255:x}{(col >> 8) & 255:x}{(col >> 0) & 255:x}".upper()

def main():
    print(int2hex(-3227226))

if __name__ == '__main__':
    main()
