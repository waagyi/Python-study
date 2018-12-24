print('TIMER0 INTERRUPT CACULATOR')
print('\n')

print('OverFlowTime= 4 x Tosc x PS x (256-TMROL)')
print('\n')
f=input('ENTER SYSTEM FREQUENCY(eg ,4e6):')
t=1.0/f;
ps=input('PS ranging 2 to 256(x2 inc):')
oft=input('Enter desire overflow time:(eg 20e-3)')
tmr0l=256.0-(oft/(4.0*t*ps));
print(tmrol);
x=input('press any key to exit');