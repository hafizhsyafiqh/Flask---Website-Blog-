from flask import Flask, render_template
app = Flask(__name__)

konten = [
    {
        'penulis': 'Hafizh Syafiqh',
        'judul': 'Postingan Pertama',
        'sinopsis': 'Ini adalah postingan pertama',
        'isi': 'Ini adalah isi dari postingan pertama',
        'tanggal': '28 januari 2023',
        'jam': '12.00'
    },
    {
        'penulis': 'BelajarPython',
        'judul': 'Belajar Flask',
        'sinopsis': 'Ini adalah belajar flask',
        'isi': 'Ini adalah isi dari belajar flask',
        'tanggal': '14 Februari 2023',
        'jam': '18.00'
    }
]

@app.route('/')
def home():
    return render_template('home.html', konten=konten, judul='Beranda')

@app.route('/tentang/')
def tentang():
    return render_template('tentang.html', judul='Tentang')

if __name__ == '__main__':
    app.run(debug=True)
