from flask import Flask, render_template, request
import qrcode
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generar', methods=['POST'])
#def generar-img():
#    url = request.form.get('url')
#    qr = qrcode.QRCode(version=1, box_size=10, border=5)
#    qr.add_data(url)
#    qr.make(fit=True)
#    img = qr.make_image(fill_color="black", back_color="white")
#    img.save("qr.png")
#    return render_template('index.html', url=url)

def generar():
    memory = BytesIO()
    data = request.form.get('url')
    img = qrcode.make(data)
    img.save(memory)
    memory.seek(0)
    
    base64_img = "data:image/png;base64," + b64encode(memory.getvalue()).decode('ascii')

    return render_template('index.html', data=base64_img)

if __name__ == '__main__':  #para iniciar el servidor python main.py en terminal
    app.run(debug=True)
    
    