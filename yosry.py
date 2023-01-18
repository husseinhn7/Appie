from pytube import YouTube


a = YouTube("https://www.youtube.com/watch?v=wnqPqV6DdFQ")

# print(a.captions.get_by_language_code('en'))
# print(a.captions['en'].download(title="fid"))

a.captions['en'].download(title="g")
