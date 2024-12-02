import os
import re
import mmap
import sys
from pathlib import Path

project_dir = Path(__file__).parent.parent
if str(project_dir) not in sys.path:
    sys.path.append(str(project_dir))

def replace_regex(event):
    """
    """
    results = {}
    
    # Walk through all files in the module
    for root, directories, files in os.walk("docs/source"):
        directories[:] = [d for d in directories if d not in ["_latex", "_static", "images"]]
        for file in files:
            full_path = os.path.join(root, file)
            with open(full_path, "rb") as f, mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as s:
                content = s.read().decode('utf-8')
                
                # Find and replace regex containing the site
                modified_content = re.sub(
                    r'www.aequilibrae.com/latest/', 
                    fr'www.aequilibrae.com/{event}/', 
                    content
                )
                
                # Write modified content back to file
                with open(full_path, 'w', encoding='utf-8') as w:
                    w.write(modified_content)
