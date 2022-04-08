import Flask
from Flask import request,flash
import exactframe

app=Flask(__name__)
 
# You can do this for extra security. MAX_CONTENT_LENGTH lets you set how big files can be. 
# UPLOAD_EXTENSIONS lets you limit what types of files can be uploaded. 
app.config['MAX_CONTENT_LENGTH'] = 2 * 1080* 1080
app.config['UPLOAD_EXTENSIONS'] = ['.mov', '.mp4', '.m4v', '.jpm', '.jp2', '.3gp', '.3g2', '.mkv', '.mpg', '.ogv',
                                   '.webm', '.wmv']

@app.route('/model',methods=['Post'])
def predict():
    if request.method == 'Post'
      vid=request.files['video']
    # The files are in an immutable multi-dictionary, so loop through to grab them all. 
    for item in vid:
        uploaded_file = my_files.get(item)

# Check if the file name was left blank or isn't in the extensions list. 
        if uploaded_file.filename != '':
            file_ext = os.path.splitext(uploaded_file.filename)[1]
        else:
            flash('Please upload a video')
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400) 
        else:
            flash('Please upload either one of these file types(['.mov', '.mp4', '.m4v', '.jpm', '.jp2', '.3gp', '.3g2',                                                                      '.mkv', '.mpg', '.ogv','.webm', '.wmv']')
        uploaded_file.filename=filename
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_image filename: ' + filename)
		flash('Image successfully uploaded and displayed below')
        for frame in os.listdir(exactframe(uploaded_file))
            if  model.predict(frame)==request.form[objectname]:
               display_image(frame)
         else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
   return render_template{'index.html'}
  
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__=="__main__":
   app.run(debug=True)