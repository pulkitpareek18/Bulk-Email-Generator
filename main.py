
# importing the module
import csv
from email.mime.text import MIMEText
import os
from email.message import EmailMessage
# open the file in read mode
filename = open('emails.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
names = []
emails = []
colleges = []
 
# iterating over each row and append values to empty list
for col in file:
    names.append(col['director'])
    emails.append(col['email'])
    colleges.append(col['college'])


for name, college, email in zip(names, colleges, emails):
    

    email_body = f"""
    to: "{email}"
    subject: "Request for admission at {college}"
    
    
    <p><span style="font-size:medium"><span style="color:#222222"><span style="font-family:&quot;Google Sans&quot;,Roboto,RobotoDraft,Helvetica,Arial,sans-serif"><span style="background-color:#ffffff"><span style="font-size:0.875rem">Respected&nbsp;<span style="color:#000000"><span style="font-family:arial,sans-serif">{name}</span></span>,</span></span></span></span></span></p>

<p><br />
<span style="font-size:medium"><span style="color:#222222"><span style="font-family:&quot;Google Sans&quot;,Roboto,RobotoDraft,Helvetica,Arial,sans-serif"><span style="background-color:#ffffff"><span style="font-size:0.875rem">Greetings from Pulkit Pareek. I am writing to express my interest in pursuing a software engineering degree at {college}, one of the most prestigious institutions of higher education in India.<br />
<br />
I have always been fascinated by computers and programming since my childhood. I have learned various programming languages such as JAVA, PHP, PYTHON and JAVASCRIPT through free online courses and self-study. I have also developed some projects using my skills and creativity, which I would like to share with you.<br />
<br />
My first project was a tribute website for my chemistry teacher, which I presented to him on his birthday. It was a simple HTML/CSS/JS website that showcased his achievements, photos and testimonials from his students.&nbsp;<br />
<br />
My second project was a free online course website that integrated with YouTube APIs. It allowed users to import online courses from YouTube as well as upload their own courses manually. You can explore it here:&nbsp;<em><strong><a href="https://iblog.rf.gd/" style="color:#1155cc" target="_blank">https://iblog.rf.gd</a></strong></em></span></span></span></span></span></p>

<p><br />
<span style="font-size:medium"><span style="color:#222222"><span style="font-family:&quot;Google Sans&quot;,Roboto,RobotoDraft,Helvetica,Arial,sans-serif"><span style="background-color:#ffffff"><span style="font-size:0.875rem">My third project was a free OTT and movies platform that used web scraping APIs to provide the content for free. I created this project on request of my friends who wanted to watch movies and shows without paying any subscription fees. You can access it here:&nbsp;<a href="https://netflix-1uh.pages.dev/" style="color:#1155cc" target="_blank"><em><strong>https://netflix-1uh.pages.dev</strong></em></a></span></span></span></span></span></p>

<p><br />
<span style="font-size:medium"><span style="color:#222222"><span style="font-family:&quot;Google Sans&quot;,Roboto,RobotoDraft,Helvetica,Arial,sans-serif"><span style="background-color:#ffffff"><span style="font-size:0.875rem">My fourth project was a YouTube video and playlist downloader that used multithreading to speed up the downloading process. It allowed users to download videos and playlists in full quality and save them on their devices. You can explore it here:<em><strong>&nbsp;<a href="https://github.com/pulkitpareek18/Youtube-Video-and-Playlist-Downloader-FullQuality-MultiThreading" style="color:#1155cc" target="_blank">https://github.com/pulkitpareek18/Youtube-Video-and-Playlist-Downloader-FullQuality-MultiThreading</a></strong></em><br />
<br />
These are some of the projects that I have done so far and I am working on more. I hope that these projects will demonstrate my potential and interest in software engineering.<br />
<br />
However, I have a problem that is preventing me from applying to IIT. I have recently appeared for the JEE examination on 15th April 2023, but I am not very confident about my marks.&nbsp;<br />
<br />
I understand that IIT has a high standard of academic excellence and merit-based admission process, but I request you to kindly consider my application based on my projects rather than my marks. I believe that my projects reflect my passion, creativity and aptitude for software engineering more than my marks do.<br />
<br />
I assure you that if given a chance to study at IIT, I will work hard and excel in my studies. I will also contribute to the research and innovation activities of the institute and make you proud.</span></span></span></span></span></p>

<p>&nbsp;</p>

<p><span style="font-size:medium"><span style="color:#222222"><span style="font-family:&quot;Google Sans&quot;,Roboto,RobotoDraft,Helvetica,Arial,sans-serif"><span style="background-color:#ffffff"><span style="font-size:0.875rem">I&#39;ll be waiting for a reply from your side.<br />
<br />
Thank you for your time and attention.<br />
<br />
Sincerely,<br />
Pulkit Pareek</span></span></span></span></span></p>

<p>&nbsp;</p>
"""

    with open(os.path.join(os.getcwd(), "drafts" ,f"{college}.html"), 'w') as f:
        f.write(email_body)
        



 
