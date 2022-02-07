import itertools

import numpy as np
from konlpy.tag import Okt
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# from transformers import *

MODEL = SentenceTransformer(
    'sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens'
)


def keyword_extraction(text):
    okt = Okt()
    tokenized_doc = okt.pos(text)
    tokenized_nouns = ' '.join(
        [word[0] for word in tokenized_doc if word[1] == 'Noun']
    )

    n_gram_range = (2, 3)
    try:
        count = CountVectorizer(ngram_range=n_gram_range).fit([tokenized_nouns])
        candidates = count.get_feature_names()

        doc_embedding = MODEL.encode([text])
        candidate_embeddings = MODEL.encode(candidates)

        top_n = 5
        distances = cosine_similarity(doc_embedding, candidate_embeddings)
        keywords = [candidates[index] for index in distances.argsort()[0][-top_n:]]
    except ValueError:
        return None
    return keywords


if __name__ == '__main__':
    doc = """
    국내 유가증권시장(코스피)이 이달에만 벌써 6%대 하락했지만 전문가들은 악재가 이어질 경우 추가적인 지수 밴드의 하락을 점치고 있다. 증시 추가 하락의 '트리거'로 작용할 요소는 오는 2월 발표될 미국의 1월 고용 등 경제지표가 손꼽힌다. 글로벌 경기 회복세가 둔화되는 모습이 관찰될 경우 기업 실적 부진 우려로 이어져 증시에 악재가 될 것이란 분석이다.
    24일 한국거래소에 따르면 코스피는 1.49% 하락한 2792.00에 마감했다. 이달에만 6.23% 떨어진 수치다. 24일엔 기관이 순매수에 나섰지만 이 기간 동안 지수를 끌어내린 건 기관투자자들이다. 이달 초부터 24일까지 기관투자자들은 코스피에서 4조7570억원을 순매도했다. 외국인투자자들은 지난 13일까진 누적 3조원가량을 순매수했지만 중순부터 약 1조3500억원을 팔아치우고 있다.

    기관과 외국인 투자자들의 투자심리가 악화된 건 국내 증시를 둘러싼 대외 환경이 긍정적이지 않기 때문이다. 특히 증권가에선 25일로 예정된 미국 연방준비제도(Fed)의 연방공개시장위원회(FOMC)에서 나올 메시지와 더불어 경제지표를 확인해야 한다고 강조한다. FOMC 정례 회의는 이미 시장에 알려진 이벤트로 시장 컨센서스(예상치)가 확립된 분야다. 오히려 불확실성 해소가 호재로 작용될 여지도 있다.
    하지만 오는 2월 발표될 미국의 1월 비농업 일자리, 실업률, 경제활동참가율, 시간당 평균 임금 등 경제지표에서 글로벌 경기 회복세가 둔화되는 점이 확인된다면 세계 증시에 추가적인 악재로 작용될 수 있다. 그 전조 현상은 지난주 미국 노동부가 발표한 1월 9~15일(현지시간) 신규 실업수당 청구건수에서 확인됐다.

    당시 노동부가 발표한 실업수당 청구건수는 28만6000건이다. 이는 전주보다 5만5000건 급증한 수치로 지난해 10월 둘째 주 이후 최다치다. 블룸버그가 집계한 전문가 전망치(22만5000건)도 크게 상회한 수치다. 물가가 상승하는 가운데 오미크론발 코로나19 확진자 수 증가세도 여전해 경기 회복 속도 둔화 우려가 증시에 부담이 될 수 있다는 지적이다.

    """
    print(keyword_extraction(doc))
