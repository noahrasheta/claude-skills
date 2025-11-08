#!/usr/bin/env python3
"""
Analyze podcast transcript to extract quotes, themes, and generate summaries.
"""

import re
import json
from pathlib import Path


def extract_meaningful_quotes(transcript_text, min_length=50, max_length=200, num_quotes=5):
    """
    Extract compelling quotes from transcript that work well for promotional content.
    
    Args:
        transcript_text: Full transcript text
        min_length: Minimum character length for a quote
        max_length: Maximum character length for a quote
        num_quotes: Number of quotes to extract
    
    Returns:
        List of quote dictionaries with text and context
    """
    # Split into sentences (basic approach)
    sentences = re.split(r'[.!?]+', transcript_text)
    
    quotes = []
    for sentence in sentences:
        sentence = sentence.strip()
        length = len(sentence)
        
        if min_length <= length <= max_length:
            # Score based on qualities that make good social media quotes
            score = 0
            
            # Prefer sentences with these qualities
            thought_starters = ['imagine', 'consider', 'think about', 'what if', 'remember']
            emotional_words = ['feel', 'realize', 'understand', 'discover', 'change']
            insight_words = ['because', 'therefore', 'actually', 'essentially', 'fundamentally']
            
            sentence_lower = sentence.lower()
            
            if any(word in sentence_lower for word in thought_starters):
                score += 3
            if any(word in sentence_lower for word in emotional_words):
                score += 2
            if any(word in sentence_lower for word in insight_words):
                score += 2
                
            # Penalize questions (usually don't work as well for promos)
            if sentence.strip().endswith('?'):
                score -= 1
            
            # Prefer medium-length quotes
            if 80 <= length <= 150:
                score += 2
                
            quotes.append({
                'text': sentence,
                'score': score,
                'length': length
            })
    
    # Sort by score and return top quotes
    quotes.sort(key=lambda x: x['score'], reverse=True)
    return [q['text'] for q in quotes[:num_quotes]]


def generate_summary_outline(transcript_text, max_words=150):
    """
    Generate a structured outline to help with summary creation.
    Returns key themes and concepts found in the transcript.
    
    Args:
        transcript_text: Full transcript text
        max_words: Target word count for summary
    
    Returns:
        Dictionary with themes and key points
    """
    # This is a simple keyword extraction approach
    # In practice, Claude will do the actual summarization
    
    words = transcript_text.lower().split()
    total_words = len(words)
    
    # Common Buddhist/mindfulness terms to look for
    key_concepts = [
        'mindfulness', 'meditation', 'awareness', 'suffering', 'compassion',
        'impermanence', 'emptiness', 'dharma', 'practice', 'attachment',
        'ego', 'self', 'consciousness', 'present', 'moment', 'peace'
    ]
    
    found_concepts = []
    for concept in key_concepts:
        count = words.count(concept)
        if count > 0:
            found_concepts.append({
                'concept': concept,
                'frequency': count,
                'density': count / total_words * 1000  # per 1000 words
            })
    
    found_concepts.sort(key=lambda x: x['frequency'], reverse=True)
    
    return {
        'total_words': total_words,
        'estimated_duration_minutes': total_words / 150,  # average speaking rate
        'key_concepts': found_concepts[:5],
        'target_summary_words': max_words
    }


def read_transcript(file_path):
    """Read transcript from markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def main():
    """Example usage of the transcript analysis functions."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python analyze_transcript.py <transcript_file.md>")
        sys.exit(1)
    
    transcript_path = sys.argv[1]
    transcript_text = read_transcript(transcript_path)
    
    # Extract quotes
    quotes = extract_meaningful_quotes(transcript_text, num_quotes=3)
    
    # Generate summary outline
    outline = generate_summary_outline(transcript_text)
    
    # Output as JSON
    result = {
        'quotes': quotes,
        'analysis': outline
    }
    
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
