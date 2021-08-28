from flask import Flask
import pyquran as pq
from pyquran import quran as q
import abjad_map
app = Flask(__name__)

@app.route('/surah_names')
def get_surah_names():
    surah_names = q.get_sura_name(sura_number=None)
    return {
        'data': [{
            'surah_name': surah_name,
            'abjad_score': abjad_map.get_abjad_score(surah_name),
            'number_of_verses': len(q.get_sura(surah_number, basmalah=True))
            } for surah_number, surah_name in enumerate(surah_names)]
    }

@app.route('/surah_body/<surah_number>')
def get_surah(surah_number):
    assert 1 <= int(surah_number) <= 114
    return {
        'surah_name': q.get_sura_name(sura_number=int(surah_number)),
        'surah_body': q.get_sura(int(surah_number), with_tashkeel=True, basmalah=True)
    }
