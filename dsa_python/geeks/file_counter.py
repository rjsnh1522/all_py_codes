import os

not_incldue_path =['./.git', './.idea', './interview/vimeo_hacker_earth/viemo_front_end',]

def fileCount(folder):
    count = 0
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        if os.path.isfile(path):
            count += 1
        elif os.path.isdir(path):
            not_in = True
            for i in not_incldue_path:
                if path in i:
                    not_in = False
                    break
            if not_in:
                print(path)
                count += fileCount(path)

    return count

print(fileCount('.'))
