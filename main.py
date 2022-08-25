from app import app

if __name__ == "__main__":
    website_url = 'lovewithme.net'
    app.config['SERVER_NAME'] = website_url
    app.run(port=5001)
