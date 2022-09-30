
from flask import Flask, jsonify, request, render_template,session  
from pytube import YouTube

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def home():
    if request.method == "POST":
        #session
        session["link"] = request.form.get('url')
        # check if the link is valid or not
        try :
            url = YouTube(session['link'])
            #using pytube inbuild session
            url.check_availability()
        except:
            return render_template('error.html')

        return render_template('download.html',url=url)
    return render_template('home.html')


@app.route("/", methods = ['GET','POST'])
def download_video():
    pass

if __name__=='__main__':
    app.run(debug=True, port=5005)

