from summarizer import Summarizer
from transformers import BertModel, BertTokenizer

tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
model = BertModel.from_pretrained(
    "bert-base-multilingual-cased", output_hidden_states=True
)
ext_sum_model = Summarizer(custom_model=model, custom_tokenizer=tokenizer)


def extractive_summarizer(text):
    return ext_sum_model(text, num_sentences=3)


if __name__ == '__main__':
    body = '''
        2020년 12월 5일, 스위스 융프라우에서는 1912년 융프라우철도 개통에 못지않은 새로운 역사가 시작되었다. 바로 ‘아이거 익스프레스Eiger Express’ 고속곤돌라가 개통한 것이다. 융프라우철도Jungfraubahn가 5,800억 원을 투입해 3년여 준비 끝에 완공한 이 고속곤돌라는 그린델발트Grindelwald 터미널(943m)과 아이거글레처Eigergletscher(2,320m)를 잇는 고도차 1,377m, 거리 6.5km의 케이블웨이Cableway다.

        26명이 탈 수 있는 초대형 곤돌라 캐빈Cabin(탑승공간)은 전체가 열선이 깔린 통유리창이어서 주변 경관을 막힘없이 감상할 수 있다. 시속 100km 강풍도 견딜 수 있을 뿐만 아니라 40초의 짧은 운행 간격, 난방 좌석, 무료 WI-FI 서비스로 탑승객의 안락함과 편의성을 극대화했다. 무엇보다 만족스러운 것은 이동 속도이다. 아이거 익스프레스는 유럽에서 최초로 8m/s(시속 28.8km)의 속도를 구현해 그린델발트 터미널~아이거글레처의 6.5km 거리를 단 15분 만에 주파한다.

        기존에는 그린델발트 철도역에서 베르너오버란트 철도BOB를 타고 클라이네샤이데크까지 가서 다시 융프라우 철도JB로 갈아타 융프라우요흐까지 가면 1시간 27분이 걸렸다. 이제 아이거 익스프레스를 이용하면 그린델발트역에서 아이거 글레처역까지 15분이 걸리고, 다시 철도를 타고 융프라우요흐까지 25분이 걸려 단 40분 만에 도착할 수 있게 되었다. 이는 기존 대비 편도 47분(그린델발트 터미널 이용 시 43분), 왕복 94분이나 이동시간을 단축시킨 것이다. ‘융프라우 철도에 이은 새로운 역사를 만들었다’는 말이 괜히 나온 것이 아니다.아이거 익스프레스의 속도와 안정성의 비결은 세 개의 연결 로프에 있다. 3Sdrei-seil, tri-cable 케이블 공법은 기존 케이블카와 ‘푸니쿨라(열차형 케이블카)’의 장점을 모두 갖춘 가장 최첨단 시스템으로 평가받는다. 6.5km 구간에 지구가 단 7개에 불과해 건설비용은 4~5배 더 들지만 환경과 경관을 보존할 수 있는 친환경적 장점이 있다. 개통 전 자체 수력 발전소를 운영할 만큼 자연 그대로의 원료 수급과 환경 보호를 주요 가치로 삼은 융프라우 철도의 기업 철학에 따라 아이거 익스프레스는 엄격한 스위스 환경정책을 통과하고, 연방정부와 주민들의 승인을 통과하기까지 장장 5년이란 시간이 걸렸다.

        코로나19 팬데믹 상황이 한참이던 2020년 12월 개통했으나 1년 동안 200만 명이 넘는 여행객이 아이거 익스프레스를 이용했다. 뿐만 아니다. 탑승장인 그린델발트 터미널은 스위스에서 가장 명예로운 모빌리티 어워즈 중 하나인 ‘FLUX-Golden Transport Hub’에서 특별상을 수상했다.

        '''

    print(extractive_summarizer(body, model, tokenizer))
