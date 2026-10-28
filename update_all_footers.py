#!/usr/bin/env python3
"""
Script to replace all footer sections in HTML files with dynamic footer loader.
This will replace the entire footer section with a placeholder div and script tag.
"""

import os
import re
from pathlib import Path

# Files to skip
SKIP_FILES = ['footer.html']

# The replacement footer HTML
REPLACEMENT = '''<!-- ══ FOOTER ══ -->
<div id="footer-placeholder"></div>
<script src="load-footer.js"></script>'''

def find_footer_section(content):
    """Find the footer section in the HTML content."""
    # Look for footer comment markers
    patterns = [
        r'<!-- ══ FOOTER ══ -->.*?</footer>',
        r'<!-- FOOTER -->.*?</footer>',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            return match.start(), match.end()
    
    return None, None

def update_file(filepath):
    """Update a single HTML file to use dynamic footer."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        start, end = find_footer_section(content)
        
        if start is not None and end is not None:
            new_content = content[:start] + REPLACEMENT + content[end:]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True
        else:
            return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Main function to update all HTML files."""
    current_dir = Path('.')
    html_files = [f for f in current_dir.glob('*.html') if f.name not in SKIP_FILES]
    
    updated = 0
    skipped = 0
    
    for html_file in html_files:
        if update_file(html_file):
            print(f"✓ Updated: {html_file.name}")
            updated += 1
        else:
            print(f"⚠ Skipped: {html_file.name} (footer not found or already updated)")
            skipped += 1
    
    print(f"\n✓ Updated {updated} files")
    print(f"⚠ Skipped {skipped} files")

if __name__ == '__main__':
    main()
