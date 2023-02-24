import os
import cairosvg

def convert_file(file_path):
    png_path = os.path.splitext(file_path)[0] + ".png"
    try:
        png_data = cairosvg.svg2png(bytestring=open(file_path, 'rb').read(), output_width=1024, output_height=1024)
        with open(png_path, "wb") as f:
            f.write(png_data)
        return (True, f"Converted {file_path} to {png_path}")
    except Exception as e:
        return (False, f"Failed to convert {file_path}: {e}")

def convert_files(file_paths):
    results = []
    for file_path in file_paths:
        success, message = convert_file(file_path)
        results.append((success, message))
    return results
