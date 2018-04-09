import os, sys, re
from glob import glob

def change(before , after):
    print ('name  before: "%s" and after: "%s"' % (before, after))
    os.rename(before, after) #renaming

baza =  '''C:\\USers\\HP\\Desktop\\24 Season 8 -----   insert path-----'''

video_files = sorted(glob(os.path.join(baza, '*.mkv'))) ''' ----- .avi, .mp4, etc. ----- '''
sub_files = sorted(glob(os.path.join(baza, '*.srt')))


for videofile, subfiles in zip(video_files, sub_files):
    new_subfile = re.sub(r'\.mkv', '.srt', videofile)
    if subfiles == new_subfile:
        print('%s OK' % (subfiles,))
        continue


    change(subfiles, new_subfile)