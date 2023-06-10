import re

def extname(fname):
    m = re.search(r'\.(\w+)$', fname.lower())
    return m.group(1) if m else ''


ext_is_html = lambda name: \
    extname(name) in ['html', 'htm', 'xhtml']
    

def ext_is_c_style_code(fname):
    return extname(fname) in [
        'c', 'cpp', 'cxx', 'h', 'hpp',
        'java', 'kt', 'scala', 
        'cs', 'js', 'json', 'ts', 
        'php', 'go', 'rust', 'swift',
    ]

def ext_is_pic(fname):
    return extname(fname) in [
        'jpg', 'jpeg', 'jfif', 'png', 
        'gif', 'tiff', 'webp'
    ]
    
def ext_is_video(fname):
    return extname(fname) in [
        'mp4', 'm4v', '3gp', 'mpg', 'flv', 'f4v', 
        'swf', 'avi', 'gif', 'wmv', 'rmvb', 'mov', 
        'mts', 'm2t', 'webm', 'ogg', 'mkv', 
    ]

def ext_is_audio(fname):
    return extname(fname) in [
        'mp3', 'aac', 'ape', 'flac', 'wav', 'wma', 'amr', 'mid', 'm4a',
    ]

def ext_is_video_or_audio(fname):
    return ext_is_video(fname) or ext_is_audio(fname)
