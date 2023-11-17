from pytube import YouTube

url = "https://www.youtube.com/watch?v=RsN0aXfPR1E"

cursor = YouTube(url)

info = cursor.streams.all()

better_info = list(enumerate(info))

for i in better_info:
    print(i)

user_input = int(input(""))

info[user_input].download()
print("done")