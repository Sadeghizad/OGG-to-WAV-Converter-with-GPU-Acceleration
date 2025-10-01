#!/usr/bin/env python3
"""
OGG to WAV Converter using FFmpeg
Fixed GPU acceleration placement
"""

import os
import subprocess
import sys
from pathlib import Path

def convert_ogg_to_wav(input_file, output_file=None, use_gpu=False):
    """
    Convert OGG file to WAV format
    
    Args:
        input_file (str): Path to input OGG file
        output_file (str): Path to output WAV file (optional)
        use_gpu (bool): Whether to use GPU acceleration
    
    Returns:
        bool: True if conversion successful, False otherwise
    """
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found")
        return False
    
    # Generate output filename if not provided
    if output_file is None:
        input_path = Path(input_file)
        output_file = input_path.with_suffix('.wav')
    
    # Build FFmpeg command
    cmd = ['ffmpeg']
    
    # Add GPU acceleration if requested (MUST be before input file)
    if use_gpu:
        cmd.extend(['-hwaccel', 'cuda', '-hwaccel_output_format', 'cuda'])
    
    # Add input file
    cmd.extend(['-i', input_file])
    
    # Add output options
    cmd.extend([
        '-acodec', 'pcm_s16le',  # 16-bit PCM WAV
        '-ar', '44100',          # Sample rate 44.1kHz
        '-ac', '2',              # Stereo
        '-y',                    # Overwrite output file
        str(output_file)
    ])
    
    try:
        print(f"Converting: {input_file} -> {output_file}")
        if use_gpu:
            print("Using GPU acceleration: cuda")
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✓ Successfully converted: {output_file}")
            return True
        else:
            print(f"✗ Error during conversion: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("Error: FFmpeg not found. Please install FFmpeg.")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

def batch_convert(input_folder, output_folder=None, use_gpu=False):
    """
    Convert all OGG files in a folder to WAV
    """
    
    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' not found")
        return
    
    if output_folder and not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Find all OGG files
    ogg_files = list(Path(input_folder).glob('**/*.ogg'))
    
    if not ogg_files:
        print("No OGG files found in the specified folder")
        return
    
    print(f"Found {len(ogg_files)} OGG files to convert")
    
    successful = 0
    for ogg_file in ogg_files:
        if output_folder:
            output_file = Path(output_folder) / ogg_file.with_suffix('.wav').name
        else:
            output_file = ogg_file.with_suffix('.wav')
        
        if convert_ogg_to_wav(str(ogg_file), str(output_file), use_gpu):
            successful += 1
    
    print(f"Conversion complete: {successful}/{len(ogg_files)} files converted successfully")

if __name__ == "__main__":
    # Command line usage
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single file: python ogg_to_wav.py input.ogg [output.wav] [--gpu]")
        print("  Batch conversion: python ogg_to_wav.py --batch input_folder [output_folder] [--gpu]")
        sys.exit(1)
    
    use_gpu = '--gpu' in sys.argv
    args = [arg for arg in sys.argv[1:] if arg != '--gpu']
    
    if args[0] == '--batch':
        if len(args) >= 2:
            output_folder = args[2] if len(args) >= 3 else None
            batch_convert(args[1], output_folder, use_gpu)
        else:
            print("Error: Please specify input folder for batch conversion")
    else:
        input_file = args[0]
        output_file = args[1] if len(args) >= 2 else None
        convert_ogg_to_wav(input_file, output_file, use_gpu)