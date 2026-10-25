from model_v6 import *
def ymk(m):
    if m is None: return None
    y,mm=divmod(int(round(m)),12)
    return f"{y}년 {mm}개월" if y and mm else (f"{y}년" if y else f"{mm}개월")
def eok(x,sign=True):
    v=x/1e4
    s=f"{abs(v):.2f}억 원"
    if not sign: return s
    return ("−" if v<0 else "+")+s if round(v,2)!=0 else "0.00억 원"
def ytable(N):
    a=sim(dict(P,N=N),True); b=sim(dict(P,N=N),False)
    rows=[('연말 고객 수',[f"{y['n']}곳" for y in a['yr'][:5]]),
          ('매출',[eok(y['rev'],False) for y in a['yr'][:5]]),
          ('변동비',[eok(y['var'],False) for y in a['yr'][:5]]),
          ('고정비(사내 인력 포함)',[eok(y['fix'],False) for y in a['yr'][:5]]),
          ('그중 사내 인력(기회비용)',[eok(2066*12,False)]*5),
          ('온보딩',[eok(y['onb'],False) for y in a['yr'][:5]]),
          ('연간 손익(사내 인력 포함)',[eok(y['op']) for y in a['yr'][:5]]),
          ('누적 손익(사내 인력 포함, 출시 전 투자 2.57억 포함)',[eok(y['cum']) for y in a['yr'][:5]]),
          ('연간 손익(현금 기준)',[eok(y['op']) for y in b['yr'][:5]]),
          ('누적 손익(현금 기준, 출시 전 현금 0.71억 포함)',[eok(y['cum']) for y in b['yr'][:5]])]
    out="| | 1년차 | 2년차 | 3년차 | 4년차 | 5년차 |\n|---|---|---|---|---|---|\n"
    for k,v in rows: out+=f"| {k} | "+" | ".join(v)+" |\n"
    return out,a,b
def be(r): return f"{ymk(r['be'][0])} · {r['be'][1]}곳" if r['be'] else "10년 안에 없음"
def pay(r,dm): return ymk(r['pay']+dm) if r['pay'] else "출시 후 10년 안에 못 함"
cases=[('기본 조건',{}),('해지율 매달 1%(1년 약 11%)',dict(churn=0.01)),('해지율 매달 3%(1년 약 31%)',dict(churn=0.03)),
('변동비 낮음(19만 원)',dict(var=19)),('변동비 높음(41만 원)',dict(var=41)),('ARPU 90만 원',dict(arpu=90)),('ARPU 65만 원(Lite가 많을 때)',dict(arpu=65)),('ARPU 45만 원(전부 Lite)',dict(arpu=45)),
('PM을 경력자로 영입(월 475만 원)',dict(pm=475)),('개발 기간 11개월(겸직 전환 비용 반영)',dict(dev_months=11)),
('출시 1년 뒤 사내 투입을 월 1,100만 원으로 축소',dict(cut_after=12)),('사내 인력을 사내 인건비로 환산(월 1,250만 원)',dict(internal_rate=1250)),
('AI 코딩 도구 사용(개발 7개월, 도구 월 50만 원)',dict(dev_months=7,fixed_cash=P['fixed_cash']+50,once_cash=P['once_cash']+350)),
('사내 플랫폼 재활용, 재사용 100%(개발 7.5개월)',dict(dev_months=7.5)),
('AI 교육 콘텐츠 제작비·야간 장애 대응비를 낮게 잡은 경우(500만 원, 월 50만 원)',dict(once_cash=P['once_cash']-1500,fixed_cash=P['fixed_cash']-50)),
('AI 교육 콘텐츠 제작비·야간 장애 대응비를 높게 잡은 경우(4,000만 원, 월 150만 원)',dict(once_cash=P['once_cash']+2000,fixed_cash=P['fixed_cash']+50))]
def sens():
    out="| 바꾼 조건 | 매달 신규 | 월 흑자 전환(출시 후, 사내 인력 포함) | 투자 회수(착수 후, 사내 인력 포함) | 투자 회수(착수 후, 현금 기준) | 최대 누적 적자(사내 인력 포함 / 현금 기준) |\n|---|---|---|---|---|---|\n"
    for lab,kw in cases:
        for N in (3,4):
            q=dict(P,N=N); q.update(kw); dm=int(round(q['dev_months']+0.01))
            a=sim(q,True); b=sim(q,False)
            out+=f"| {lab} | {N}곳 | {be(a)} | {pay(a,dm)} | {pay(b,dm)} | {eok(-a['trough'],False)} / {eok(-b['trough'],False)} |\n"
    for N in (2,1):
        q=dict(P,N=N); a=sim(q,True); b=sim(q,False)
        out+=f"| 신규가 적을 때 | {N}곳 | {be(a)} | {pay(a,9)} | {pay(b,9)} | {eok(-a['trough'],False)} / {eok(-b['trough'],False)} |\n"
    return out
def need():
    o1="| 매달 신규 | 손익분기(영업이익률 0%) | 영업이익률 10% | 영업이익률 20% |\n|---|---|---|---|\n"
    o2="| 매달 신규 | 착수 후 3년 | 착수 후 4년 | 착수 후 5년 |\n|---|---|---|---|\n"
    for N in (2,3,4):
        q=dict(P,N=N); qi=dict(q,internal_rate=1250)
        f=lambda m:f"{arpu_margin(q,True,m):.0f}만 원 / {arpu_margin(qi,True,m):.0f}만 원 / {arpu_margin(q,False,m):.0f}만 원"
        o1+=f"| {N}곳 | {f(0)} | {f(0.1)} | {f(0.2)} |\n"
        g=lambda Y:f"{arpu_payback(q,True,Y):.0f}만 원 / {arpu_payback(qi,True,Y):.0f}만 원 / {arpu_payback(q,False,Y):.0f}만 원"
        o2+=f"| {N}곳 | {g(3)} | {g(4)} | {g(5)} |\n"
    return o1,o2
t3,a3,b3=ytable(3); t4,a4,b4=ytable(4)
o1,o2=need()
open('ch5_tables.md','w').write("T3\n"+t3+"\nT4\n"+t4+"\nSENS\n"+sens()+"\nNEED1\n"+o1+"\nNEED2\n"+o2)
print(open('ch5_tables.md').read())
