import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

   
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    heap = []
    for char, freq in frequency.items():
        heapq.heappush(heap, Node(char, freq))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(root, current_code="", codes={}):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code

    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)

    return codes


def huffman_encoding(text):
    root = build_huffman_tree(text)
    codes = generate_codes(root)

    encoded_text = "".join([codes[char] for char in text])

    return codes, encoded_text



text = "huffman coding example"
codes, encoded_text = huffman_encoding(text)

print("Huffman Codes:")
for char, code in codes.items():
    print(f"{char}: {code}")

print("\nEncoded Text:", encoded_text)