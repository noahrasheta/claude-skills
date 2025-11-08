# Quick Start Guide - Podcast Asset Generator

---

## The One File You Need to Know About

### 📝 `config.md` - Your Control Panel

This is your **single source of truth** for all settings. Everything is configured in the config.md file. 

**What's inside:**
- ✅ Image generation model
- ✅ Video generation model  
- ✅ Default aspect ratios
- ✅ Quality settings
- ✅ Brand voice preferences
- ✅ Social media strategy

**To change models:** Just edit the model names in config.md. That's it!

---

## How to Use the Skill

### 1. Upload Your Transcript
Upload a markdown file with your podcast episode transcript.

### 2. Ask Claude to Generate Assets
```
"Generate podcast assets for this episode"
```

### 3. Claude Will Automatically:
- ✅ Read the current models from config.md
- ✅ Analyze your transcript
- ✅ Write the episode summary
- ✅ Extract compelling quotes
- ✅ Create image/video prompts
- ✅ Generate assets via Replicate MCP
- ✅ Compile everything into a deliverable package

---

## Default Configuration 
Don't change these here, this is for your reference only. Change them in the config file if you want to change the models.

**Image Model**: `bytedance/seedream-3`  
**Video Model**: `bytedance/seedance-1-lite`

*(See config.md for full settings)*

---

## How to Change Models

### Option 1: Edit config.md Directly
1. Open `config.md`
2. Find the model section you want to change
3. Update the model name
4. Save the file
5. Done! Next time you use the skill, it'll use the new model

### Option 2: Ask Claude
```
"Please update the image model to [model-name] in the config"
```

Claude will edit config.md for you.

---

## What Python Scripts Are Used?

- `analyze_transcript.py` - This script extracts useful quotes from the podcast transcript.

---

## Typical Workflow

```
YOU: [Upload transcript]
YOU: "Generate podcast assets for this episode"

CLAUDE:
1. Reads config.md for current models
2. Analyzes transcript
3. Creates summary (100-150 words)
4. Extracts 3-4 quotes
5. Crafts image prompt
6. Generates image with bytedance/seedream-3
7. Crafts video prompt  
8. Generates video with bytedance/seedance-1-lite
9. Compiles everything into formatted output

YOU: [Downloads assets, posts to social media]
```

---

## Testing New Models

Want to try a different model? Here's the process:

1. **Edit config.md**
   - Change model name
   - Update any notes

2. **Generate test assets**
   - Use a short test transcript
   - See if output quality is good

3. **Keep or revert**
   - Like it? Keep the new model
   - Don't like it? Change back in config.md

No code changes needed. No API re-configuration. Just edit one line.

---

## Troubleshooting

### "Model not found" error
- Check the model name in config.md
- Verify it exists on Replicate
- Make sure MCP server is connected

### "Generation failed" error
- Try a simpler prompt
- Check if the model is currently available
- Consider switching to alternative model in config.md

### Want to test without using credits?
- Comment out the actual generation calls
- Just test the prompt creation
- Review the formatted output

---

## Pro Tips

### Tip 1: Keep Alternative Models Ready
In config.md, keep commented-out alternatives so you can quickly swap:

```
# Current
bytedance/seedream-3

# Alternatives (uncomment to switch)
# black-forest-labs/flux-schnell
# ideogram-ai/ideogram-v3-turbo
```

### Tip 2: Document Your Model Changes
Add notes in config.md about why you changed models:

```
bytedance/seedream-3

Notes: Switched from ideogram on 11/7/25
- Better handling of abstract concepts
- Faster generation
- More consistent zen aesthetic
```

### Tip 3: Version Control
If you're tracking changes, config.md makes it easy to see what changed:
- Model updates
- Preference changes
- Setting adjustments

All in one diff!

---

*Last Updated: November 7, 2025*  
*Version: 2.0*
