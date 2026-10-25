from model_v6 import *
p=dict(P)
print('사내/월',internal_month(p),'CAPEX 경제',capex(p),'현금',capex(p,False),'고정 경제',fixed(p,1),'현금',fixed(p,1,False))
for N in (3,4):
    for incl in (True,False):
        r=sim(dict(p,N=N),incl)
        print('N',N,'incl',incl,'be',r['be'],'pay 출시후',ym(r['pay']),'착수후',ym(r['pay_start']),'trough',round(r['trough']))
        for y in r['yr'][:5]: print('   ',{k:(round(v/1e4,2) if k!='n' else v) for k,v in y.items()})
print('--- 필요 ARPU (출시 후 3년차 기준)')
for N in (2,3,4):
    q=dict(p,N=N)
    row=[]
    for incl,tag in ((True,'경제'),(False,'현금')):
        row.append(f"{tag}: 손익0 {arpu_margin(q,incl,0):.0f} / 10% {arpu_margin(q,incl,0.1):.0f} / 20% {arpu_margin(q,incl,0.2):.0f} | 착수후 회수 3·4·5년 {arpu_payback(q,incl,3):.0f}·{arpu_payback(q,incl,4):.0f}·{arpu_payback(q,incl,5):.0f}")
    q2=dict(q,internal_rate=1250)
    row.append(f"사내인건비: 손익0 {arpu_margin(q2,True,0):.0f} / 10% {arpu_margin(q2,True,0.1):.0f} / 20% {arpu_margin(q2,True,0.2):.0f} | 회수 {arpu_payback(q2,True,3):.0f}·{arpu_payback(q2,True,4):.0f}·{arpu_payback(q2,True,5):.0f}")
    print('N',N); [print('  ',x) for x in row]
print('--- 민감도 (ARPU 80)')
cases=[('기본',{}),('해지 1%',dict(churn=0.01)),('해지 3%',dict(churn=0.03)),('변동비 19',dict(var=19)),('변동비 41',dict(var=41)),
('ARPU 90',dict(arpu=90)),('ARPU 65',dict(arpu=65)),('ARPU 45',dict(arpu=45)),('PM 경력자 475',dict(pm=475)),('개발 11개월(겸직 전환 비용)',dict(dev_months=11)),
('출시 1년 뒤 사내 투입 월 1,100',dict(cut_after=12)),('사내 인건비 기준 1,250',dict(internal_rate=1250)),
('AI 코딩 도구(개발 7개월, 월 50)',dict(dev_months=7,fixed_cash=P['fixed_cash']+50,once_cash=P['once_cash']+350)),
('사내 플랫폼 재사용 100%(개발 7.5개월)',dict(dev_months=7.5)),
('콘텐츠 500·장애 50',dict(once_cash=P['once_cash']-1500,fixed_cash=P['fixed_cash']-50)),('콘텐츠 4000·장애 150',dict(once_cash=P['once_cash']+2000,fixed_cash=P['fixed_cash']+50))]
for lab,kw in cases:
    for N in (3,4):
        q=dict(p,N=N); q.update(kw); q['dev_months']=kw.get('dev_months',p['dev_months'])
        a=sim(q,True); b=sim(q,False)
        dm=q['dev_months']
        ps=lambda r: ym(r['pay']+round(dm)) if r['pay'] else '10년 안에 못 함'
        print(f"{lab} | {N}곳 | 흑자 {a['be'][0] if a['be'] else '-'}개월·{a['be'][1] if a['be'] else '-'}곳 | 회수(착수후,경제) {ps(a)} | 회수(착수후,현금) {ps(b)} | 최대적자 경제 {-a['trough']/1e4:.2f} 현금 {-b['trough']/1e4:.2f} | 3년차 말 누적(출시후) {a['yr'][2]['cum']/1e4:.2f}")
for N in (1,2):
    q=dict(p,N=N); a=sim(q,True); b=sim(q,False)
    print('N',N,'경제',a['be'],ym(a['pay_start']),'현금',b['be'],ym(b['pay_start']), round(-a['trough']/1e4,2), round(-b['trough']/1e4,2))
