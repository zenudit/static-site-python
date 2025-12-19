import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Just plain text")
        self.assertEqual(node.to_html(), "Just plain text")

    def test_leaf_to_html_span(self):
        node = LeafNode("span", "Inline text")
        self.assertEqual(node.to_html(), "<span>Inline text</span>")

    def test_leaf_no_value_raises_error(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
