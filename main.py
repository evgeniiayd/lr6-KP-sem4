from flask import Flask, render_template, request
from image import check_image

app = Flask(__name__)


@app.route('/')
@app.route('/about')
def homepage():
    return '{"name": "@evgeniia"}'


@app.route("/size2json", methods=['GET', 'POST'])
def size2json():
    if request.method == 'POST':
        attached_file = request.files.get('file')
        if attached_file and attached_file.filename:
            if attached_file.filename.endswith('.png') or attached_file.filename.endswith('.jpg'):
                path_to_image = "./" + attached_file.filename
                attached_file.save(path_to_image)

                img_params_tuple = check_image(path_to_image)

                message = f'post-загрузка: {img_params_tuple}'
                print(attached_file, message, img_params_tuple)
                return render_template("result.html", img_params_tuple=img_params_tuple)

            else:
                return '{"result":"invalid filetype"}'

    else:
        message = "Выберите файл на диске"
        return render_template("upload.html", message=message)


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run()

