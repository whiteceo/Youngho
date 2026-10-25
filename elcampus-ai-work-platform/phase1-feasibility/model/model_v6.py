# 손익 모델 v6 (단위: 만 원). 계산기용 입력값·계산식. 근거: research-org.md, research-market.md
P=dict(
 DEV=775, UX=516,              # KOSA 2026 응용SW개발자·UI/UX디자이너 월(회사 부담 총액)
 dev_fte=2.0, ux_fte=1.0,      # 개발자 4명 x 50%, UIX 2명 x 50% (출시 전·후 모두)
 dev_months=9,                 # 개발 인력 작업량 16.25개월분 / 2.0명분 = 약 8.1개월 → 9개월
 pm=610,                       # 경력 PM 1명 신규 채용(5년차 이상, 연 5,000~7,000만 x 1.2~1.25 = 월 500~730), 기준 연 6,000만 x 약 1.22
 once_cash=531+500+300+550+2000, # 설계 전문가 0.5개월(외부), MSP 구축, 법률, 보안 점검, AI 교육 콘텐츠
 fixed_cash=150+150+325+45+10+17.5+100, # AWS 공용, MSP 월정액, 마케팅, 운영 도구, 운영자 PC, 보험, 야간·주말 장애 대응
 var=29, onb=65, churn=0.02, N=3, arpu=80,
 cut_after=0, cut_to=1100,      # 출시 n개월 뒤 사내 투입을 월 cut_to로 줄이는 민감도(0이면 미적용)
 internal_rate=None,           # 사내 인건비 기준 월 합계(예: 1250). None이면 DEV·UX 시장 인건비
)
def internal_month(p): return p['internal_rate'] if p['internal_rate'] else p['dev_fte']*p['DEV']+p['ux_fte']*p['UX']
def capex(p,incl=True): return p['once_cash']+p['pm']*p['dev_months']+(internal_month(p)*p['dev_months'] if incl else 0)
def fixed(p,m,incl=True):
    f=p['fixed_cash']+p['pm']
    if incl: f+= p['cut_to'] if (p['cut_after'] and m>p['cut_after']) else internal_month(p)
    return f
def sim(p,incl=True,months=120):
    n=0;cum=-capex(p,incl);be=pay=None;low=cum;yr=[];R=C=V=F=O=0
    for m in range(1,months+1):
        n=n*(1-p['churn'])+p['N']
        rev=n*p['arpu']; v=n*p['var']; f=fixed(p,m,incl); o=p['N']*p['onb']
        pr=rev-v-f-o; cum+=pr; low=min(low,cum); R+=rev;V+=v;F+=f;O+=o
        if be is None and pr>=0: be=(m,round(n))
        if pay is None and cum>=0: pay=m
        if m%12==0: yr.append(dict(n=round(n),rev=R,var=V,fix=F,onb=O,op=R-V-F-O,cum=cum));R=V=F=O=0
    return dict(be=be,pay=pay,pay_start=(pay+p['dev_months']) if pay else None,trough=low,yr=yr)
def solve(p,cond,incl=True,lo=20,hi=600):
    for _ in range(40):
        mid=(lo+hi)/2
        if cond(dict(p,arpu=mid),incl): hi=mid
        else: lo=mid
    return hi
def arpu_margin(p,incl,margin,year=3):
    return solve(p,lambda x,i:(lambda y:y['op']>=margin*y['rev'])(sim(x,i)['yr'][year-1]),incl)
def arpu_payback(p,incl,years):
    return solve(p,lambda x,i:(lambda s:s['pay'] is not None and s['pay']+x['dev_months']<=years*12)(sim(x,i)),incl)
def ym(m):
    if m is None: return '10년 안에 못 함'
    y,mm=divmod(m,12); return f"{y}년 {mm}개월" if y and mm else (f"{y}년" if y else f"{mm}개월")
