import numpy as np
import pandas as pd
import torch
from transformers import BartForConditionalGeneration, PreTrainedTokenizerFast

TOKENIZER = PreTrainedTokenizerFast.from_pretrained(
    'gogamza/kobart-summarization'
)
MODEL = BartForConditionalGeneration.from_pretrained(
    'gogamza/kobart-summarization'
)
MODEL.eval()


def abstractive_summarizer(text):
    # tokenize text for preprocessing
    raw_input_ids = TOKENIZER.encode(text)
    input_ids = (
        [TOKENIZER.bos_token_id] + raw_input_ids + [TOKENIZER.eos_token_id]
    )

    # generate summary using KoBART
    summary_ids = MODEL.generate(
        torch.tensor([input_ids]),
        max_length=256,
        early_stopping=True,
        repetition_penalty=2.0,
    )
    summ = TOKENIZER.decode(
        summary_ids.squeeze().tolist(), skip_special_tokens=True
    )
    return summ


if __name__ == '__main__':

    text = '''
    솔라나 지갑 팬텀, 모바일 앱 내일 출시
    코인데스크에 따르면, 솔라나 지갑 팬텀(Phantom)이 30일 iOS 베타 버전을 출시하고, 한달 안에 전체 버전을 출시할 예정이다. 모바일 지갑은 암호화폐와 NFT 거래, 전송, 스왑, 스테이킹 등을 지원한다. 팬텀 지갑은 11월 100만 명의 활성 사용자를 유치, 모바일 버전 없이 솔플레어(SolFlare) 지갑 사용자 수를 제친 바 있다.
    '''

    print("요약문:")
    print(abstractive_summarizer(text))
