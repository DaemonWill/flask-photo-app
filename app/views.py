from flask import render_template, request, redirect, flash, url_for, send_from_directory
from app import app
import os

@app.route('/tmp/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route("/", methods=["GET","POST"])
@app.route("/uploader", methods=["GET","POST"])
def uploader():
    if request.method == "POST":
        try:
            #request object must contain a file to upload
            if "file" not in request.files:
                flash("No file was provided")
                return redirect(request.url)
            #the received file must exist and be valid, let 'photo' = file to upload
            photo = request.files["file"]
            if photo and not photo.filename:
                flash("Filename does not exist")
                return redirect(request.url)
            if photo and allow_file(photo.filename):
                #ensure file name isn't malicious
                filename = secure_filename(photo.filename)
                #add photo to temporary bucket for viewing
                photo.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                return redirect(url_for("uploaded_file",
                                        filename = filename))
        #display error information upon unsuccessful processing
        except Exception as e:
            render_template("500.html",
                            error = str(e),
                            title = "Server Error")
    return render_template("index.html",
                            title = "Photo Uploader")
