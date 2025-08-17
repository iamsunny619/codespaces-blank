def hello(name,lang):
    greetings = {
        "English":"Hello",
        "Spanish":"Hola",
        "Hindi":"Namaste"
    }
    msg = f"{greetings[lang]} {name}"
    print(msg)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
    description="Provide a personal Greetings"
    )

    parser.add_argument("-n","--name",metavar="NAME",required=True,help="add your name")
    parser.add_argument("-l","--lang",metavar="lanaguage",required=True,choices=["English","Spanish","Hindi"],help="select your language.")
    args = parser.parse_args()
    hello(args.name,args.lang)