# Word Dictionary Using Red-Black Trees

## Description

This repository contains an implementation of a word dictionary using Red-Black Trees (RB Trees) data structure. The project supports efficient dictionary operations including searching, insertion, and various tree-related operations. The use of Red-Black Trees ensures that the dictionary remains balanced, providing optimal performance for these operations.

## Features

### Core Operations

1. **Search**
   - Search for a specific element in the Red-Black Tree.
2. **Insertion**
   - Insert a new node into the Red-Black Tree while maintaining tree balance through rotation operations.
3. **Print Tree Height**
   - Print the height of the Red-Black Tree, which is the longest path from the root to a leaf node.
4. **Print Black Height**
   - Print the number of black nodes in any path from the root to a leaf.
5. **Print Tree Size**
   - Print the number of elements in the Red-Black Tree.

### Dictionary-Specific Operations

1. **Load Dictionary**
   - Load a dictionary from a text file (`dictionary.txt`) where each word is on a separate line. The words are inserted into the Red-Black Tree to support efficient insertions and search operations.
2. **Insert Word**
   - Insert a word provided by the user into the dictionary. If the word already exists, an error message ("ERROR: Word already in the dictionary!") is displayed. The dictionary file is updated with the newly inserted word.
3. **Look-up a Word**
   - Look up a word provided by the user and print "YES" if the word is found in the dictionary or "NO" if it is not.

## Getting Started

### Prerequisites

- Python 3.x
- Basic understanding of data structures and algorithms, particularly Red-Black Trees.

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/rb-tree-dictionary.git
   cd rb-tree-dictionary
   ```

2. Ensure you have the necessary dependencies installed. You can use `pip` for this:
   ```sh
   pip install -r requirements.txt
   ```

### Usage

1. Load the dictionary from the provided `dictionary.txt` file:
   ```sh
   python load_dictionary.py
   ```

2. Insert a new word into the dictionary:
   ```sh
   python insert_word.py "newword"
   ```

3. Look up a word in the dictionary:
   ```sh
   python lookup_word.py "word"
   ```

4. Print tree height:
   ```sh
   python print_tree_height.py
   ```

5. Print black height:
   ```sh
   python print_black_height.py
   ```

6. Print tree size:
   ```sh
   python print_tree_size.py
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any bugs or feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Special thanks to the developers and maintainers of the Red-Black Tree data structure and algorithm resources that helped in the implementation of this project.

---

For more information, please refer to the documentation or contact the repository maintainer.

---

Feel free to reach out if you have any questions or need further assistance. Happy coding!

