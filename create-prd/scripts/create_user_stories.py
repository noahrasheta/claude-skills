#!/usr/bin/env python3
"""
User Story Generator
Creates INVEST-compliant user stories from features
"""

import json
from pathlib import Path
import argparse

class UserStoryGenerator:
    def __init__(self):
        self.output_dir = Path('outputs')
        self.output_dir.mkdir(exist_ok=True)
    
    def create_story(self, feature_name, feature_desc, persona_name="user"):
        """Create a single user story with acceptance criteria"""
        
        # Generate user story format
        story = {
            'title': feature_name,
            'description': feature_desc,
            'story': self.generate_story_text(feature_name, feature_desc, persona_name),
            'acceptance_criteria': self.generate_acceptance_criteria(feature_name, feature_desc),
            'notes': [],
            'priority': 'Must Have',
            'estimation': 'TBD'
        }
        
        return story
    
    def generate_story_text(self, feature_name, feature_desc, persona_name):
        """Generate user story in standard format"""
        
        # Parse feature to understand intent
        feature_lower = feature_name.lower()
        desc_lower = feature_desc.lower()
        
        # Determine action and benefit based on feature
        if 'login' in feature_lower or 'auth' in feature_lower:
            action = "log in to the application"
            benefit = "access my personalized content and features"
        elif 'register' in feature_lower or 'signup' in feature_lower:
            action = "create an account"
            benefit = "start using the application and save my preferences"
        elif 'profile' in feature_lower:
            action = "manage my profile"
            benefit = "keep my information up to date"
        elif 'search' in feature_lower:
            action = "search for content"
            benefit = "quickly find what I'm looking for"
        elif 'dashboard' in feature_lower:
            action = "view a dashboard"
            benefit = "see all important information at a glance"
        elif 'payment' in feature_lower or 'checkout' in feature_lower:
            action = "make a payment"
            benefit = "complete my purchase securely"
        elif 'notification' in feature_lower:
            action = "receive notifications"
            benefit = "stay informed about important updates"
        elif 'upload' in feature_lower:
            action = "upload files"
            benefit = "share my content with others"
        elif 'download' in feature_lower:
            action = "download content"
            benefit = "access information offline"
        elif 'share' in feature_lower:
            action = "share content"
            benefit = "collaborate with others"
        else:
            # Generic fallback
            action = f"use {feature_name}"
            benefit = "accomplish my goals efficiently"
        
        return f"As a {persona_name}, I want to {action} so that I can {benefit}"
    
    def generate_acceptance_criteria(self, feature_name, feature_desc):
        """Generate acceptance criteria for the feature"""
        
        criteria = []
        feature_lower = feature_name.lower()
        
        # Common acceptance criteria patterns
        criteria.append(f"GIVEN I am a user, WHEN I access {feature_name}, THEN I should see the main interface")
        
        # Feature-specific criteria
        if 'login' in feature_lower or 'auth' in feature_lower:
            criteria.extend([
                "GIVEN valid credentials, WHEN I submit the login form, THEN I should be authenticated successfully",
                "GIVEN invalid credentials, WHEN I submit the login form, THEN I should see an error message",
                "GIVEN I am logged in, WHEN my session expires, THEN I should be prompted to login again"
            ])
        elif 'register' in feature_lower or 'signup' in feature_lower:
            criteria.extend([
                "GIVEN valid information, WHEN I submit the registration form, THEN my account should be created",
                "GIVEN an existing email, WHEN I try to register, THEN I should see an appropriate error message",
                "GIVEN I complete registration, WHEN the process is done, THEN I should receive a confirmation"
            ])
        elif 'search' in feature_lower:
            criteria.extend([
                "GIVEN I enter a search query, WHEN I submit the search, THEN I should see relevant results",
                "GIVEN no results match, WHEN I search, THEN I should see a 'no results' message",
                "GIVEN I search, WHEN results are shown, THEN I should be able to filter and sort them"
            ])
        elif 'dashboard' in feature_lower:
            criteria.extend([
                "GIVEN I have data, WHEN I view the dashboard, THEN I should see my key metrics",
                "GIVEN data updates, WHEN I refresh, THEN I should see the latest information",
                "GIVEN I am on the dashboard, WHEN I interact with elements, THEN I should be able to drill down for details"
            ])
        elif 'payment' in feature_lower:
            criteria.extend([
                "GIVEN valid payment details, WHEN I submit payment, THEN the transaction should be processed",
                "GIVEN invalid payment details, WHEN I submit, THEN I should see an error message",
                "GIVEN successful payment, WHEN complete, THEN I should receive a confirmation"
            ])
        else:
            # Generic criteria
            criteria.extend([
                f"GIVEN I have access, WHEN I use {feature_name}, THEN it should work as described",
                f"GIVEN an error occurs, WHEN using {feature_name}, THEN I should see a helpful error message"
            ])
        
        # Add performance criteria
        criteria.append(f"GIVEN normal conditions, WHEN I use {feature_name}, THEN response time should be under 2 seconds")
        
        # Add accessibility criteria
        criteria.append(f"GIVEN I use assistive technology, WHEN I access {feature_name}, THEN it should be fully accessible (WCAG 2.1 AA)")
        
        return criteria[:5]  # Return top 5 most relevant criteria
    
    def create_stories_from_prd(self, prd_json_path):
        """Create user stories from PRD JSON file"""
        
        with open(prd_json_path, 'r') as f:
            prd_data = json.load(f)
        
        stories = []
        
        # Extract persona name
        persona_name = "user"
        if 'primary_persona' in prd_data and 'name' in prd_data['primary_persona']:
            persona_name = prd_data['primary_persona']['name']
        
        # Create stories for each MVP feature
        for feature in prd_data.get('mvp_features', []):
            # Use existing user story if available
            if 'user_story' in feature and feature['user_story']:
                story_text = feature['user_story']
            else:
                story_text = self.generate_story_text(
                    feature['name'],
                    feature['description'],
                    persona_name
                )
            
            story = {
                'title': feature['name'],
                'description': feature['description'],
                'story': story_text,
                'acceptance_criteria': self.generate_acceptance_criteria(
                    feature['name'],
                    feature['description']
                ),
                'priority': self.get_priority(feature.get('priority', 1)),
                'success_metric': feature.get('success_metric', 'TBD'),
                'notes': []
            }
            
            stories.append(story)
        
        return stories, prd_data.get('product_name', 'Product')
    
    def get_priority(self, priority_num):
        """Convert priority number to MoSCoW method"""
        if priority_num <= 2:
            return "Must Have"
        elif priority_num == 3:
            return "Should Have"
        elif priority_num == 4:
            return "Could Have"
        else:
            return "Won't Have (this release)"
    
    def generate_stories_document(self, stories, product_name):
        """Generate user stories document in Markdown"""
        
        doc = f"""# User Stories: {product_name}

## Overview
This document contains INVEST-compliant user stories for {product_name}.

### INVEST Criteria
- **I**ndependent: Each story can be developed independently
- **N**egotiable: Details can be discussed and refined
- **V**aluable: Each story provides value to users
- **E**stimable: Stories can be estimated for effort
- **S**mall: Stories are small enough to complete in a sprint
- **T**estable: Clear acceptance criteria for testing

---

## User Stories

"""
        
        for i, story in enumerate(stories, 1):
            doc += f"""### Story {i}: {story['title']}

**Priority:** {story['priority']}

**User Story:**
> {story['story']}

**Description:**
{story['description']}

**Acceptance Criteria:**
"""
            for criterion in story['acceptance_criteria']:
                doc += f"- {criterion}\n"
            
            doc += f"""
**Success Metric:** {story['success_metric']}

---

"""
        
        doc += """## Story Map

### Release 1 (MVP)
"""
        must_haves = [s for s in stories if s['priority'] == 'Must Have']
        for story in must_haves:
            doc += f"- ✅ {story['title']}\n"
        
        doc += """
### Release 2 (Enhancement)
"""
        should_haves = [s for s in stories if s['priority'] == 'Should Have']
        for story in should_haves:
            doc += f"- 📋 {story['title']}\n"
        
        doc += """
### Backlog
"""
        could_haves = [s for s in stories if s['priority'] in ['Could Have', "Won't Have (this release)"]]
        for story in could_haves:
            doc += f"- 💭 {story['title']}\n"
        
        doc += """
---

## Definition of Done

A user story is considered "done" when:

1. ✅ All acceptance criteria are met
2. ✅ Code is written and reviewed
3. ✅ Unit tests are written and passing
4. ✅ Feature is tested on all target platforms
5. ✅ Documentation is updated
6. ✅ Feature is deployed to staging environment
7. ✅ Product owner has accepted the story

---

## Notes for Development

- Each story should be broken down into technical tasks during sprint planning
- Acceptance criteria should be turned into automated tests where possible
- Stories may be split if they're too large for a single sprint
- Dependencies between stories should be identified during planning

---

*Generated by create-prd skill*
"""
        
        return doc
    
    def save_stories(self, stories, product_name):
        """Save user stories to file"""
        
        # Save as JSON
        json_path = self.output_dir / f"{product_name.lower().replace(' ', '_')}_user_stories.json"
        with open(json_path, 'w') as f:
            json.dump(stories, f, indent=2)
        
        # Save as Markdown
        doc = self.generate_stories_document(stories, product_name)
        md_path = self.output_dir / f"{product_name.lower().replace(' ', '_')}_user_stories.md"
        with open(md_path, 'w') as f:
            f.write(doc)
        
        return md_path, json_path
    
    def run_interactive(self):
        """Run interactive user story generation"""
        print("\n" + "="*60)
        print("USER STORY GENERATOR")
        print("="*60)
        
        # Check for existing PRD files
        json_files = list(self.output_dir.glob('*_prd.json'))
        
        if not json_files:
            print("\nNo PRD files found. Please run 'python scripts/init_prd.py' first.")
            return None
        
        print("\nFound PRD files:")
        for i, file in enumerate(json_files, 1):
            print(f"{i}. {file.name}")
        
        choice = input("\nSelect a PRD file number: ")
        
        if choice.isdigit() and 1 <= int(choice) <= len(json_files):
            prd_path = json_files[int(choice)-1]
            
            print(f"\nGenerating user stories from {prd_path.name}...")
            
            stories, product_name = self.create_stories_from_prd(prd_path)
            md_path, json_path = self.save_stories(stories, product_name)
            
            print(f"\n✅ User stories generated successfully!")
            print(f"📄 Markdown: {md_path}")
            print(f"📊 JSON: {json_path}")
            
            return md_path
        else:
            print("\nInvalid selection.")
            return None


def main():
    parser = argparse.ArgumentParser(description='Generate user stories from PRD')
    parser.add_argument('--input', help='Path to PRD JSON file', required=False)
    
    args = parser.parse_args()
    
    generator = UserStoryGenerator()
    
    if args.input:
        if Path(args.input).exists():
            stories, product_name = generator.create_stories_from_prd(args.input)
            md_path, json_path = generator.save_stories(stories, product_name)
            print(f"✅ User stories generated: {md_path}")
        else:
            print(f"Error: File {args.input} not found")
    else:
        generator.run_interactive()


if __name__ == '__main__':
    main()
