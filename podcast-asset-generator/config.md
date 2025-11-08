# Podcast Asset Generator - Configuration

This file contains all the key settings for the podcast asset generator skill. Edit these values to customize the models and settings used for asset generation.

---

## AI Models Configuration

### Image Generation Model
```
bytedance/seedream-3
```

**Notes**: 
- High-quality image generation
- Good for podcast cover art and promotional images
- Fast generation time

**Alternative Models** (comment/uncomment as needed):
```
# black-forest-labs/flux-schnell
# black-forest-labs/flux-dev
# ideogram-ai/ideogram-v3-turbo
# stability-ai/sdxl
```

---

### Video Generation Model
```
bytedance/seedance-1-lite
```

**Notes**:
- Optimized for promotional video content
- Good balance of quality and speed
- Suitable for social media formats

**Alternative Models** (comment/uncomment as needed):
```
# wan-video/wan-2.5-t2v
# stability-ai/stable-video-diffusion
```

---

## Default Generation Settings

### Image Settings
- **Default Aspect Ratio**: `1:1` (square)
- **Quality**: High
- **Output Count**: 1

**Available Aspect Ratios**:
- `1:1` - Square (podcast cover art, Instagram posts)
- `16:9` - Widescreen (YouTube thumbnails)
- `9:16` - Vertical (Instagram Stories, Reels)
- `4:5` - Portrait (Instagram feed optimization)

---

### Video Settings
- **Default Duration**: `10` seconds
- **Default Aspect Ratio**: `9:16` (vertical for Reels/Stories)
- **Quality**: High

**Available Aspect Ratios**:
- `9:16` - Vertical (Instagram Reels, Stories, TikTok)
- `1:1` - Square (Instagram/Facebook feed)
- `16:9` - Horizontal (YouTube Shorts, landscape)

---

## Content Preferences

### Summary Guidelines
- **Target Length**: 100-150 words
- **Structure**: Hook → Core Content → Takeaway
- **Tone**: Conversational yet professional
- **Tense**: Present tense for describing content

### Quote Selection
- **Optimal Length**: 50-150 characters
- **Count**: 3-4 quotes per episode
- **Requirements**:
  - Standalone clarity
  - Emotionally resonant
  - Suitable for text overlay

---

## Podcast-Specific Settings

### Brand Voice
- **Podcast Name**: Secular Buddhism Podcast
- **Host**: Noah Rasheta
- **Primary Topics**: Mindfulness, Buddhist philosophy, secular approach
- **Target Audience**: People interested in practical wisdom without religious dogma

### Visual Style Preferences
- **Image Style**: Minimalist, zen-inspired, contemplative
- **Color Palette**: Muted earth tones, natural colors, occasional pops of meaning
- **Composition**: Clean, professional, space for breathing
- **Avoid**: Overly busy designs, religious symbolism, cliché imagery

### Video Style Preferences
- **Motion**: Slow, gentle, contemplative (matches podcast tone)
- **Themes**: Nature-based, abstract, metaphorical
- **Pacing**: Calm and meditative
- **Text Overlay**: Always leave space for centered text

---

## Social Media Optimization

### Primary Platforms
1. Instagram (Reels, Feed, Stories)
2. YouTube (Shorts, video podcasts)
3. LinkedIn (professional audience)
4. Newsletter/Email

### Hashtag Strategy
**Primary Tags**: #SecularBuddhism #Mindfulness #BuddhistPhilosophy #Podcast
**Engagement Tags**: #Wisdom #InnerPeace #Meditation #PersonalGrowth
**Niche Tags**: Episode-specific philosophical concepts

---

## File Naming Convention

### Template
```
SB_E[EPISODE_NUMBER]_[TOPIC]_[TYPE]_[SPECS].[EXT]
```

### Examples
```
SB_E213_Zen_Koans_Image_1x1.png
SB_E213_Zen_Koans_Video_9x16.mp4
SB_E213_Zen_Koans_Quote1.png
```

---

## Notes for Future Updates

### To Change Image Model:
1. Edit the "Image Generation Model" section above
2. Update to new model identifier
3. Test with a simple prompt first

### To Change Video Model:
1. Edit the "Video Generation Model" section above
2. Update to new model identifier
3. Adjust duration/aspect ratio if model has different limits

### To Adjust Output Preferences:
- Modify the "Default Generation Settings" section
- Update aspect ratios based on platform priorities
- Adjust quality/duration based on needs and costs

---

**Last Updated**: November 7, 2025  
**Version**: 2.0 (MCP Integration)
