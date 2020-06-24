from github import Github
import smtplib
import email


token = "95060e0c31804e260be221fedd31103dd0b83b08"
user_name = "jfrance00"
g = Github(token)
user = g.get_user()
path = "C:/Users/Julie/Desktop/di/week10/day3/"


repo_name = "test"
repo = user.create_repo(repo_name)

commit_message = "testing using Git with Python"
content = "this is a bunch of sample content for a new file in a new repo. I couldn't figure out how to add the current daily challenge using pyGithub"


repo.create_file("test.py", commit_message, content, branch="test")


#--------sending email----------------

sender = 'france_soccer00@hotmail.com'
sender_name = "Julie"
receiver = 'eyal.work@chocron.eu'
receiver_name = "Eyal"
message = f'This is my daily challenge email. See my daily challenge here: github.com/{user_name}/{repo_name}'

s = smtplib.SMTP("smtp.live.com",587)
s.ehlo()  # Hostname to send for this command defaults to the fully qualified domain name of the local host.
s.starttls() #Puts connection to SMTP server in TLS mode
s.ehlo()
s.login(sender, '*******')

parts = ("From: " + sender,
         "To: " + receiver,
         "Subject: " + "daily challenge",
         "",
         message
         )
msg ='\r\n'.join(parts)

s.sendmail(sender, receiver, msg)

print("Successfully sent email")

s.quit()


