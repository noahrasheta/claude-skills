#!/usr/bin/env python3
"""
PRD Export Tool
Exports PRD to multiple formats: Markdown, HTML, DOCX
"""

import json
import os
from pathlib import Path
import argparse
from datetime import datetime

class PRDExporter:
    def __init__(self):
        self.output_dir = Path('outputs')
        self.output_dir.mkdir(exist_ok=True)
        
    def export_to_html(self, md_content, product_name):
        """Convert Markdown PRD to HTML"""
        
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PRD: {product_name}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .container {{
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #34495e;
            margin-top: 30px;
            border-bottom: 2px solid #ecf0f1;
            padding-bottom: 8px;
        }}
        h3 {{
            color: #7f8c8d;
            margin-top: 20px;
        }}
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }}
        pre {{
            background: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            margin-left: 0;
            padding-left: 20px;
            color: #666;
            font-style: italic;
        }}
        ul, ol {{
            margin-left: 20px;
        }}
        li {{
            margin: 8px 0;
        }}
        hr {{
            border: none;
            border-top: 2px solid #ecf0f1;
            margin: 30px 0;
        }}
        .metadata {{
            background: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }}
        .metadata p {{
            margin: 5px 0;
        }}
        .feature {{
            background: #f8f9fa;
            padding: 15px;
            border-left: 3px solid #28a745;
            margin: 15px 0;
            border-radius: 3px;
        }}
        strong {{
            color: #2c3e50;
        }}
        @media print {{
            body {{
                background: white;
            }}
            .container {{
                box-shadow: none;
                padding: 0;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
"""
        
        # Simple Markdown to HTML conversion
        lines = md_content.split('\n')
        in_code_block = False
        
        for line in lines:
            if line.startswith('```'):
                if in_code_block:
                    html += '</pre>\n'
                    in_code_block = False
                else:
                    html += '<pre>\n'
                    in_code_block = True
            elif in_code_block:
                html += line + '\n'
            elif line.startswith('# '):
                html += f'<h1>{line[2:]}</h1>\n'
            elif line.startswith('## '):
                html += f'<h2>{line[3:]}</h2>\n'
            elif line.startswith('### '):
                html += f'<h3>{line[4:]}</h3>\n'
            elif line.startswith('- '):
                html += f'<ul><li>{line[2:]}</li></ul>\n'
            elif line.startswith('**') and line.endswith('**'):
                html += f'<p><strong>{line[2:-2]}</strong></p>\n'
            elif line.startswith('> '):
                html += f'<blockquote>{line[2:]}</blockquote>\n'
            elif line == '---':
                html += '<hr>\n'
            elif line.strip():
                # Handle inline formatting
                formatted = line
                # Bold
                while '**' in formatted:
                    start = formatted.index('**')
                    formatted = formatted[:start] + '<strong>' + formatted[start+2:]
                    if '**' in formatted:
                        end = formatted.index('**')
                        formatted = formatted[:end] + '</strong>' + formatted[end+2:]
                
                html += f'<p>{formatted}</p>\n'
            else:
                html += '<br>\n'
        
        html += """
    </div>
</body>
</html>"""
        
        return html
    
    def export_to_docx_markdown(self, md_content, product_name):
        """Create a Google Docs compatible version of the PRD"""
        
        # Add formatting hints for Google Docs
        docx_md = f"""# Product Requirements Document

## {product_name}

---

**Document Information**
- Format: Google Docs Compatible
- Generated: {datetime.now().strftime('%Y-%m-%d')}
- Version: 1.0.0

---

{md_content}

---

## Import Instructions

### For Google Docs:
1. Copy all content below the line
2. Open Google Docs
3. Paste the content
4. Use Format > Clear Formatting if needed
5. Apply Google Docs styles as desired

### For Microsoft Word:
1. Save this file with .md extension
2. Open Word and import the Markdown file
3. Or copy-paste and apply styles

---

## Collaboration Notes

This document is optimized for collaborative editing. Feel free to:
- Add comments using your platform's comment feature
- Track changes if working in Word
- Use suggestion mode in Google Docs
- Add team members as collaborators

---

*End of Document*
"""
        
        return docx_md
    
    def create_combined_export(self, prd_json_path):
        """Create a combined export with all related documents"""
        
        with open(prd_json_path, 'r') as f:
            prd_data = json.load(f)
        
        product_name = prd_data.get('product_name', 'Product')
        base_name = product_name.lower().replace(' ', '_')
        
        # Check for related documents
        prd_md_path = self.output_dir / f"{base_name}_prd.md"
        stories_path = self.output_dir / f"{base_name}_user_stories.md"
        canvas_path = self.output_dir / f"{base_name}_lean_canvas.md"
        
        combined = f"""# Complete Product Documentation: {product_name}

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## Table of Contents

1. [Product Requirements Document](#product-requirements-document)
2. [Lean Canvas](#lean-canvas)
3. [User Stories](#user-stories)

---

"""
        
        # Add PRD content
        if prd_md_path.exists():
            with open(prd_md_path, 'r') as f:
                combined += f.read() + "\n\n---\n\n"
        
        # Add Lean Canvas
        if canvas_path.exists():
            with open(canvas_path, 'r') as f:
                combined += f.read() + "\n\n---\n\n"
        
        # Add User Stories
        if stories_path.exists():
            with open(stories_path, 'r') as f:
                combined += f.read() + "\n\n---\n\n"
        
        return combined
    
    def export_all_formats(self, prd_json_path):
        """Export PRD to all available formats"""
        
        with open(prd_json_path, 'r') as f:
            prd_data = json.load(f)
        
        product_name = prd_data.get('product_name', 'Product')
        base_name = product_name.lower().replace(' ', '_')
        
        # Load PRD Markdown
        prd_md_path = self.output_dir / f"{base_name}_prd.md"
        if not prd_md_path.exists():
            print(f"Error: PRD markdown file not found at {prd_md_path}")
            return []
        
        with open(prd_md_path, 'r') as f:
            md_content = f.read()
        
        exported_files = []
        
        # Export as HTML
        html_content = self.export_to_html(md_content, product_name)
        html_path = self.output_dir / f"{base_name}_prd.html"
        with open(html_path, 'w') as f:
            f.write(html_content)
        exported_files.append(html_path)
        print(f"✅ HTML: {html_path}")
        
        # Export as DOCX-compatible Markdown
        docx_content = self.export_to_docx_markdown(md_content, product_name)
        docx_path = self.output_dir / f"{base_name}_prd_gdocs.md"
        with open(docx_path, 'w') as f:
            f.write(docx_content)
        exported_files.append(docx_path)
        print(f"✅ Google Docs Compatible: {docx_path}")
        
        # Create combined document
        combined_content = self.create_combined_export(prd_json_path)
        combined_path = self.output_dir / f"{base_name}_complete_documentation.md"
        with open(combined_path, 'w') as f:
            f.write(combined_content)
        exported_files.append(combined_path)
        print(f"✅ Combined Documentation: {combined_path}")
        
        # Also export combined as HTML
        combined_html = self.export_to_html(combined_content, f"{product_name} - Complete")
        combined_html_path = self.output_dir / f"{base_name}_complete_documentation.html"
        with open(combined_html_path, 'w') as f:
            f.write(combined_html)
        exported_files.append(combined_html_path)
        print(f"✅ Combined HTML: {combined_html_path}")
        
        return exported_files
    
    def run_interactive(self, format_type='all'):
        """Run interactive export"""
        print("\n" + "="*60)
        print("PRD EXPORT TOOL")
        print("="*60)
        
        # Check for existing PRD files
        json_files = list(self.output_dir.glob('*_prd.json'))
        
        if not json_files:
            print("\nNo PRD files found. Please run 'python scripts/init_prd.py' first.")
            return None
        
        print("\nFound PRD files:")
        for i, file in enumerate(json_files, 1):
            print(f"{i}. {file.name}")
        
        choice = input("\nSelect a PRD file number to export: ")
        
        if choice.isdigit() and 1 <= int(choice) <= len(json_files):
            prd_path = json_files[int(choice)-1]
            
            print(f"\nExporting {prd_path.name}...")
            
            if format_type == 'all':
                exported = self.export_all_formats(prd_path)
                
                print("\n" + "="*60)
                print("EXPORT COMPLETE!")
                print("="*60)
                print("\nFiles created:")
                for file in exported:
                    print(f"  📄 {file.name}")
                
                print("\n💡 Tips:")
                print("  - HTML files can be opened directly in a browser")
                print("  - *_gdocs.md files are optimized for Google Docs import")
                print("  - Complete documentation includes PRD, Canvas, and Stories")
                
            return exported
        else:
            print("\nInvalid selection.")
            return None


def main():
    parser = argparse.ArgumentParser(description='Export PRD to multiple formats')
    parser.add_argument(
        '--format',
        choices=['md', 'html', 'docx', 'all'],
        default='all',
        help='Export format'
    )
    parser.add_argument(
        '--input',
        help='Path to PRD JSON file',
        required=False
    )
    parser.add_argument(
        '--output',
        help='Output file path',
        required=False
    )
    
    args = parser.parse_args()
    
    exporter = PRDExporter()
    
    if args.input:
        if Path(args.input).exists():
            exporter.export_all_formats(args.input)
        else:
            print(f"Error: File {args.input} not found")
    else:
        exporter.run_interactive(args.format)


if __name__ == '__main__':
    main()
