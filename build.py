import os
from bs4 import BeautifulSoup

# Define file paths for the input TXT and HTML files, and the output HTML file
txt_file_path = 'cc.gru'
html_file_path = 'template.html'
output_file_path = 'build/index.html'

# Read in the contents of the TXT file
with open(txt_file_path, 'r') as f:
    txt_contents = f.read()

# Read in the contents of the HTML file and create a BeautifulSoup object
with open(html_file_path, 'r') as f:
    html_contents = f.read()

# Replace the contents of the textarea with ID gsEdit in the HTML file with the contents of the TXT file
html_contents = html_contents \
                    .replace('<textarea id="gsEdit" style="display: none;"></textarea>',
                            f'<textarea id="gsEdit" style="display: none;">{txt_contents}</textarea>')

# Write the modified HTML file to the output file path
with open(output_file_path, 'w') as f:
    f.write(html_contents)

# Print a confirmation message
print(f'Successfully inserted contents of "{txt_file_path}" into "{html_file_path}" and saved as "{output_file_path}"')

