# LaTeX Slide Generator

This Python script automates the creation of LaTeX-formatted slides from a plain text source. Designed for educational content, it segments the text into slides based on numerical headers, supporting a hierarchical organization into sections, subsections, and sub-subsections. It enhances readability by automatically handling itemizations, keywords, and learning objectives. Additionally, the script can paraphrase content to improve variation and clarity.

## Features

- **Automatic Slide Segmentation**: Organizes content into slides based on header levels.
- **Support for LaTeX Commands**: Generates slides with LaTeX formatting, including sections and itemizations.
- **Paraphrasing**: Utilizes a custom paraphrase function to reword text, ensuring content is engaging and varied.
- **Clear Console Compatibility**: Offers cross-platform support for clearing the console, ensuring a clean output environment.
- **File Handling**: Reads from a `source.txt` file and writes the output to `content.tex`, ready for LaTeX compilation.

## Prerequisites

- Source text file
- Python 3.x
- [Optional] LaTeX environment for compiling the generated `.tex` file.

## Setup

1. Clone the repository or download the script to your local machine.
2. Ensure you have Python installed on your system.
3. Place your source text in a file named `source.txt` in the same directory as the script. The source text should follow the specific format for headers and special frames like keywords and learning objectives.

## Usage

Run the script with Python from your terminal or command prompt:

```bash
python slide_generator.py
```

After execution, the script will read source.txt file with proper source text, and generate a `content.tex` file, containing a proper Beamer presentation in the same directory. This file can be compiled with a LaTeX editor or command-line tool to produce the final presentation slides.

## Customizing the Script

You may modify the script to adjust the number of lines per slide, paraphrasing behavior, or LaTeX formatting according to your needs. The key variables and their functions are commented within the script for easy identification and modification.

## Contributing

Contributions to improve the script or extend its functionality are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
---

For any questions or suggestions, please open an issue in the GitHub repository.