from flask import render_template, request, redirect
from app import app
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])
UPLOAD_FOLDER = "./app/static/images"

def allow_file(filename):
    return "." in filename and \
            filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET","POST"])
@app.route("/uploader", methods=["GET","POST"])
def uploader():
    if request.method == "POST":
        try:
            #request object must contain a file to upload
            if "file" not in request.files:
                raise FileNotFoundError("No file was provided")
            #the received file must exist and be valid, let 'photo' = file to upload
            photo = request.files["file"]
            if photo and not photo.filename:
                raise FileNotFoundError("Filename does not exist")
            if photo and allow_file(photo.filename):
                #ensure file name isn't malicious
                filename = secure_filename(photo.filename)
                #add photo to temporary bucket for viewing
                photo.save(os.path.join(UPLOAD_FOLDER, filename))
                return redirect("static/images" + "/" + filename)
            raise ValueError("filename not allowed")
        #display error information upon unsuccessful processing
        except Exception as e:
            return render_template("error.html",
                            error = str(e),
                            title = "Server Error")
    else:
        return render_template("index.html",
                                title = "Photo Uploader")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html",
                    error = str(e),
                    title = "Resource Not Found")
