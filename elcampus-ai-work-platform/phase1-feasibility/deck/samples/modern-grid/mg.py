# Modern Grid 샘플: 현재 덱 02(summary)·21(pnl)·34(decision)를 같은 내용으로 다시 디자인
# 1280×720 디자인 시스템 수치를 1920×1080에 맞게 1.5배로 환산
import re, json, os
OUT = os.path.dirname(os.path.abspath(__file__)) + '/project'
SRC = '/tmp/claude-0/-home-claude/c565d7d3-335e-5114-b22b-a52fd328de4c/scratchpad/deck2/project'

BG, SURF, SURF2, FOOTER, LINE, LINE2 = '#242424', '#303030', '#3a3a3a', '#3b3b3b', '#4a4a4a', '#5e5e5e'
INK, INK2, INK3 = '#ffffff', '#c8c8c8', '#a3a3a3'
G, G6, G8, GP, Y = '#84bd26', '#66901e', '#426012', '#3a4a1c', '#f0ae24'
R = "'Spoqa Han Sans Neo', 'Noto Sans KR', sans-serif"
B = "'Spoqa Han Sans Neo Bold', 'Spoqa Han Sans Neo', 'Noto Sans KR', sans-serif"
NUM = "'Inter Tight', 'Spoqa Han Sans Neo Bold', sans-serif"
HATCH = f'repeating-linear-gradient(-45deg,{LINE2} 0px,{LINE2} 1.5px,transparent 1.5px,transparent 9px)'

def p(t, size, font=R, color=INK, extra=''):
    lh = 1.3 if size >= 30 else 1.55
    return f'<p style="font-family:{font};font-weight:400;font-size:{size}px;line-height:{lh};color:{color};{extra}">{t}</p>'

def num(t, color=G):
    return f'<span style="font-family:{NUM};font-weight:700;color:{color}">{t}</span>'

def src(n):
    return f'<span style="color:{INK3}">[{n}]</span>'

def eyebrow(t):
    return (f'<div style="display:flex;flex-direction:column;gap:9px">'
            f'<div style="width:36px;height:5px;background:repeating-linear-gradient(90deg,{G} 0px,{G} 6px,transparent 6px,transparent 10px)"></div>'
            + p(t, 18, B, G, 'letter-spacing:1px') + '</div>')

def foot_bar(no):
    return (f'<div style="position:absolute;left:0;right:0;bottom:0;height:66px;background:{FOOTER};display:flex;align-items:center;gap:18px;padding:0 90px">'
            + p(f'<span style="font-family:{NUM};font-weight:700;color:{INK}">{no}</span>', 18, R, INK3)
            + f'<div style="width:1px;height:20px;background:{LINE2}"></div>'
            + p('AI 업무 플랫폼 사업 타당성 검토 – 2026', 18, R, INK3) + '</div>')

def gloss(items):
    # items: [(term, desc)] 한 줄에 여러 개
    return '<div style="display:flex;flex-wrap:wrap;column-gap:28px;row-gap:2px">' + ''.join(
        p(f'<span style="font-family:{B};color:{INK2}">{t}</span>{d}', 16, R, INK3) for t, d in items) + '</div>'

def slide(sid, no, eb, title, body, foot):
    return (f'<section id="{sid}" data-transition="fade" style="background:{BG};color:{INK};font-family:{R};font-weight:400;'
            f'padding:72px 90px 96px;display:flex;flex-direction:column;gap:30px">'
            + eyebrow(eb)
            + f'<h2 style="font-family:{B};font-weight:400;font-size:46px;line-height:1.3;letter-spacing:-0.5px;color:{INK};max-width:1650px">{title}</h2>'
            + body
            + f'<div class="foot" style="margin-top:auto;display:flex;flex-direction:column;gap:2px">{foot}</div>'
            + foot_bar(no) + '</section>')

def card(label, text, extra=''):
    return (f'<div style="background:{SURF};padding:22px 28px 24px 34px;display:flex;flex-direction:column;gap:8px;position:relative;{extra}">'
            f'<div style="position:absolute;left:0;top:24px;width:6px;height:56px;background:{G}"></div>'
            + label + text + '</div>')

def callout(title, inner, extra=''):
    return (f'<div style="background:{GP};padding:30px 34px;display:flex;flex-direction:column;gap:18px;{extra}">'
            + p(title, 24, B, INK) + inner + '</div>')

def metric(label, value, sub=''):
    return (f'<div style="border-top:1px solid {LINE2};padding-top:14px;display:flex;flex-direction:column;gap:4px">'
            + p(label, 18, R, INK3)
            + f'<p style="font-family:{NUM};font-weight:500;font-size:46px;line-height:1.15;letter-spacing:-1px;color:{INK}">{value}</p>'
            + (p(sub, 17, R, INK3) if sub else '') + '</div>')

slides = {}

# ---------------- 02 summary: 판정 → 근거 → 경영진 결정 ----------------
KO = lambda t: f'<span style="font-family:{B};color:{G}">{t}</span>'
left = (f'<div style="width:430px;flex:none;display:flex;flex-direction:column;gap:22px">'
        + f'<div style="display:flex;align-items:center;gap:14px"><div style="width:36px;height:5px;background:repeating-linear-gradient(90deg,{G} 0px,{G} 6px,transparent 6px,transparent 10px)"></div>{p("종합 판정", 20, B, G)}</div>'
        + f'<p style="font-family:{B};font-weight:400;font-size:150px;line-height:1;letter-spacing:-4px;color:{G}">보류</p>'
        + p('안 된다는 결론이 아니라 진행 여부를 가를 핵심 근거가 아직 없다는 뜻', 20, R, INK2)
        + metric('투자 회수, 현금 기준(매달 3곳)', '3년 3개월', '4곳이면 2년 8개월')
        + metric('투자 회수, 사내 인력 포함', '7년 9개월', '4곳이면 5년 7개월')
        + '</div>')
ROWS = [('起', '개요', '엘캠퍼스가 30~100인 중소기업에 화이트 라벨 업무 플랫폼·독립 서버·AI 연동·교육을 묶어 월 구독으로 판매'),
        ('承', '구성·비용·가격', '개발자 4명과 UIX 2명이 시간의 절반씩 투입하면 출시까지 약 9개월. 출시 전 투자(CAPEX) 약 2억 8,000만 원, 그중 새 현금은 경력 PM 영입을 포함해 약 9,400만 원'),
        ('轉', '손익·위험', '매달 3곳은 아직 근거 없는 기준 가정(기존 채널 고객만). 전국 30~99인 약 4만 7,500곳은 지불 의향의 근거가 아님. 교육 갱신과 SaaS 혜택을 묶어 제안하면 환급과정이 위험해질 수 있어 분리 필요')]
mid = '<div style="flex:1;min-width:0;display:flex;flex-direction:column;gap:14px">' + ''.join(
    card(p(f'<span style="font-family:\'Noto Serif KR\', serif;font-weight:700;color:{G}">{h}</span>&nbsp;&nbsp;{k}', 20, B, INK), p(t, 20, R, INK2))
    for h, k, t in ROWS) + '</div>'
DEC = [('01', '시장 검증 승인', '개발 없이 기존 교육 고객에게 가격을 제시하고 LOI를 받는 검증'),
       ('02', '예산과 기간', '내부 시간 환산 약 2,150~2,280만 원(새 현금 0~300만 원, 선택 항목 포함 최대 약 2,580만 원), 2~3개월'),
       ('03', '판단 기준', '결과를 판정할 투자 한도와 허용 회수 기간, 사내 인력 기회비용 포함 여부')]
dec = '<div style="display:flex;flex-direction:column;gap:16px">' + ''.join(
    f'<div style="display:flex;gap:16px;align-items:flex-start;border-top:1px solid {G6};padding-top:14px">'
    f'<p style="font-family:{NUM};font-weight:700;font-size:26px;line-height:1.2;color:{G};flex:none;width:38px">{n}</p>'
    f'<div style="display:flex;flex-direction:column;gap:4px;flex:1;min-width:0">{p(t, 21, B, INK)}{p(d, 18, R, INK2)}</div></div>'
    for n, t, d in DEC) + '</div>'
right = callout('結 경영진이 이번에 결정할 세 가지', dec, 'width:500px;flex:none')
body = f'<div style="display:flex;gap:36px;align-items:stretch;flex:1;min-height:0">{left}{mid}{right}</div>'
foot = (p('<span style="font-family:' + B + ';color:' + INK2 + '">기본 조건</span>: ARPU 80만 원, 고객 1곳당 월 변동비 29만 원, 월 고정비 약 3,470만 원(그중 현금 약 1,410만 원), 해지율 매달 2%(추정). 사내 인력은 KOSA 2026 시장 인건비로 환산. 착수 후 = 개발 9개월 + 출시 후', 16, R, INK3)
        + gloss([('ARPU', '(Average Revenue Per User): 고객 1곳당 평균 월 매출'), ('CAPEX', '(Capital Expenditure): 출시 전 투자비'),
                 ('LOI', '(Letter of Intent): 구매의향서'), ('PM', '(Product Manager): 제품 책임자'), ('UIX', ': UI/UX 디자인'),
                 ('SaaS', '(Software as a Service): 인터넷으로 빌려 쓰는 소프트웨어'), ('KOSA', ': 한국소프트웨어산업협회(SW기술자 평균임금 발표)'),
                 ('화이트 라벨', ': 고객사 브랜드로 바꿔 제공하는 방식')]))
slides['summary'] = slide('summary', '02', '한눈에 보기',
    f'검토한 사업의 진행은 <span style="color:{G}">보류</span>, 월 75~90만 원(Pro)에 구독할 근거보다 반대 근거가 더 많음', body, foot)

# ---------------- 21 pnl: 전제 → 누적 손익 차트 → 핵심 숫자 ----------------
h = open(SRC + '/slides/pnl.html', encoding='utf8').read()
cash = re.search(r'aria-label="현금 기준.*?<polyline points="([^"]+)".*?<polyline points="([^"]+)"', h, re.S)
inh = re.search(r'aria-label="사내 인력 포함 기준.*?<polyline points="([^"]+)".*?<polyline points="([^"]+)"', h, re.S)
CASHC, INHC = '#c8c8c8', G
W, H = 720, 380   # 원본 좌표: y 95 = 10억, 285 = 0, x 80 = 1년
grid = ''.join(f'<line x1="0" x2="{W}" y1="{y}" y2="{y}" stroke="{LINE2 if y == 285 else LINE}" stroke-width="{2 if y == 285 else 1.2}"/>' for y in (0, 95, 190, 285, 380))
svg_grid = f'<svg aria-label="격자" width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position:absolute;left:96px;top:10px;width:{W}px;height:{H}px">{grid}<line x1="60" x2="60" y1="275" y2="295" stroke="{LINE2}" stroke-width="2"/></svg>'
def curve(label, m, c, cx):
    return (f'<svg aria-label="{label}" width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position:absolute;left:96px;top:10px;width:{W}px;height:{H}px">'
            f'<polyline points="{m.group(1)}" fill="none" stroke="{c}" stroke-width="4" stroke-linecap="round" stroke-dasharray="2 9"/>'
            f'<polyline points="{m.group(2)}" fill="none" stroke="{c}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>'
            f'<circle cx="{cx}" cy="285" r="9" fill="{c}" stroke="{BG}" stroke-width="3"/></svg>')
def at(x, y, t, size=18, font=R, color=INK3, extra=''):
    return f'<p style="position:absolute;left:{x}px;top:{y}px;font-family:{font};font-weight:400;font-size:{size}px;line-height:1.3;color:{color};white-space:nowrap;{extra}">{t}</p>'
ylab = ''.join(at(0, 10 + y - 13, t, 18, NUM, INK3, 'width:80px;text-align:right') for y, t in ((0, '+30억'), (95, '+20억'), (190, '+10억'), (285, '0'), (380, '−10억')))
xlab = ''.join(at(96 + 80 * i - 18, 404, f'{i}년', 18, R, INK3) for i in range(1, 10))
chart = (f'<div style="position:relative;width:830px;height:440px;flex:none">'
         + svg_grid + curve('현금 기준: 누적 손익이 착수 후 3년 3개월째 0을 넘는다', cash, CASHC, 260)
         + curve('사내 인력 포함 기준: 누적 적자가 최대 약 7.9억 원까지 커지고 착수 후 7년 9개월째 0을 넘는다', inh, INHC, 620)
         + ylab + xlab + at(0, 404, '착수 후', 18, B, INK2)
         + at(148, 262, '출시', 17) + at(282, 236, '회수 3년 3개월', 19, B, INK)
         + at(730, 310, '회수 7년 9개월', 19, B, G) + at(380, 336, '최대 −7.90억', 18, R, INK2)
         + '</div>')
legend = ('<div style="display:flex;gap:28px">'
          + ''.join(f'<div style="display:flex;align-items:center;gap:10px"><div style="width:26px;height:5px;background:{c}"></div>{p(t, 18, R, INK2)}</div>'
                    for c, t in ((INHC, '사내 인력 포함(시장 인건비)'), (CASHC, '현금'))) + p('점선: 개발 9개월(출시 전)', 18, R, INK3) + '</div>')
tab = f'<div style="display:flex;justify-content:space-between;align-items:center"><p style="font-family:{B};font-weight:400;font-size:18px;line-height:1.3;color:{INK};background:{SURF2};padding:10px 18px">매달 3곳, 착수 후 누적 손익</p></div>'
center = f'<div style="display:flex;flex-direction:column;gap:18px;flex:none;width:830px">{tab}{chart}{legend}</div>'
leftc = ('<div style="width:350px;flex:none;display:flex;flex-direction:column;gap:14px">'
         + card(p('전제(추정)', 20, B, INK), p('매달 신규 고객 3곳, 평균 구독료(ARPU) 80만 원, 해지율 매달 2%, 신규 고객은 기존 교육 고객 채널만', 19, R, INK2))
         + card(p('두 기준의 차이', 20, B, INK), p('사내 인력의 기회비용. 현금은 새로 나가는 돈만, 사내 인력 포함은 개발·디자인 시간을 시장 인건비로 환산', 19, R, INK2))
         + '</div>')
def krow(label, a, b2, last=False):
    bd = '' if last else f'border-bottom:1px solid {G6};'
    return (f'<div style="display:flex;flex-direction:column;gap:6px;padding:14px 0;{bd}">{p(label, 18, R, INK2)}'
            f'<div style="display:flex;gap:12px;align-items:baseline"><div style="flex:1"></div>'
            f'<p style="font-family:{NUM};font-weight:700;font-size:30px;line-height:1.2;color:{INK};width:150px;text-align:right">{a}</p>'
            f'<p style="font-family:{NUM};font-weight:500;font-size:30px;line-height:1.2;color:{INK2};width:150px;text-align:right">{b2}</p></div></div>')
khead = (f'<div style="display:flex;gap:12px;padding-bottom:8px;border-bottom:1px solid {G6}"><div style="flex:1"></div>'
         + p('사내 인력 포함', 17, B, G, 'width:150px;text-align:right') + p('현금', 17, B, INK2, 'width:150px;text-align:right') + '</div>')
kinner = ('<div style="display:flex;flex-direction:column">' + khead
          + krow('투자 회수(착수 후)', '7년 9개월', '3년 3개월')
          + krow('최대 누적 적자', '−7.90억', '−1.75억')
          + krow('5년차 연간 손익(출시 후)', '+1.72억', '+4.20억', True) + '</div>')
rightc = callout('두 기준의 핵심 숫자(원)', kinner, 'flex:1;min-width:0')
body = f'<div style="display:flex;gap:36px;align-items:flex-start;flex:1;min-height:0">{leftc}{center}{rightc}</div>'
foot = (p(f'<span style="font-family:{B};color:{INK2}">상세 표</span>: Appendix A3 · 연도별 손익(출시 후 1~5년차 고객 수·매출·연간·누적 손익)', 16, R, INK3)
        + gloss([('사내 인력 포함', '(시장 인건비): 사내 개발·디자인 인력의 시간을 시장 인건비로 환산해 넣은 기준(경제적 타당성)'),
                 ('현금', ': 새로 나가는 돈만 넣은 기준(마련할 자금)'), ('ARPU', '(Average Revenue Per User): 고객 1곳당 평균 월 매출')]))
slides['pnl'] = slide('pnl', '21', '연도별 손익',
    f'현금 기준 <span style="color:{G}">3년 3개월</span>, 사내 인력 포함 <span style="color:{G}">7년 9개월</span>에 투자 회수(매달 신규 고객 3곳)', body, foot)

# ---------------- 34 decision: 세 기준 카드 → Stage-Gate 집행 ----------------
CR = [('01', '투자 한도', '운영비 3~6개월분의 현금을 남긴 뒤, 사업이 실패해 투자금을 모두 잃어도 본업에 지장이 없는 금액으로 정함(QuickBooks 2026)',
       '비교할 값: 최대 누적 적자(매달 3곳)', '현금 기준 약 1.75억 원<br>사내 인력 포함 약 7.90억 원'),
      ('02', '허용 회수 기간', '미국 CFO(최고재무책임자)의 56.7%가 회수 기간을 (거의) 항상 쓰고, 기준은 주로 2~4년(Graham·Harvey 2001, Dobbs)',
       '다만 일반 투자 관행이므로', '이 사업의 기준은<br>경영진이 직접 정함'),
      ('03', '사내 인력 기회비용의 포함 여부', '같은 조건에서도 판단에 사내 인력의 기회비용을 넣는지에 따라 회수 기간이 크게 달라짐',
       '착수 후 회수(매달 3곳)', '현금 기준 3년 3개월<br>사내 인력 포함 7년 9개월')]
cards = '<div style="display:flex;gap:30px;align-items:stretch">' + ''.join(
    f'<div style="flex:1;min-width:0;background:{SURF};padding:28px 30px 30px;display:flex;flex-direction:column;gap:14px;position:relative">'
    f'<div style="position:absolute;left:0;top:30px;width:6px;height:56px;background:{G}"></div>'
    f'<p style="font-family:{NUM};font-weight:700;font-size:44px;line-height:1;color:{G}">{n}</p>'
    + p(t, 28, B, INK) + p(d, 19, R, INK2)
    + f'<div style="margin-top:auto;border-top:1px solid {LINE2};padding-top:16px;display:flex;flex-direction:column;gap:6px">{p(cl, 17, R, INK3)}{p(cv, 22, B, INK)}</div>'
    + '</div>' for n, t, d, cl, cv in CR) + '</div>'
STEPS = ['시장 검증', '개발', '출시', '확장']
steps = '<div style="display:flex;flex:1;min-width:0">' + ''.join(
    f'<div style="flex:1;min-width:0;padding:14px 18px;display:flex;flex-direction:column;gap:10px;{"background:" + HATCH if i == 0 else ""}">'
    f'<div style="display:flex;align-items:center;gap:12px"><div style="width:18px;height:18px;transform:rotate(45deg);border:3px solid {G};flex:none;{"background:" + G if i == 0 else ""}"></div>'
    + ('' if i == len(STEPS) - 1 else f'<div style="flex:1;height:2px;background:{G6}"></div>') + '</div>'
    + p(s, 21, B, INK) + p('관문(Gate)에서 다음 투자 여부 판정' if i < len(STEPS) - 1 else '단계마다 숫자 기준으로 판정', 16, R, INK2) + '</div>'
    for i, s in enumerate(STEPS)) + '</div>'
exec_ = (f'<div style="background:{GP};padding:22px 30px;display:flex;gap:36px;align-items:center">'
         f'<div style="width:420px;flex:none;display:flex;flex-direction:column;gap:6px">{p("집행 방식", 24, B, INK)}{p("투자 한도는 한 번에 쓰지 않고 관문(Stage-Gate)마다 나눠 집행함", 19, R, INK2)}</div>'
         + steps + '</div>')
body = ('<div style="display:flex;flex-direction:column;gap:24px">'
        + p('투자 한도, 허용 회수 기간, 사내 인력 기회비용 포함 여부는 엘캠퍼스 경영진이 직접 정할 사항', 24, R, INK2, 'margin-top:-14px')
        + cards + exec_ + '</div>')
foot = (p(f'<span style="font-family:{B};color:{INK2}">근거</span>: Stage-Gate(Cooper 1990), Discovery-Driven Planning(McGrath·MacMillan 1995), 감당 가능한 손실(Sarasvathy 2006), 신사업 기대치·예산 분리 기업 조사(McKinsey 2021)', 16, R, INK3)
        + gloss([('Stage 1~3', ': 착수할 경우의 단계(1 기존 채널 파일럿, 2 신규 영업 확장, 3 전국 확대, 42장)'), ('빗금', ': 지금 결정할 단계')]))
slides['decision'] = slide('decision', '34', '결정 기준 권고',
    f'착수 판단 전에 <span style="color:{G}">결정 기준 세 가지</span>부터 정해야 함', body, foot)

os.makedirs(OUT + '/slides', exist_ok=True)
for k, v in slides.items():
    open(f'{OUT}/slides/{k}.html', 'w', encoding='utf8').write(v + '\n')
d = json.load(open(SRC + '/deck.json', encoding='utf8'))
d['order'] = ['summary', 'pnl', 'decision']
d['title'] = 'Modern Grid 샘플: AI 업무 플랫폼 타당성 검토'
d['cover'] = 'summary'
d['sections'] = {'s0': {'description': 'Modern Grid 디자인 샘플(원 덱 02·21·34장)', 'start': 'summary'}}
d['faces']['inter-tight'] = {'family': 'Inter Tight', 'href': 'https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;700&display=swap'}
for k in ('anim', 'lists'):
    pass
json.dump(d, open(OUT + '/deck.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('ok', list(slides))
