import settings

def convertToLinkedinPrompt(
    transcript,
    number_of_posts=settings.number_of_posts,
    tone=settings.tone,
    style=settings.style,
    length=settings.length,
    hook_type=settings.hook_type,
    cta_type=settings.cta_type,
    emoji_preference=settings.emoji_preference,
    spacing=settings.spacing,
    formatting=settings.formatting,
    hashtag_preference=settings.hashtag_preference,
    industry=settings.industry,
    target_audience=settings.target_audience,
    brand_voice=settings.brand_voice,
    creator_style=settings.creator_style,
    focus=settings.focus,
    experience=settings.experience,
    perspective=settings.perspective,
    cultural_context=settings.cultural_context,
    angle=settings.angle
):
    """Converts a transcript to a LinkedIn prompt"""
    prompt = """
        You are a professional content creator specializing in LinkedIn posts. Create {number_of_posts} LinkedIn post(s) based on the following inputs and parameters:
        SOURCE CONTENT:

        YouTube Video Transcript: {transcript}

        STYLE PARAMETERS:

        Tone: {tone} [Options: Professional, Casual, Gen-Z, Motivational, Educational, Technical]
        Writing Style: {style} [Options: Story-based, Data-driven, Question-based, List format, Problem-solution]
        Post Length: {length} [Options: Short (< 800 chars), Medium (800-1500 chars), Long (1500-3000 chars)]
        Hook Style: {hook_type} [Options: Question, Statistic, Bold Statement, Personal Story, Contrarian View]
        Call-to-Action Type: {cta_type} [Options: Soft CTA, Strong CTA, Question-based CTA, None]

        FORMATTING PREFERENCES:

        Emoji Usage: {emoji_preference} [Options: None, Minimal (1-2), Moderate (3-5), Heavy (6+)]
        Line Spacing: {spacing} [Options: Compact, Regular, Airy]
        Text Formatting: {formatting} [Options: Plain, With Bold Points, With Bullet Points]
        Hashtag Usage: {hashtag_preference} [Options: None, Minimal (1-3), Moderate (4-6), Heavy (7+)]

        BRANDING ELEMENTS:

        Industry: {industry}
        Target Audience: {target_audience}
        Brand Voice: {brand_voice} [Options: Authoritative, Friendly, Innovative, Traditional]
        Creator Inspiration: {creator_style}
        Key Message Focus: {focus} [Options: Educational, Inspirational, Problem-solving, Thought Leadership]

        PERSONALIZATION:

        Personal Experience Level: {experience} [Options: Beginner, Intermediate, Expert]
        Unique Perspective: {perspective} [Options: First-hand experience, Research-based, Opinion, Case study]
        Cultural Context: {cultural_context} [Options: Global, Region-specific, Industry-specific]
        Content Angle: {angle} [Options: Success story, Learning experience, Industry insight, Trend analysis]

        Create {number_of_posts} unique LinkedIn posts that are:

        Engaging and scroll-stopping
        Relevant to the source content
        Formatted according to the specified preferences
        Aligned with the chosen creator's style while maintaining authenticity
        Optimized for LinkedIn's algorithm

        Format each post as:
        Post 1:
        [Post content]
        Post 2:
        [Post content]
        Post 3:
        [Post content]
    """.format(
        transcript=transcript,
        tone=tone,
        style=style,
        length=length,
        hook_type=hook_type,
        cta_type=cta_type,
        emoji_preference=emoji_preference,
        spacing=spacing,
        formatting=formatting,
        hashtag_preference=hashtag_preference,
        industry=industry,
        target_audience=target_audience,
        brand_voice=brand_voice,
        creator_style=creator_style,
        focus=focus,
        experience=experience,
        perspective=perspective,
        cultural_context=cultural_context,
        angle=angle,
        number_of_posts=number_of_posts
    )

    return prompt