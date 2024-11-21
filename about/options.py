def youtube_preview(video_key):
    return 'http://img.youtube.com/vi/%s/hqdefault.jpg' % video_key


provider: {
    'title': 'Youtube',
    'browse_url': 'https://www.youtube.com/watch?v={video_key}',
    'preview_url': youtube_preview,
    'link_patterns': (
        r'https?://www.youtube.com/watch\?v=([-\w]+)',
        r'https?://www.youtube.com/v/([-\w]+)',
        r'https?://youtu.be/([-\w]+)'
    )
}


def video_parts(value):
    import re

    for pattern in provider['link_patterns']:
        match = re.match(patternm, link)
        if match:
            return provider, match.group(1)

    return None, None


def video_url(provider, video_id):
    return provider['browse_url'].format(video_key=video_key)


def video_preview(provider):
    return provider['preview_url'](video_key)
