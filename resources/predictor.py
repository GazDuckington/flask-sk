from nltk.tokenize import sent_tokenize
from resources.sentiment import predict_nbc
from resources.processing import freqs, normalisasi
from database.query import readLogprior, readLoglikelihood

logprior = readLogprior()
loglikelihood = readLoglikelihood()

tr = 0

def predTotal(text):
    x = predict_nbc(text, logprior, loglikelihood)
    return round(x, 4)

def Convert(tup, di):
    for i, (a, b) in enumerate(tup):
        di[i] = {'text': a, 'freq': b}
    return di

def perKalimat(text):
    kalimat = []
    x = sent_tokenize(text)

    for i in range(len(x)):
        sk = predict_nbc(x[i], logprior, loglikelihood)
        lb = '1' if sk > tr else '0'

        kalimat.append({
            'kalimat':x[i],
            'skor': round(sk, 4),
            'label': lb,
            'perkata': perKata(x[i])
        })

    return kalimat

def perKata(text):
    temp_norm = normalisasi(text)
    frekwensi = freqs(temp_norm)

    kata = []
    dicti = {}
    kamus_freq = Convert(frekwensi, dicti)

    for x,y in kamus_freq.items():
        sk = predict_nbc(y['text'], logprior, loglikelihood)
        lb = '1' if sk > tr else '0'

        kata.append({
            'kata': normalisasi(y['text'])[0],
            'skor': round(sk, 4),
            'label': lb,
            'freq': y['freq']
        })

    return kata