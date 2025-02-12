def listdir_matches(match):
    import os
    last_slash = match.rfind('/')
    if last_slash == -1:
        dirname = '.'
        match_prefix = match
        result_prefix = ''
    else:
        match_prefix = match[last_slash + 1:]
        if last_slash == 0:
            dirname = '/'
            result_prefix = '/'
        else:
            dirname = match[0:last_slash]
            result_prefix = dirname + '/'
    def add_suffix_if_dir(filename):
        try:
            if (os.stat(filename)[0] & 0x4000) != 0:
                return filename + '/'
        except FileNotFoundError:
            pass
        return filename
    if os.stat(dirname)[0] & 0x4000 == 0:
        return []
    matches = [add_suffix_if_dir(result_prefix + filename)
               for filename in os.listdir(dirname) if filename.startswith(match_prefix)]
    return matches
output = listdir_matches('/ma')
if output is None:
    print("None")
else:
    print(output)
