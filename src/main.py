from textnode import TextNode, Bender

def main():
    node = TextNode(
        "This is some anchor text",
        Bender.AIR_BENDER,
        "https://www.boot.dev"
    )
    print(node)

main()