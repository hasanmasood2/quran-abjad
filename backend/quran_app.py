from flask import Flask
import pyquran as pq
from pyquran import quran as q

app = Flask(__name__)

@app.route('/surahs')
def get_surahs():
    return {'surah_names': q.get_sura_name(sura_number=None)}

@app.route('/surah_body/<surah_number>')
def get_surah(surah_number):
    assert 1 <= int(surah_number) <= 114
    return {
        'surah_name': q.get_sura_name(sura_number=int(surah_number)),
        'surah_body': q.get_sura(int(surah_number), with_tashkeel=True, basmalah=True)
    }
