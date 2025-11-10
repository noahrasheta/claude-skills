#!/usr/bin/env python3
"""
Lean Canvas Generator
Creates a one-page business model canvas from PRD data
"""

import json
import os
from pathlib import Path
from datetime import datetime

class LeanCanvasGenerator:
    def __init__(self):
        self.output_dir = Path('outputs')
        self.output_dir.mkdir(exist_ok=True)
        
    def load_prd_data(self, json_path):
        """Load PRD data from JSON file"""
        with open(json_path, 'r') as f:
            return json.load(f)
    
    def create_from_prd(self, prd_data):
        """Create lean canvas from PRD data"""
        canvas = {
            'problem': self.extract_problems(prd_data),
            'solution': self.extract_solutions(prd_data),
            'key_metrics': self.extract_metrics(prd_data),
            'unique_value_proposition': prd_data.get('value_proposition', ''),
            'unfair_advantage': prd_data.get('key_differentiators', ''),
            'channels': self.extract_channels(prd_data),
            'customer_segments': self.extract_segments(prd_data),
            'cost_structure': self.extract_costs(prd_data),
            'revenue_streams': self.extract_revenue(prd_data)
        }
        return canvas
    
    def extract_problems(self, prd_data):
        """Extract top 3 problems from PRD"""
        problem = prd_data.get('problem_statement', '').split('\n')
        return problem[:3] if problem else ['Problem not defined']
    
    def extract_solutions(self, prd_data):
        """Extract top 3 solutions from PRD"""
        features = prd_data.get('mvp_features', [])
        return [f['name'] for f in features[:3]]
    
    def extract_metrics(self, prd_data):
        """Extract key metrics from PRD"""
        metrics = []
        
        # From business model
        if 'key_metrics' in prd_data:
            metrics.extend(prd_data['key_metrics'].split('\n')[:3])
        
        # From features
        for feature in prd_data.get('mvp_features', [])[:2]:
            if 'success_metric' in feature:
                metrics.append(feature['success_metric'])
        
        return metrics[:5] if metrics else ['Metrics TBD']
    
    def extract_channels(self, prd_data):
        """Extract distribution channels"""
        channels = []
        
        platform = prd_data.get('platform', 'web')
        if platform in ['web', 'both']:
            channels.append('Web application')
        if platform in ['mobile', 'both']:
            channels.append('Mobile app stores')
        
        # Add based on product type
        product_type = prd_data.get('product_type', '')
        if 'b2b' in product_type:
            channels.extend(['Direct sales', 'Partner channels'])
        elif 'marketplace' in product_type:
            channels.extend(['SEO/Content', 'Paid acquisition'])
        else:
            channels.extend(['Social media', 'Content marketing'])
        
        return channels[:4]
    
    def extract_segments(self, prd_data):
        """Extract customer segments"""
        segments = []
        
        # Primary segment
        if 'target_audience' in prd_data:
            segments.append(prd_data['target_audience'])
        
        # Early adopters
        if 'early_adopters' in prd_data:
            segments.append(f"Early Adopters: {prd_data['early_adopters'][:100]}...")
        
        return segments if segments else ['Customer segments TBD']
    
    def extract_costs(self, prd_data):
        """Extract cost structure"""
        costs = []
        
        # Platform costs
        platform = prd_data.get('platform', 'web')
        if platform in ['web', 'both']:
            costs.append('Hosting & infrastructure')
        if platform in ['mobile', 'both']:
            costs.append('App store fees')
        
        # Integration costs
        integrations = prd_data.get('integrations', '')
        if 'payment' in integrations.lower():
            costs.append('Payment processing fees')
        if 'auth' in integrations.lower() or 'email' in integrations.lower():
            costs.append('Third-party service fees')
        
        # Standard costs
        costs.extend(['Development costs', 'Marketing & acquisition'])
        
        return costs[:5]
    
    def extract_revenue(self, prd_data):
        """Extract revenue streams"""
        revenue = []
        
        model = prd_data.get('revenue_model', 'TBD')
        pricing = prd_data.get('pricing_strategy', '')
        
        if model == 'subscription':
            revenue.append(f'Monthly/Annual subscriptions {pricing}')
        elif model == 'marketplace':
            revenue.append('Transaction fees')
            revenue.append('Premium listings')
        elif model == 'freemium':
            revenue.append('Free tier → Premium upgrades')
            revenue.append(f'Premium features {pricing}')
        elif model == 'one-time':
            revenue.append(f'One-time purchase {pricing}')
        elif model == 'ads':
            revenue.append('Advertising revenue')
        
        return revenue if revenue else ['Revenue model TBD']
    
    def generate_canvas_markdown(self, canvas, product_name):
        """Generate lean canvas in Markdown format"""
        md = f"""# Lean Canvas: {product_name}

Generated: {datetime.now().strftime('%Y-%m-%d')}

## Overview

| **PROBLEM** | **SOLUTION** | **UNIQUE VALUE PROPOSITION** |
|-------------|--------------|------------------------------|
| {self._format_list(canvas['problem'])} | {self._format_list(canvas['solution'])} | {canvas['unique_value_proposition']} |

| **KEY METRICS** | **UNFAIR ADVANTAGE** |
|-----------------|----------------------|
| {self._format_list(canvas['key_metrics'])} | {canvas['unfair_advantage'][:200] if canvas['unfair_advantage'] else 'TBD'} |

## Customer & Market

| **CUSTOMER SEGMENTS** | **CHANNELS** |
|----------------------|--------------|
| {self._format_list(canvas['customer_segments'])} | {self._format_list(canvas['channels'])} |

## Business Model

| **COST STRUCTURE** | **REVENUE STREAMS** |
|--------------------|---------------------|
| {self._format_list(canvas['cost_structure'])} | {self._format_list(canvas['revenue_streams'])} |

---

## Canvas Summary

### Problem-Solution Fit
- **Core Problem:** {canvas['problem'][0] if canvas['problem'] else 'TBD'}
- **Core Solution:** {canvas['solution'][0] if canvas['solution'] else 'TBD'}
- **Value Prop:** {canvas['unique_value_proposition']}

### Key Hypotheses to Test
1. **Problem Hypothesis:** Target customers experience the stated problem
2. **Solution Hypothesis:** Our solution effectively addresses the problem
3. **Channel Hypothesis:** We can reach customers through identified channels
4. **Revenue Hypothesis:** Customers will pay for the solution

### Next Steps
1. Validate problem through customer interviews
2. Build MVP to test solution hypothesis
3. Test channel effectiveness with small experiments
4. Validate pricing through willingness-to-pay research

---

*This Lean Canvas is a living document. Update it as you learn from customers and experiments.*
"""
        return md
    
    def _format_list(self, items):
        """Format list items for table cell"""
        if not items:
            return 'TBD'
        return '<br>'.join([f'• {item[:50]}{"..." if len(item) > 50 else ""}' for item in items[:3]])
    
    def generate_from_json(self, json_path):
        """Generate lean canvas from PRD JSON file"""
        prd_data = self.load_prd_data(json_path)
        canvas = self.create_from_prd(prd_data)
        
        product_name = prd_data.get('product_name', 'Product')
        canvas_md = self.generate_canvas_markdown(canvas, product_name)
        
        # Save canvas
        output_path = self.output_dir / f"{product_name.lower().replace(' ', '_')}_lean_canvas.md"
        with open(output_path, 'w') as f:
            f.write(canvas_md)
        
        print(f"✅ Lean Canvas generated: {output_path}")
        return output_path
    
    def interactive_create(self):
        """Interactive lean canvas creation"""
        print("\n" + "="*60)
        print("LEAN CANVAS GENERATOR")
        print("="*60)
        
        # Check for existing PRD files
        json_files = list(self.output_dir.glob('*_prd.json'))
        
        if json_files:
            print("\nFound existing PRD files:")
            for i, file in enumerate(json_files, 1):
                print(f"{i}. {file.name}")
            
            choice = input("\nSelect a PRD file number (or press Enter to create new): ")
            
            if choice.isdigit() and 1 <= int(choice) <= len(json_files):
                return self.generate_from_json(json_files[int(choice)-1])
        
        print("\nNo PRD files found. Please run 'python scripts/init_prd.py' first.")
        return None


def main():
    generator = LeanCanvasGenerator()
    generator.interactive_create()


if __name__ == '__main__':
    main()
