import numpy as np

from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

from transformers import *

MODEL = SentenceTransformer(
    'sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens'
)


def mmr(doc_embedding, candidate_embeddings, words, top_n, diversity):
    word_doc_similarity = cosine_similarity(candidate_embeddings, doc_embedding)
    word_similarity = cosine_similarity(candidate_embeddings)
    keywords_idx = [np.argmax(word_doc_similarity)]
    candidates_idx = [i for i in range(len(words)) if i != keywords_idx[0]]
    for _ in range(top_n - 1):
        candidate_similarities = word_doc_similarity[candidates_idx, :]
        target_similarities = np.max(
            word_similarity[candidates_idx][:, keywords_idx], axis=1
        )

        # MMR을 계산
        mmr = (
            1 - diversity
        ) * candidate_similarities - diversity * target_similarities.reshape(
            -1, 1
        )
        mmr_idx = candidates_idx[np.argmax(mmr)]

        keywords_idx.append(mmr_idx)
        candidates_idx.remove(mmr_idx)

    return [words[idx] for idx in keywords_idx]


def keyword_extraction(text):
    okt = Okt()
    tokenized_doc = okt.pos(text)
    tokenized_nouns = ' '.join(
        [word[0] for word in tokenized_doc if word[1] == 'Noun']
    )
    n_gram_range = (1, 2)
    try:
        count = CountVectorizer(ngram_range=n_gram_range).fit([tokenized_nouns])
    except ValueError as exc:
        print(exc)
    candidates = count.get_feature_names()
    doc_embedding = MODEL.encode([text])
    candidate_embeddings = MODEL.encode(candidates)
    top_n = 5
    # add more diversity to keywords
    keywords = mmr(
        doc_embedding, candidate_embeddings, candidates, top_n=5, diversity=0.7
    )
    return keywords
