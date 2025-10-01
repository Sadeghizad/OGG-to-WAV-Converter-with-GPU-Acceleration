# OGG to WAV Converter with GPU Acceleration

## Overview
This project provides a Python script to convert OGG audio files to WAV format using FFmpeg. It includes support for GPU acceleration to enhance conversion speed. The script can handle both single file conversions and batch processing of multiple files.

## Features
- Convert OGG files to WAV format
- Optional GPU acceleration using FFmpeg
- Batch conversion of multiple OGG files
- Error handling for file operations

## Requirements
- Python 3.6 or higher
- FFmpeg installed on your system
- (Optional) CUDA for GPU acceleration

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ogg-to-wav-converter.git
   cd ogg-to-wav-converter
2. Install required Python packages:

    ```bash
    pip install -r requirements.txt
    ```
Ensure FFmpeg is installed and accessible from your command line. You can download it from FFmpeg's official website. 

## Usage
### Single File Conversion
To convert a single OGG file to WAV:
```bash
python src/ogg_to_wav.py input.ogg [output.wav] [--gpu]
```
- `input.ogg`: Path to the input OGG file.
- `output.wav`: (Optional) Path to the output WAV file. If not provided, the output file will have the same name as the input file with a `.wav` extension.
- `--gpu`: (Optional) Use GPU acceleration for conversion.

### Batch Conversion
To convert all OGG files in a folder:
```bash
python src/ogg_to_wav.py --batch input_folder [output_folder] [--gpu]
```
- `input_folder`: Path to the folder containing OGG files.
- `output_folder`: (Optional) Path to the folder where WAV files will be saved. If not provided, WAV files will be saved in the same folder as the input files.
- `--gpu`: (Optional) Use GPU acceleration for conversion.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments
- [FFmpeg](https://ffmpeg.org/) for the audio conversion capabilities.
```
