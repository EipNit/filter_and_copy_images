# Filter and Copy Images

This script `filter_and_copy_images.py` filters images based on corresponding label files and copies them, along with the label files, into a new directory structure. The script assumes that images are in `.jpg` format and labels are in `.txt` format. 

## Features
- Traverses a directory of label files and copies both label files and corresponding image files into a specified output directory.
- Automatically creates the necessary output subdirectories for images and labels.
- Ensures the images and labels are transferred together, only if both are present.

## Requirements
- Python 3.x
- `shutil` (standard Python library)
- `os` (standard Python library)

## Directory Structure

### Input (Original Files)
- `data_mouse_time/`
  - `images/` — contains the image files.
  - `labels/` — contains the label files.

### Output (Filtered Files)
- `data_mouse_labels/`
  - `images/` — will contain the copied image files.
  - `labels/` — will contain the copied label files.

## Usage

1. Ensure the input directories are set up as expected under `data_mouse_time/`, with images in the `images/` folder and corresponding labels in the `labels/` folder.
   
2. Run the script:

    ```bash
    python filter_and_copy_images.py
    ```

3. The output will be generated in the `data_mouse_labels/` directory, with `images/` and `labels/` subdirectories containing the copied files.

## Example

If your input directory contains the following files:
- `data_mouse_time/images/sample1.jpg`
- `data_mouse_time/labels/sample1.txt`

The script will copy them to:
- `data_mouse_labels/images/sample1.jpg`
- `data_mouse_labels/labels/sample1.txt`

## Customization

You can modify the following paths in the script based on your project structure:

```python
data_dir = "data_mouse_time"
output_dir = "data_mouse_labels"
```
