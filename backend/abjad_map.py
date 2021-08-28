import pyquran as pq
from pyquran import quran as q

ABJAD_MAP = {
    ' ': 0, # Empty space worth zero
    pq.alef: 1,
    pq.alef_hamza_above: 1,
    pq.alef_hamza_below: 1,
    pq.alef_mad: 1,
    pq.hamza: 1,
    pq.beh: 2,
    pq.jeem: 3,
    pq.dal: 4,
    pq.heh: 5,
    pq.waw: 6,
    pq.waw_hamza: 6,
    pq.zain: 7,
    pq.hah: 8,
    pq.tah: 9,
    pq.yeh: 10,
    pq.yeh_hamza: 10,
    pq.alef_maksura: 10,
    pq.kaf: 20,
    pq.lam: 30,
    pq.meem: 40,
    pq.noon: 50,
    pq.seen: 60,
    pq.ain: 70,
    pq.feh: 80,
    pq.sad: 90,
    pq.qaf: 100,
    pq.reh: 200,
    pq.sheen: 300,
    pq.teh: 400,
    pq.teh_marbuta: 400,
    pq.theh: 500,
    pq.khah: 600,
    pq.thal: 700,
    pq.dad: 800,
    pq.zah: 900,
    pq.ghain: 1000
}


def get_abjad_score(list_of_characters):
    '''
    Takes a list of arabic characters
    Returns the abjad value based on ABJAD_MAP
    ABJAD_MAP is stored in abjad_map.py
    '''
    abjad_score = 0
    for character in list_of_characters:
        try:
            abjad_score += ABJAD_MAP[character]
        except KeyError:
            print('Error was encountered on mapping ' + character)
    return abjad_score
