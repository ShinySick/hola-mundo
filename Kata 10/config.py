def main():
    try:
        configuration = open('config')
    except Exception:
        print("No se pudo encontrar el archivo")


if __name__ == '__main__':
    main()