#!/usr/bin/env python3
"""
Interactive PRD Builder
Guides users through creating a comprehensive Product Requirements Document
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
import argparse

class PRDBuilder:
    def __init__(self, template_type='lean'):
        self.template_type = template_type
        self.prd_data = {
            'created_at': datetime.now().isoformat(),
            'version': '1.0.0',
            'status': 'draft'
        }
        self.output_dir = Path('outputs')
        self.output_dir.mkdir(exist_ok=True)
        
    def get_input(self, prompt, required=True, default=None):
        """Get user input with optional default value"""
        if default:
            prompt = f"{prompt} [{default}]"
        
        response = input(f"\n{prompt}: ").strip()
        
        if not response and default:
            return default
        
        if required and not response:
            print("This field is required. Please provide a value.")
            return self.get_input(prompt, required, default)
        
        return response
    
    def get_multiline_input(self, prompt):
        """Get multiline input from user"""
        print(f"\n{prompt}")
        print("(Enter 'END' on a new line when finished)")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == 'END':
                break
            lines.append(line)
        return '\n'.join(lines)
    
    def collect_basic_info(self):
        """Collect basic product information"""
        print("\n" + "="*60)
        print("PRODUCT REQUIREMENTS DOCUMENT BUILDER")
        print("="*60)
        print("\nLet's start with basic information about your product.")
        
        self.prd_data['product_name'] = self.get_input("Product Name")
        self.prd_data['product_type'] = self.get_input(
            "Product Type (consumer-app/b2b-saas/marketplace/other)",
            default=self.template_type
        )
        self.prd_data['platform'] = self.get_input(
            "Platform (web/mobile/both)",
            default="web"
        )
        
        if self.prd_data['platform'] in ['mobile', 'both']:
            self.prd_data['mobile_platforms'] = self.get_input(
                "Mobile Platforms (ios/android/both)",
                default="both"
            )
    
    def collect_problem_statement(self):
        """Collect problem statement and evidence"""
        print("\n" + "-"*40)
        print("PROBLEM DEFINITION")
        print("-"*40)
        
        self.prd_data['problem_statement'] = self.get_multiline_input(
            "What problem are you solving? Be specific:"
        )
        
        self.prd_data['target_audience'] = self.get_input(
            "Who experiences this problem? (Be specific about your target user)"
        )
        
        self.prd_data['problem_evidence'] = self.get_multiline_input(
            "What evidence do you have that this is a real problem?\n(User interviews, data, personal experience, etc.)"
        )
        
        self.prd_data['current_solutions'] = self.get_multiline_input(
            "How do people currently solve this problem?"
        )
    
    def collect_solution(self):
        """Collect solution and value proposition"""
        print("\n" + "-"*40)
        print("SOLUTION APPROACH")
        print("-"*40)
        
        self.prd_data['solution_description'] = self.get_multiline_input(
            "Describe your solution:"
        )
        
        self.prd_data['value_proposition'] = self.get_input(
            "What's your unique value proposition? (One sentence)"
        )
        
        self.prd_data['key_differentiators'] = self.get_multiline_input(
            "What makes your solution different/better?"
        )
        
        self.prd_data['solution_hypothesis'] = self.get_input(
            "What's your core hypothesis to test?"
        )
    
    def collect_user_persona(self):
        """Collect primary user persona"""
        print("\n" + "-"*40)
        print("USER PERSONA")
        print("-"*40)
        
        persona = {}
        persona['name'] = self.get_input("Persona Name (e.g., 'Busy Professional Beth')")
        persona['demographics'] = self.get_input("Age range and key demographics")
        persona['occupation'] = self.get_input("Occupation/Role")
        persona['goals'] = self.get_multiline_input("What are their main goals?")
        persona['frustrations'] = self.get_multiline_input("What frustrates them about current solutions?")
        persona['tech_savvy'] = self.get_input("Tech comfort level (low/medium/high)", default="medium")
        
        self.prd_data['primary_persona'] = persona
        
        # Early adopter characteristics
        self.prd_data['early_adopters'] = self.get_multiline_input(
            "Describe your early adopters (who will use this first?)"
        )
    
    def collect_mvp_features(self):
        """Collect MVP features"""
        print("\n" + "-"*40)
        print("MVP FEATURES (Maximum 5)")
        print("-"*40)
        print("List your core features in priority order.")
        print("Remember: Each feature should be essential for your MVP.")
        
        features = []
        for i in range(1, 6):
            print(f"\nFeature {i}:")
            name = self.get_input("Feature name", required=(i <= 3), default="")
            if not name:
                break
                
            description = self.get_input("Brief description")
            user_story = self.get_input(
                "User story (As a [user], I want to [action] so that [benefit])"
            )
            success_metric = self.get_input("How will you measure success?")
            
            features.append({
                'name': name,
                'description': description,
                'user_story': user_story,
                'success_metric': success_metric,
                'priority': i
            })
        
        self.prd_data['mvp_features'] = features
    
    def collect_technical_requirements(self):
        """Collect technical requirements"""
        print("\n" + "-"*40)
        print("TECHNICAL REQUIREMENTS")
        print("-"*40)
        
        self.prd_data['tech_stack'] = self.get_input(
            "Preferred tech stack (or 'TBD' if unsure)",
            default="TBD"
        )
        
        self.prd_data['integrations'] = self.get_multiline_input(
            "List any required integrations (Payment, Auth, APIs, etc.)\nOne per line:"
        )
        
        self.prd_data['performance_requirements'] = self.get_input(
            "Key performance requirements (load time, concurrent users, etc.)",
            required=False
        )
        
        self.prd_data['security_requirements'] = self.get_input(
            "Security/compliance requirements",
            required=False
        )
    
    def collect_business_model(self):
        """Collect business model information"""
        print("\n" + "-"*40)
        print("BUSINESS MODEL (Optional)")
        print("-"*40)
        
        include_business = self.get_input(
            "Include business model section? (yes/no)",
            default="yes"
        )
        
        if include_business.lower() == 'yes':
            self.prd_data['revenue_model'] = self.get_input(
                "Revenue model (subscription/one-time/freemium/marketplace/ads/other)"
            )
            
            self.prd_data['pricing_strategy'] = self.get_input(
                "Pricing strategy or price point",
                required=False
            )
            
            self.prd_data['key_metrics'] = self.get_multiline_input(
                "Key metrics to track (acquisition, activation, retention, etc.)"
            )
    
    def collect_assumptions_risks(self):
        """Collect assumptions and risks"""
        print("\n" + "-"*40)
        print("ASSUMPTIONS & RISKS")
        print("-"*40)
        
        self.prd_data['key_assumptions'] = self.get_multiline_input(
            "List your key assumptions:"
        )
        
        self.prd_data['main_risks'] = self.get_multiline_input(
            "What are the main risks?"
        )
        
        self.prd_data['open_questions'] = self.get_multiline_input(
            "Open questions to answer:"
        )
    
    def generate_prd(self):
        """Generate the PRD document"""
        template_path = Path(f'assets/templates/{self.template_type}_prd_template.md')
        
        if not template_path.exists():
            template_path = Path('assets/templates/lean_prd_template.md')
        
        # For now, we'll create a simple PRD structure
        # In production, this would use the template file
        prd_content = self.create_prd_content()
        
        # Save PRD data as JSON
        json_path = self.output_dir / f"{self.prd_data['product_name'].lower().replace(' ', '_')}_prd.json"
        with open(json_path, 'w') as f:
            json.dump(self.prd_data, f, indent=2)
        
        # Save PRD as Markdown
        md_path = self.output_dir / f"{self.prd_data['product_name'].lower().replace(' ', '_')}_prd.md"
        with open(md_path, 'w') as f:
            f.write(prd_content)
        
        return md_path, json_path
    
    def create_prd_content(self):
        """Create PRD content in Markdown format"""
        prd = f"""# Product Requirements Document: {self.prd_data['product_name']}

**Version:** {self.prd_data['version']}  
**Status:** {self.prd_data['status']}  
**Created:** {self.prd_data['created_at'][:10]}  
**Type:** {self.prd_data['product_type']}  
**Platform:** {self.prd_data['platform']}

---

## Executive Summary

### Problem Statement
{self.prd_data['problem_statement']}

**Target Audience:** {self.prd_data['target_audience']}

**Evidence:**
{self.prd_data['problem_evidence']}

**Current Solutions:**
{self.prd_data['current_solutions']}

### Solution
{self.prd_data['solution_description']}

**Value Proposition:** {self.prd_data['value_proposition']}

**Key Differentiators:**
{self.prd_data['key_differentiators']}

**Hypothesis to Test:** {self.prd_data['solution_hypothesis']}

---

## User Persona

### {self.prd_data['primary_persona']['name']}
- **Demographics:** {self.prd_data['primary_persona']['demographics']}
- **Occupation:** {self.prd_data['primary_persona']['occupation']}
- **Tech Savvy:** {self.prd_data['primary_persona']['tech_savvy']}

**Goals:**
{self.prd_data['primary_persona']['goals']}

**Frustrations:**
{self.prd_data['primary_persona']['frustrations']}

### Early Adopters
{self.prd_data['early_adopters']}

---

## MVP Features

"""
        
        for feature in self.prd_data['mvp_features']:
            prd += f"""### {feature['priority']}. {feature['name']}
**Description:** {feature['description']}

**User Story:** {feature['user_story']}

**Success Metric:** {feature['success_metric']}

"""
        
        prd += f"""---

## Technical Requirements

**Tech Stack:** {self.prd_data.get('tech_stack', 'TBD')}

**Integrations:**
{self.prd_data.get('integrations', 'None specified')}

**Performance Requirements:** {self.prd_data.get('performance_requirements', 'Standard web application performance')}

**Security Requirements:** {self.prd_data.get('security_requirements', 'Standard security best practices')}

"""
        
        if 'revenue_model' in self.prd_data:
            prd += f"""---

## Business Model

**Revenue Model:** {self.prd_data['revenue_model']}

**Pricing Strategy:** {self.prd_data.get('pricing_strategy', 'TBD')}

**Key Metrics:**
{self.prd_data.get('key_metrics', 'TBD')}

"""
        
        prd += f"""---

## Assumptions & Risks

### Key Assumptions
{self.prd_data['key_assumptions']}

### Main Risks
{self.prd_data['main_risks']}

### Open Questions
{self.prd_data['open_questions']}

---

## Next Steps

1. Validate core assumptions through user interviews
2. Create wireframes/mockups for MVP features
3. Develop technical architecture
4. Build MVP
5. Test with early adopters
6. Iterate based on feedback

---

*This PRD is a living document and should be updated as new information becomes available.*
"""
        
        return prd
    
    def run(self):
        """Run the complete PRD builder process"""
        try:
            # Collect all information
            self.collect_basic_info()
            self.collect_problem_statement()
            self.collect_solution()
            self.collect_user_persona()
            self.collect_mvp_features()
            self.collect_technical_requirements()
            self.collect_business_model()
            self.collect_assumptions_risks()
            
            # Generate PRD
            print("\n" + "="*60)
            print("GENERATING PRD...")
            print("="*60)
            
            md_path, json_path = self.generate_prd()
            
            print(f"\n✅ PRD created successfully!")
            print(f"📄 Markdown: {md_path}")
            print(f"📊 JSON Data: {json_path}")
            print(f"\nRun 'python scripts/export_prd.py' to generate other formats.")
            
            return True
            
        except KeyboardInterrupt:
            print("\n\n❌ PRD creation cancelled by user.")
            return False
        except Exception as e:
            print(f"\n❌ Error creating PRD: {e}")
            return False


def main():
    parser = argparse.ArgumentParser(description='Create a Product Requirements Document')
    parser.add_argument(
        '--type',
        choices=['lean', 'consumer-app', 'b2b-saas', 'marketplace', 'custom'],
        default='lean',
        help='Template type to use'
    )
    
    args = parser.parse_args()
    
    builder = PRDBuilder(template_type=args.type)
    builder.run()


if __name__ == '__main__':
    main()
